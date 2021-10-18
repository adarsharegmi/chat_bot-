import asyncio
from webapi import settings
from webapi import create_app
from sanic_cors import CORS, cross_origin


from sanic import response
from sanic_session import Session, InMemorySessionInterface

app = asyncio.run(create_app(settings.settings_factory()))
app.config.FALLBACK_ERROR_FORMAT = "json"
app.config.DEBUG = True
app.config.AUTO_RELOAD = True
CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0, http://128.199.156.12"}})


session = Session(app, interface=InMemorySessionInterface())


@app.main_process_start
async def start_db(request, loop):
    await app.ctx.db.connect()
    print("DB Connected")


@app.main_process_stop
async def stop_db(request, loop):
    await app.ctx.db.disconnect()
    print("DB Disconnected")


@app.get("/")
async def hello_world(request):
    return response.json({"success": "Hello, Chat Module."})


# @app.middleware("request")
async def verify_user(request):
    token = None
    if "sign_in" in request.headers:
        if request.url == settings.settings_factory().SIGN_IN_URL:
            print("matched")
            pass
        else:
            return response.json("Invalid url for login")
    elif "sign_up" in request.headers:
        if request.url == settings.settings_factory().SIGN_UP_URL:
            print("matched")
            pass
        else:
            return response.json("Invalid url for register")
    else:
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return response.json({"message": "Token is missing !!"}, 401)
        try:
            import jwt

            secret_key = settings.settings_factory().secret_key
            data = jwt.decode(token, secret_key, algorithms="HS256")
            email = data["email"]
            if email:
                pass
            else:
                return response.json({"message": "Please Log in Again!!"}, 403)
        except Exception as e:
            return response.json({"message": f"{e}"}, 403)


def main():
    app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=False)


# auto reload setting True does not work for poetry


if __name__ == "__main__":
    main
