#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
**💞 乛𝘼𝙇𝙊𝙉𝙀🕊️⃝🦋⁪⁬𝙈𝙐𝙎𝙄𝘾**
**🌹️ 𝐂нατ:** {message.chat.title} [`{message.chat.id}`]
**🥀 𝐔ѕєя:** {message.from_user.mention}
**🌸 𝐔ѕєяиαмє:** @{message.from_user.username}
**🌷 𝐔ѕєя 𝐈∂:** `{message.from_user.id}`
**🌿 𝐂нατ 𝐋ιиκ:** {chatusername}
**🌻 𝐐υєяγ:** {message.text}
**💐 𝐒τяєαмτγρє:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
