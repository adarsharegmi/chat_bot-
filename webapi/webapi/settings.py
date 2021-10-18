import os
import typing
from pydantic import PostgresDsn
from dotenv import load_dotenv, find_dotenv
from addy_core.lib.settings import AbstractSettings


load_dotenv(find_dotenv())
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_HOST = os.environ.get("HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "postgres")


class Settings(AbstractSettings):
    pg_dsn: PostgresDsn
    redis_settings: typing.Dict
    components: typing.List[str]
    secret_key: str
    alembic_config: str
    email_host: str
    email_port: str
    page_size: int
    debug: bool
    token_life_time: int
    # SIGN_IN_URL: str
    # SIGN_UP_URL: str


def settings_factory() -> Settings:
    return Settings(
        pg_dsn=typing.cast(
            PostgresDsn,
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        ),
        components=[
            "hisab_keeper.company",
            "hisab_keeper.authentication",
            "hisab_keeper.ledger",
            "hisab_keeper.payment",
            "hisab_keeper.journal_voucher",
            "hisab_keeper.contra_entry",
            "hisab_keeper.receipt",
        ],
        secret_key="2#$%^&SDFGHJKLOIUYTR@#$%^&*987654#$%^&*kJHGF3$%^&*",
        redis_settings={"host": "0.0.0.0", "port": "6379"},
        alembic_config="alembic.ini",
        email_host="mailtrap_host",
        email_port="mailtrap_port",
        page_size=5,
        debug=True,
        token_life_time=18000
        # SIGN_IN_URL = "http://0.0.0.0:8000/api/v1/login_user",
        # SIGN_UP_URL = "http://0.0.0.0:8000/api/v1/register_user"
    )
