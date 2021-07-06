from telethon.tl import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)
from telethon.tl.functions.channels import GetFullChannelRequest

from userbot.events import register
from userbot import CMD_HELP


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Channel/group tidak valid`")
            return None
        except ChannelPrivateError:
            await event.reply("`Ini adalah channel / grup pribadi atau saya diblokir sana`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Saluran atau supergrup tidak ada`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Channel/group tidak valid`")
            return None
    return chat_info


@register(outgoing=True, pattern=r"^\.inviteall(?: |$)(.*)")
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        kaisar = await event.reply("`proses...`")
    else:
        kaisar = await event.edit("`proses...`")
    kaisartes = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await kaisar.edit("`Maaf, Silahkan menambahkan pengguna di sini`")
    s = 0
    f = 0
    error = 'None'

    await kaisar.edit("**Terminal Status**\n\n`Koleksi Member.......`")
    async for user in event.client.iter_participants(kaisartes.full_chat.id):
        try:
            if error.startswith("Too"):
                return await kaisar.edit(f"**Terminal Selesai dengan kesalahan**\n(`Mungkin mendapat kesalahan batas dari telethon silahkan coba lagi nanti`)\n**Error** : \n`{error}`\n\n• Invited `{s}` Member \n• Gagal Menambahkan `{f}` Member")
            await event.client(functions.channels.InviteToChannelRequest(channel=chat, users=[user.id]))
            s = s + 1
            await kaisar.edit(f"**Terminal Running...**\n\n• Invited `{s}` Member \n• Gagal Menambahkan `{f}` Member\n\n**× LastError:** `{error}`")
        except Exception as e:
            error = str(e)
            f = f + 1
    return await kaisar.edit(f"**Terminal Finished** \n\n• Sukses Menambahkan `{s}` Member \n• Gagal Menambahkan `{f}` Member")


CMD_HELP.update({
    "invite":
      "\n\nPenggunaan: .inviteall link group lain\
       \n\nPenjelasan: Fungsinya menambahkan member dari group lain ke group anda."
})
