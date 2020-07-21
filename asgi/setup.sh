#!/usr/bin/env bash
brew install wrk
python3 -m pip install starlette uvicorn falcon==3.0.0a1 sanic responder molten blacksheep

# inspired by https://deepsource.io/blog/new-python-web-frameworks/