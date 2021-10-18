import json
from pydantic import ValidationError
from sanic import response
from sanic.views import HTTPMethodView

from addy_core.lib import err_msg
from addy_core.lib.json_encoder import jsonable_encoder
from webapi.messagebus import messagebus


class ChatView(HTTPMethodView):
    async def get(self, request, id_):
        return response.json({"error": "you are Addy"}, status=200)

    async def post(self, request):
        return response.json({"ERr": "You called post method"}, status=200)

    async def put(self, request, id_):
        return response.json({"error": "you are not authorized"}, status=403)

    async def delete(self, request, id_):
        return response.json({"suceess": "STH deleted successfully"}, status=200)
