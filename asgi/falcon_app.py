import falcon.asgi


class Resource:

    async def on_get(self, req, resp):
        resp.media = f'Hello, World!'
        resp.status = 200


# -- snip --


app = falcon.asgi.App()
app.add_route('/', Resource())
