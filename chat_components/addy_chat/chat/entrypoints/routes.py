from sanic import Blueprint
from addy_chat.chat.entrypoints import route_handler

chat_module = Blueprint("chat_module", url_prefix="api/v1/")


chat_module.add_route(
    route_handler.ChatView.as_view(),
    "chat_module/<id_>",
)
