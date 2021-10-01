from sanic import Blueprint
from sanic.response import text

bp = Blueprint(__name__)


@bp.exception(Exception)
async def oops(request, exception):
    return text("OOops")
