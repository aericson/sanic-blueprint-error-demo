from sanic import Sanic
from sanic.response import text

import sentry_sdk

sentry_sdk.init(
    dsn="https://3ff613d66c074adb89ff2e61b4a1f4b1@o119926.ingest.sentry.io/5996019",
    environment="dev",
)


def init_app():
    app = Sanic("MyHelloWorldApp")

    @app.get("/")
    async def hello_world(request):
        return text("Hello World!\n")

    return app
