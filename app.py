from sanic import Sanic

from errors import bp


def init_app():
    app = Sanic("MyHelloWorldApp")

    @app.get("/")
    async def hello_world(request):
        raise Exception("this is an exception")

    app.blueprint(bp)

    return app
