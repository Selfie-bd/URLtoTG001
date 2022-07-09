#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, logging
from pyrogram import Client

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

download_path = "Downloads/"

api_id = int(os.environ.get("API_ID",1976680))
api_hash = os.environ.get("API_HASH","9073255ce64a6072a59099803493f97d")
bot_token =os.environ.get("BOT_TOKEN","5054079474:AAEWJ98jMZviPm9u2UVQdfbywns8sWITouM")

class Config:
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS").split())
    TIMEOUT = 0
    MAX_SIZE = 9 * 1024 * 1024 * 1024
    CUSTOM_THUMB = None
    EDIT_TIME = 3
    DOWNLOAD_DIRECTORY = "Downloads/"
    SP_LIT_ALGO_RITH_M= "hjs"
    MAX_TG_SPLIT_FILE_SIZE = 1.92 * 1024 * 1024 * 1024
    TG_MAX_FILE_SIZE = 1.92 * 1024 * 1024 * 1024
    
    
if __name__ == "__main__":
    if not os.path.isdir(download_path):
        os.mkdir(download_path)
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "URLtoTG",
        bot_token=bot_token,
        api_id=api_id,
        api_hash=api_hash,
        plugins=plugins,
        workdir=download_path
    )
    LOGGER.info('Starting Bot !')
    app.run()
    LOGGER.info('Bot Stopped !')
