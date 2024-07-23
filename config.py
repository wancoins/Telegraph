import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7444352696:AAHbFC2nSrX1TZD4_tJcbklsnyA5DDWqdc0")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")
