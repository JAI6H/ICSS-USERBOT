# Hey There
import os
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger

import heroku3
from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient as tc
from telethon.sessions import StringSession as ss

from .Config import Config

StartTime = time.time()
icsv = "1.0.0"

if Config.STRING_SESSION:
    session_name = str(Config.STRING_SESSION)
    if session_name.endswith("="):
        bot = tc(ss(session_name), Config.APP_ID, Config.API_HASH)
    else:
        bot = tc("TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH).start(
            bot_token=Config.STRING_SESSION
        )
else:
    session_name = "startup"
    bot = tc(session_name, Config.APP_ID, Config.API_HASH)


ICSS_ID = ["1588663614", "1233775025"]

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
    )
LOGS = getLogger(__name__)

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None

# Global Configiables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}
