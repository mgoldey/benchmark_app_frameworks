from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return f'Hello, World!'


app = Starlette(debug=True, routes=[Route('/', homepage)])
