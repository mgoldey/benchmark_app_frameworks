#!/usr/bin/env python3

import socket
import fire

try:
    from cheroot.wsgi import Server as WSGIServer
except ImportError:
    from cherrypy.wsgiserver import CherryPyWSGIServer as WSGIServer

def main(app):
    if app=="falcon":
        from falcon_app import application
    else:
        from flask_app import application

    server = WSGIServer(
        bind_addr=('0.0.0.0', 8000),
        wsgi_app=application,
        request_queue_size=500,
        server_name=socket.gethostname()
    )
    try:
        server.start()
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()

fire.Fire(main)