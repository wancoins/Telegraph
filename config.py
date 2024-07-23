import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7444352696:AAHbFC2nSrX1TZD4_tJcbklsnyA5DDWqdc0")

    APP_ID = int(os.environ.get("APP_ID", 8447214))

    API_HASH = os.environ.get("API_HASH", "9ec5782ddd935f7e2763e5e49a590c0d")
