import os
from dataclasses import dataclass

BOT_TOKEN = os.environ.get("BOT_TOKEN") or "123"
ADMIN_ID = os.environ.get("ADMIN_ID") or "123"


@dataclass
class TgBot:
    token: str
    admin_id: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config() -> Config:
    return Config(tg_bot=TgBot(token=BOT_TOKEN, admin_id=ADMIN_ID))
