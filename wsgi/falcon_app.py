# default falcon application

import falcon

class Index(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('Hello world from falcon')

application = falcon.API()

application.add_route('/', Index())
