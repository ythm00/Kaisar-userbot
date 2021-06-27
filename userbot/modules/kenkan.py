# Dibuat kenkan @kenkanasw
import os
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.events import register
from userbot import bot, TEMP_DOWNLOAD_DIRECTORY, CMD_HELP

@register(outgoing=True, pattern=".butt")
async def _(butt):
  await butt.edit("Kaisar mencoba membuat button")
  level=butt.pattern_match.group(2)
  if butt.fwd_from:
    return
  if not butt.reply_to_msg_id:
    await butt.edit("Mohon Kaisar balas ke media")
    return
  reply_message = await butt.get_reply_message()
  if not reply_message.media:
    await butt.edit("`Gambar tidak di dukung`")
    return
  if reply_message.sender.bot:
    await butt.edit("`Mohon Balas Di Media Kaisar`")
    return
    chat = "@ForwardsCoverbot"
    message_id_to_reply = butt.message.reply_to_msg_id
  async with butt.client.conversation(chat) as conv:
    try:
      msg = await conv.send_message(reply_message)
      if level:
      m = f"/addbutton {level}"
      msg_level = await conv.send_message(
      m,
      reply_to=msg.id)
      r = await conv.get_response()
      response = await conv.get_response()
        else:
          response = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await butt.reply("`Kaisar Mohon Unblock` @ForwardsCoverbot`...`")
              return
          if response.text.startswith("Forward"):
              await butt.edit("`Kaisar Mohon Matikan Setelan Forward Privasi...`")
          else:
              downloaded_file_name = await butt.client.download_media(
                  response.media,
                  TEMP_DOWNLOAD_DIRECTORY
              )
              await butt.client.send_file(
                  butt.chat_id,
                  downloaded_file_name,
                  force_document=False,
                  reply_to=message_id_to_reply
              )
              """ - cleanup chat after completed - """
              
CMD_HELP.update:({
  ".butt"
  ".butt:\
  \nUsage: Menambahkan button link pada media.\
  \nFormat:tautan pertama=https://telegram.org && tautan kedua baris yang sama=https://google.it &&& tautan ketiga baris baru=https://t.me"
})
  
