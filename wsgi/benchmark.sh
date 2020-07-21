#!/usr/bin/env bash

function wait_until_up {
	while true; do
		curl localhost:8000 2>/dev/null && break
		sleep 0.25
	done
}

function run_benchmark {
	wrk -c 1 -t 1 -d 1 http://localhost:8000 > "${1}_${2}.log"
}

for app in falcon flask; do 
	for wsgi in cherrypy meinheld twisted bjoern; do
		python3 ${wsgi}.wsgi $app &
		pid=$!
		wait_until_up
		run_benchmark $wsgi $app
		kill -9 $pid
		sleep 1
	done
done


gunicorn -w 1 falcon_app:application &
pid=$!
wait_until_up
run_benchmark gunicorn falcon
kill -9 $pid
sleep 1

gunicorn -w 1 flask_app:application &
pid=$!
wait_until_up
run_benchmark gunicorn flask
kill -9 $pid
sleep 1

uwsgi --http :8000 --wsgi-file falcon_app.py &
pid=$!
wait_until_up
run_benchmark uwsgi falcon
kill -9 $pid

# something needs to release here and doesn't do it quickly
pkill -9 uwsgi
sleep 10 

uwsgi --http :8000 --wsgi-file flask_app.py &
pid=$!
wait_until_up
run_benchmark uwsgi flask
kill -9 $pid
pkill -9 uwsgi
