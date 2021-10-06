from sanic import Sanic
from sanic.response import text

import sentry_sdk

sentry_sdk.init(
    dsn=None,
    environment="dev",
)


def init_app():
    app = Sanic("MyHelloWorldApp")

    @app.get("/")
    async def hello_world(request):
        raise text("Hello World!\n")

    return app
