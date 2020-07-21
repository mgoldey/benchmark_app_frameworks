
import fire
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource

def main(app):
    if app=="falcon":
        from falcon_app import application
    else:
        from flask_app import application
    resource = WSGIResource(reactor, reactor.getThreadPool(), application)

    port = 8000
    host = '127.0.0.1'

    # Alternatively, use reactor.listenSSL
    reactor.listenTCP(port, Site(resource), interface=host)
    reactor.run()

fire.Fire(main)