from sanic import Sanic


from webapi.bootstrap import init_database
from addy_chat.chat.entrypoints.routes import chat_module

app = Sanic("AddyChat", register=True)


async def create_app(settings):
    app.blueprint(chat_module)
    db = init_database(settings)
    app.ctx.settings = settings
    app.ctx.db = db
    return app
