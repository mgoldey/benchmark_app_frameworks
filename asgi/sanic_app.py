from sanic import Sanic

app = Sanic()


@app.route('/')
async def test(request):
    return f'Hello, World!'
