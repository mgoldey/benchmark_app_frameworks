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

for framework in  fastapi starlette falcon sanic molten blacksheep; do
	for asgi in uvicorn daphne hypercorn; do
		$asgi "${framework}_app":app &
		pid=$!
		wait_until_up
		run_benchmark $asgi $framework
		kill -9 $pid
		pkill -9 $asgi
		sleep 0.25
	done
done

# framework=responder
# python3 -m pip install responder
# for asgi in uvicorn daphne hypercorn; do
# 	$asgi "${framework}_app":app &
# 	pid=$!
# 	wait_until_up
# 	run_benchmark $asgi $framework
# 	kill -9 $pid
# 	pkill -9 $asgi
# 	sleep 0.25
# done


# minimal uvicorn only example
uvicorn uvicorn_app:app &
pid=$!
wait_until_up
run_benchmark uvicorn uvicorn
kill -9 $pid
