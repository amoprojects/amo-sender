from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
import os

APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
session = os.environ.get("TERMUX")
app = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']
ispay2 = ['yes']


async def join_channel():
    try:
        await app(JoinChannelRequest("https://t.me/doneamo"))
        await app(JoinChannelRequest("https://t.me/YuYxx"))
        await app(JoinChannelRequest("https://t.me/AmoSwap"))
        await app(JoinChannelRequest("https://t.me/Z_Q_Qi"))
    except BaseException:
        pass
