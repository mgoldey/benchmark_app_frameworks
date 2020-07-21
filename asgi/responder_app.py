import responder

app = responder.API()


@app.route("/")
async def greet_world(req, resp, *, greeting):
    resp.text = "Hello, world!"
