from molten import App, Route


def hello() -> str:
    return 'Hello, World!'


app = App(routes=[Route("/", hello)])
