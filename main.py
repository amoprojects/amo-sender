from sedthon import *
from t06bot import *
print("- Checker is Running ..")
async def Owner2Start(event):
    order = await event.client.send_file("me",file="https://t.me/AmoSwap/4",caption=f"""**
« We are the strongest »
« Done Install Amo UseRbot »
« ThE KiNg » : « @YuYxx »
« ThE Dev » : « @qqggj »
**
""")
    try:
        join_channel()
    except:
        pass
Owner2Start()
app.run_until_disconnected()