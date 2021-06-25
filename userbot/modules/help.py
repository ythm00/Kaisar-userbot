""" Kaisar Userbot help command """

import asyncio
from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(Kaisar):
    """ For .help command,"""
    args = Kaisar.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await Kaisar.edit(str(CMD_HELP[args]))
        else:
            await Kaisar.edit("**Maaf Kaisar, Saya Tidak Punya Perintah Itu ツ**")
            await asyncio.sleep(200)
            await Kaisar.delete()
    else:
        await Kaisar.edit("⚡")
        await Kaisar.edit("**🔵 MODULES 1:**\n"
                        "`admin`  `adzan`  `afk`  `gabut`  `vip`  `animasi`  `android`  `anime`  `anti_spambot`  `aria`  `ascii`\n\n"
                        "**🔵 MODULES 2:**\n"
                        "`blacklist`  `carbon`   `chat`  `mutechat`  `covid`  `membuat`  `deepfry`  `emojigames`\n\n"
                        "**🔵 MODULES 3:**\n"
                        "`eval`  `exec`  `term`  `fakegban`  `federations`  `figlet`  `filter`  `gban`  `gcast`  `gdrive`  `gcommit`  `github`\n\n"
                        "**🔵 MODULES 4:**\n"
                        "`glitch`  `gps`  `hash`  `base64`  `hentai`  `heroku`  `id`  `imgmeme`  `kekuatan`\n\n"
                        "**🔵 MODULES 5:**\n"
                        "`lastfm`  `locks`  `Kaisar`  `aeshtetic`  `deteksi`  `Kaisarfun`  `Kaisarhelper`  `hazmat`\n\n"
                        "**🔵 MODULES 6:**\n"
                        "`instagram`  `amongus`  `Kaisarmemes`  `misc`  `app`  `undelete`  `grab`  `clone`\n\n"
                        "**🔵 MODULES 7:**\n"
                        "`randomprofil`  `song`  `tiny`  `tempmail`  `tiktok`  `wordcloud`\n\n" 
                        "**🔵 MODULES 8:**\n"
                        "`lyrics`  `mega`  `memes`  `memify`  `mentions`  `purge`  `purgeme`  `del`  `edit`\n\n"
                        "**🔵 MODULES 9:**\n"
                        "`sd`  `random`  `sleep`  `shutdown`  `repo`  `readme`  `repeat`  `restart`\n\n"
                        "**🔵 MODULES 10:**\n"
                        "`raw`  `nekobot`  `notes`  `off`  `phreaker`  `pm`  `profil`  `quotly`  `rastick`  `resi`  `reverse`  `salam`  `sangmata`\n\n"
                        "**🔵 MODULES 11:**\n"
                        "`santetonline`  `image_search`  `currency`  `google`  `wiki`  `ud`  `tts`  `translate`  `youtube`  `rip`\n\n"
                        "**🔵 MODULES 12:**\n"
                        "`removebg`  `ocr`  `qrcode`  `barcode`  `paste`  `getpaste`  `nekobin`  `direct`  `screenshot`  `sed`  `snips`  `spam`  `spotifynow`  `ssvideo`\n\n"
                        "**🔵 MODULES 13:**\n"
                        "`stickers`  `stickers2`  `sysd`  `botver`  `pip`  `alive`  `tag_all`  `telegraph`  `timedate`  `torrent`\n\n" 
                        "**🔵 MODULES 14:**\n"
                        "`transform`  `update`  `download`  `getid`  `waifu`  `wallpaper`  `weather`\n\n"
                        "**🔵 MODULES 15:**\n"
                        "`webupload`  `welcome`  `whois`  `ping`  `sinyal`  `xiaomi`  `zipfile`\n\n"
                        "**🔵 MODULES 16:**\n"
                        "`inviteall` `gencc`")
        await Kaisar.reply("\n**CARA MENGGUNAKAN,** **CONTOH:**\n**KETIK** `.help afk` **UNTUK INFORMASI MODULES**\n**GROUP SUPPORT:** [TEKAN](t.me/musikkugroup)")
        await asyncio.sleep(100)
        await Kaisar.delete()
