# Benchmarking application frameworks with asynchronous server gateway interface (ASGI) and webserver gateway interface (WSGI) servers

In order to evaluate that I'm chosing a reasonably efficient web server for a machine learning (ML) service,
I performed a few quick tests for latency and requests served/second under low load conditions using the [wrk](https://github.com/wg/wrk) benchmarking tool.

For more exaustive tests, please consult 
- [the-benchmarker](https://github.com/the-benchmarker/web-frameworks)
- [techempower](https://www.techempower.com/benchmarks/#section=data-r19&hw=ph&test=composite&l=z8kflr-v&a=2)

## Why these in particular?
A number of inconsistencies remain for environments block scripted execution of these frameworks in all possible cases.
Independent virtual environments would work around those blockers if more exhaustive benchmarks are needed.
I've chosen to investigate the particular frameworks due to popularity and how quickly a toy "Hello, world!" example could be constructed.
This is an embarassingly weak proxy for documentation, code maintenance, and interoperability.
It is quite possible that different python package versions, CPU chips (I am using a 13 inch 2019 MBP),
and different load testing conditions in wrk would result in appreciably different performance.
No malice is intended against developers or users of any particular frameworks.

Also, interoperability of a framework with frontrunner ASGI and WSGI servers is important for future proofing
against any given application framework becoming obsolete. As such, standalone frameworks which did not work with common ASGIs or WSGIs were not tested.

# Results

## WSGI+framework performance in requests / second
![WSGI requests/sec](https://github.com/mgoldey/benchmark_app_frameworks/blob/master/plots/wsgi_request_speed.png)
## WSGI+framework performance in latency
![WSGI latency](https://github.com/mgoldey/benchmark_app_frameworks/blob/master/plots/wsgi_latency.png)

## ASGI+framework performance in requests / second
![ASGI requests/sec](https://github.com/mgoldey/benchmark_app_frameworks/blob/master/plots/asgi_request_speed.png)
## ASGI+framework performance in latency
![ASGI latency](https://github.com/mgoldey/benchmark_app_frameworks/blob/master/plots/asgi_latency.png)
