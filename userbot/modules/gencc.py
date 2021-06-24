
from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.gencc(?: |$)(.*)")
async def gencc(Kaisarevent):
    if Kaisarevent.fwd_from:
        return
    Kaisarcc = Faker()
    Kaisarname = Kaisarcc.name()
    Kaisaradre = Kaisarcc.address()
    Kaisarcard = Kaisarcc.credit_card_full()

    await edit_or_reply(Kaisarevent, f"__**👤 NAMA :- **__\n`{Kaisarname}`\n\n__**🏡 ALAMAT :- **__\n`{Kaisaradre}`\n\n__**💸 KARTU :- **__\n`{Kaisarcard}`")


@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def bin(event):
    if event.fwd_from:
        return
    Kaisar_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Pengecekan...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/bin {Kaisar_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.vbv(?: |$)(.*)")
async def vbv(event):
    if event.fwd_from:
        return
    Kaisar_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Pengecekan...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/vbv {Kaisar_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.key(?: |$)(.*)")
async def key(event):
    if event.fwd_from:
        return
    Kaisar_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Pengecekan...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/key {Kaisar_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.iban(?: |$)(.*)")
async def iban(event):
    if event.fwd_from:
        return
    Kaisar_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Pengecekan...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/iban {Kaisar_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.ccheck(?: |$)(.*)")
async def ccheck(event):
    if event.fwd_from:
        return
    Kaisar_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Pengecekan...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/ss {Kaisar_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.ccbin(?: |$)(.*)")
async def ccbin(event):
    if event.fwd_from:
        return
    Kaisar_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit(f" Mencoba menghasilkan CC dari bin yang diberikan `{Kaisar_input}`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/gen {Kaisar_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)

CMD_HELP.update({
    "ccarder": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gencc`\
\n↳ : Menghasilkan CC Palsu.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ccheck` <query>\
\n↳ : Memeriksa Apakah CC yang Diberikan Aktif atau Tidak.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.iban` <kueri>\
\n↳ : Memeriksa Apakah ID IBAN yang Diberikan Aktif atau Tidak.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.key` <kueri>\
\n↳ : Memeriksa status kunci yang diprobid.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vbv` <kueri>\
\n↳ : Memeriksa status vbv dari kartu yang diberikan.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.bin` <kueri>\
\n↳ : Memeriksa apakah bin yang diberikan valid atau tidak.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ccbin` <bin>\
\n↳ : Menghasilkan CC dari bin yang diberikan."
})