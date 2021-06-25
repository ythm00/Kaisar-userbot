from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern=r"^\.butn(?: |$)(.*)")
async def bin(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@ForwardsCoverBot"
    await event.edit("Kaisar sedang memprosesnya...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/addbuttons {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @ForwardsCoverBot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.rbutn(?: |$)(.*)")
async def vbv(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@ForwardsCoverBot"
    await event.edit("Kaisar sedang memprosesnya...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/removebuttons  {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @ForwardsCoverBot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.capt(?: |$)(.*)")
async def key(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@ForwardsCoverBot"
    await event.edit("Kaisar sedang memprosesnya...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/addcaption  {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @ForwardsCoverBot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.rcapt(?: |$)(.*)")
async def iban(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@ForwardsCoverBot"
    await event.edit("Kaisar sedang memprosesnya...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/removecaption  {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @ForwardsCoverBot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.dcwb(?: |$)(.*)")
async def ccheck(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@ForwardsCoverBot"
    await event.edit("Kaisar sedang memprosesnya...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/disablewebpagepreview  {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @ForwardsCoverBot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)

CMD_HELP.update({
  "fileforward":
    "butn : untuk menambahkan button pada file.\n"
    "rbutn : untuk menghapus button dari file.\n"
    "capt : untuk menambahkan caption pada file.\n"
    "rcapt : untuk menghapus caption pada file.\n"
    "dcwb : untuk menghapus penampil web."
})