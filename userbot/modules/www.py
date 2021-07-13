""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time
from time import sleep

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.fping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit(".                      /¯ )")
    await pong.edit(".                       /¯ )\n                      /¯  /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"┍━━☽【❖】☾━━┑\n       **⌖ PING!**\n┕━━☽【❖】☾━━┙\n"
                    f"\n  ➥ `%sms` \n"
                    f"**𖣘 KAISAR** "
                    f"\n  ➥ `{ALIVE_NAME}` \n" % (duration))
    

@register(outgoing=True, pattern="^.lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("⚡")
    await pong.edit("__**KAISAR⚡**__")
    await pong.edit("__**KAISA⚡R**__")
    await pong.edit("__**KAIS⚡AR**__")
    await pong.edit("__**KAI⚡SAR**__")
    await pong.edit("__**KA⚡ISAR**__")
    await pong.edit("__**K⚡AISAR**__")
    await pong.edit("__**⚡KAISAR⚡**__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"─━━━⊱༻⚡️༺⊰━━━─\n **     ⚡KAISAR PING⚡**\n"
                    f"⚡ **ᴘɪɴɢ:** "
                    f"`%sms` \n"
                    f"⚡ **ᴏɴʟɪɴᴇ:** "
                    f"`{uptime}` \n" % (duration))
  

@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Ping..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"┍━━☽【❖】☾━━┑\n       **⌖ PONG!**\n┕━━☽【❖】☾━━┙\n"
                    f"➠ __ＰＩＮＧ :__ "
                    f" `%sms` \n"
                    f"➠ __ＵＰＴＩＭＥ :__ "
                    f" `{uptime}` \n" % (duration))
     

@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**◢◤**")
    await pong.edit("**◢◤◢◤**")
    await pong.edit("**◢◤◢◤◢◤**")
    await pong.edit("**◢◤◢◤◢◤◢◤**")
    await pong.edit("**◢◤◢◤◢◤◢◤◢◤**")
    await pong.edit("**◢◤◢◤◢◤◢◤◢◤◢◤**")
    await pong.edit("**:۞: PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"┏━━━━━━༻❁༺━━━━━━┓\n ＫＡＩＳＡＲ-ＵＳＥＲＢＯＴ\n┗━━━━━━༻❁༺━━━━━━┛\n"
                    f":۞:ＰＩＮＧ:"
                    f" `%sms` \n"
                    f":۞:ＵＰＴＩＭＥ:"
                    f" `{uptime}` \n"
                    f"━━━━━━━━━━━━━━━━━━━\n"
                    f"** ❖  My кคเรคг :** `{ALIVE_NAME}`\n"
                    f"┗━━━━━━༻❁༺━━━━━━┛" % (duration))
      

@register(outgoing=True, pattern="^.sinyal$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"┏━━━━━━༻❁༺━━━━━━┓\n ＫＡＩＳＡＲ-ＵＳＥＲＢＯＴ\n┗━━━━━━༻❁༺━━━━━━┛\n"
                    f"**• ꜱɪɴʏᴀʟ :** "
                    f" `%sms`\n"
                    f"**• ᴏɴʟɪɴᴇ :** "
                    f" `{uptime}`\n"
                    f"**• ᴏᴡɴᴇʀ :** `{ALIVE_NAME}`\n"
                    f"┗━━━━━━༻❁༺━━━━━━┛" % (duration))
      

@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit(f"┏━━━━━━━༻❁༺━━━━━━━┓\n"
                     f"  ＫＡＩＳＡＲ-ＵＳＥＲＢＯＴ\n"
                     f"┣━━━━━━━༻❁༺━━━━━━━┛\n"
                     f"┣ **HASIL TES :\n**"
                     f"┣ 👤**Dimulai Pada : **\n"
                     f"┣`{result['timestamp']}` \n"
                     f"┣━━━━━━━━━━━━━━━━━━━━\n"
                     f"┣ 📥**Download :** `{speed_convert(result['download'])}` \n"
                     f"┣ 📤**Upload :** `{speed_convert(result['upload'])}` \n"
                     f"┣ 📡**Ping :** `{result['ping']}` \n"
                     f"┣ 🌍**ISP :** `{result['client']['isp']}` \n"
                     f"┗━━━━━━━༻❁༺━━━━━━━┛")
      

def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`ＰＯＮＧ━━━━━❮❮`")
    await pong.edit("`ＰＯＮＧ━━━━❮❮━`")
    await pong.edit("`ＰＯＮＧ━━━❮❮━━`")
    await pong.edit("`ＰＯＮＧ━━❮❮━━━`")
    await pong.edit("`ＰＯＮＧ━❮❮━━━━`")
    await pong.edit("`ＰＯＮＧ❮❮━━━━━`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"┏━━━━━━༻❁༺━━━━━━┓\n ＫＡＩＳＡＲ-ＵＳＥＲＢＯＴ\n┗━━━━━━༻❁༺━━━━━━┛\n"
                                 f"✘ ＰＩＮＧ! : `%sms`" % (duration))
    
@register(outgoing=True, pattern="^.kping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n")
    sleep(1)
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n█▓░░░░░░░░░\n")
    sleep(1)
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n█▓░░░░░░░░░\n█▓█▓░░░░░░░\n")
    sleep(1)
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n█▓░░░░░░░░░\n█▓█▓░░░░░░░\n█▓█▓█▓░░░░░\n")
    sleep(1)
    await pong.edit("░░░░░░░░░░░\n█▓░░░░░░░░░\n█▓█▓░░░░░░░\n█▓█▓█▓░░░░░\n█▓█▓█▓█▓░░░\n")
    sleep(1)
    await pong.edit("█▓░░░░░░░░░\n█▓█▓░░░░░░░\n█▓█▓█▓░░░░░\n█▓█▓█▓█▓░░░\n█▓█▓█▓█▓█▓░\n")
    sleep(1)
    await pong.edit("**[♦] PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"┏━━━━━━༻❁༺━━━━━━┓\n ＫＡＩＳＡＲ-ＵＳＥＲＢＯＴ\n┗━━━━━━༻❁༺━━━━━━┛\n"
                    f"[♦] ＰＩＮＧ:"
                    f" `%sms` \n"
                    f"[♦] ＵＰＴＩＭＥ:"
                    f" `{uptime}` \n"
                    f"━━━━━━━━━━━━━━━━━━━\n"
                    f"**[♦] My KAISAR  :** `{ALIVE_NAME}`\n"
                    f"┗━━━━━━༻❁༺━━━━━━┛" % (duration))
     


CMD_HELP.update(
    {"ping": "`.ping` ; `.lping` ; `.xping` ; `.fping` : `.kping`\
    \nPenjelasan: Untuk menunjukkan ping bot.\
    \n\n`.speed`\
    \nPenjelasan: Untuk menunjukkan kecepatan.\
    \n\n`.pong`\
    \nPenjelasan: sama kaya perintah ping."
     })
CMD_HELP.update(
    {"sinyal": "**Modules:** `Sinyal`\
    \n\n**• Perintah :** `.sinyal`\
    \n  ➥ **Penjelasan :** __Untuk melihat sinyal bot__"})
