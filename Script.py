class script(object):  
    START_TXT = """<b>✨ Hᴇʟʟᴏ {user}.

Mʏ Nᴀᴍᴇ Is {bot}.

I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇ Fᴏʀ Yᴏᴜ Jᴜsᴛ Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Oʀ Jᴏɪɴ Oᴜʀ Gʀᴏᴜᴘ</b>"""

    HELP_TXT = "Hᴇʏ {}\nHᴇʀᴇ Mꜱ Mʏ Hᴇʟᴩ"

    ABOUT_TXT = """ 
╔════❰ 𝙼𝙾𝚅𝙸𝙴 𝙱𝙾𝚃 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/movie_bot_by_firos_bot>𝕄𝕆𝕍𝕀𝔼 𝔹𝕆𝕋</a>
║┣⪼👦ᴅᴇᴠ  : <a href=https://t.me/firossha>ғɪʀᴏs</a>
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ3</a>
║┣⪼📚ʟɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a> 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : 𝕄𝕆𝕍𝕀𝔼 𝔹𝕆𝕋 v2.0
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ """   
    SOURCE_TXT = """ 
╔════❰ 𝙼𝙾𝚅𝙸𝙴 𝙱𝙾𝚃 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼❣️sᴏᴜʀᴄᴇ ᴄᴏᴅ : <a href=https://github.com/firossha321/Movie_bot>ᴍᴏᴠɪᴇ ʙᴏᴛ</a>
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ3</a>
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : 𝙼𝙾𝚅𝙸𝙴 𝙱𝙾𝚃 v2.0
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ """

    FILE_TXT = """<b>➤ Hᴇʟᴘ Fᴏʀ Fɪʟᴇ Sᴛᴏʀᴇ</b>

<i>Bʏ Usɪɴɢ Tʜɪs Mᴏᴅᴜʟᴇ Yᴏᴜ Cᴀɴ Sᴛᴏʀᴇ Fɪʟᴇs Iɴ Mʏ Dᴀᴛᴀʙᴀsᴇ Aɴᴅ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ A Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ  Tᴏ Aᴄᴄᴇss Tʜᴇ Sᴀᴠᴇᴅ Fɪʟᴇs. Iғ Yᴏᴜ Wᴀɴᴛ Tᴏ Aᴅᴅ Fɪʟᴇs Fʀᴏᴍ A Pᴜʙʟɪᴄ Cʜᴀɴɴᴇʟ Sᴇɴᴅ Tʜᴇ Fɪʟᴇ Lɪɴᴋ Oɴʟʏ  Oʀ Yᴏᴜ Wᴀɴᴛ Tᴏ Aᴅᴅ Fɪʟᴇs Fʀᴏᴍ A  Pʀɪᴠᴀᴛᴇ Cʜᴀɴɴᴇʟ Yᴏᴜʀ Mᴜsᴛ Mᴀᴋᴇ Mᴇ Aᴅᴍɪɴ Oɴ Tʜᴇ Cʜᴀɴɴᴇʟ Tᴏ Aᴄᴄᴇss Fɪʟᴇs</i>

<b>⪼ Cᴏᴍᴍᴀɴᴅ & Usᴀɢᴇ</b>
➪ /link › Rᴇᴘʟʏ Tᴏ Aɴʏ Mᴇᴅɪᴀ Tᴏ Gᴇᴛ Tʜᴇ Lɪɴᴋ 
➪ /batch › Tᴏ Cʀᴇᴀᴛᴇ Lɪɴᴋ Fᴏʀ Mᴜʟᴛɪᴘʟᴇ Mᴇᴅɪᴀ

<b>⪼ EG:</b>
</code>/batch https://t.me/firosshamuhammad https://t.me/firossh</code>"""

    FILTER_TXT = "Sᴇʟᴇᴄᴛ Wʜɪᴄʜ Oɴᴇ Yᴏᴜ Wᴀɴᴛ...✨"

    GLOBALFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs</b>

<i>Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ Bᴏᴛ  Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ</i>

<b>Nᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /gfilter - Tᴏ Aᴅᴅ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs
• /gfilters - Tᴏ Vɪᴇᴡ Lɪsᴛ Oғ Aʟʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs
• /delg - Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ
• /delallg - Tᴏ Dᴇʟᴇᴛᴇ Aʟʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀꜱ

• /g_filter off Usᴇ Tʜɪs Cᴏᴍᴍᴏᴀɴᴅ + on/offғ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Tᴏ Cᴏɴᴛʀᴏʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ"""

    MANUELFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ Fɪʟᴛᴇʀs</b>

<i>Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ Bᴏᴛ  Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ</i>

<b>Nᴏᴛᴇ:</b>
𝟷. Tʜɪs Bᴏᴛ Sʜᴏᴜʟᴅ Hᴀᴠᴇ Aᴅᴍɪɴ Pʀɪᴠɪʟʟᴀɢᴇ.
𝟸. Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ.
𝟹. Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs Hᴀᴠᴇ A Lɪᴍɪᴛ Oғ 𝟼𝟺 Cʜᴀʀᴀᴄᴛᴇʀs.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /filter - Aᴅᴅ A Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ
• /filters - Lɪsᴛ Aʟʟ Tʜᴇ Fɪʟᴛᴇʀs Oғ A Cʜᴀᴛ
• /del - Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ
• /delall - Dᴇʟᴇᴛᴇ Tʜᴇ Wʜᴏʟᴇ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ (Cʜᴀᴛ Oᴡɴᴇʀ Oɴʟʏ)

• /g_filter off Usᴇ Tʜɪs Cᴏᴍᴍᴏᴀɴᴅ + on/offғ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Tᴏ Cᴏɴᴛʀᴏʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ"""

    BUTTON_TXT = """<b>Hᴇʟᴘ Fᴏʀ Bᴜᴛᴛᴏɴs</b>

<i>Tʜɪs Bᴏᴛ Sᴜᴘᴘᴏʀᴛs Bᴏᴛʜ Uʀʟ Aɴᴅ Aʟᴇʀᴛ Iɴʟɪɴᴇ Bᴜᴛᴛᴏɴs.</i>

<b>Nᴏᴛᴇ:</b>
𝟷. Tᴇʟᴇɢʀᴀᴍ Wɪʟʟ Nᴏᴛ Aʟʟᴏᴡs Yᴏᴜ Tᴏ Sᴇɴᴅ Bᴜᴛᴛᴏɴs Wɪᴛʜᴏᴜᴛ Aɴʏ Cᴏɴᴛᴇɴᴛ, Sᴏ Cᴏɴᴛᴇɴᴛ Is Mᴀɴᴅᴀᴛᴏʀʏ.
𝟸. Tʜɪs Bᴏᴛ Sᴜᴘᴘᴏʀᴛs Bᴜᴛᴛᴏɴs Wɪᴛʜ Aɴʏ Tᴇʟᴇɢʀᴀᴍ Mᴇᴅɪᴀ Tʏᴘᴇ.
𝟹. Bᴜᴛᴛᴏɴs Sʜᴏᴜʟᴅ Bᴇ Pʀᴏᴘᴇʀʟʏ Pᴀʀsᴇᴅ As Mᴀʀᴋᴅᴏᴡɴ Fᴏʀᴍᴀᴛ

<b>Uʀʟ Bᴜᴛᴛᴏɴs:</b>
[Bᴜᴛᴛᴏɴ Tᴇxᴛ](buttonurl:xxxxxxxxxxxx)

<b>Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs:</b>
[Bᴜᴛᴛᴏɴ Tᴇxᴛ](buttonalert:Tʜɪs Is Aɴ Aʟᴇʀᴛ Mᴇssᴀɢᴇ)"""

    AUTOFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ AᴜᴛᴏFɪʟᴛᴇʀ</b>

<Ai>Aᴜᴛᴏ Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Tᴏ Fɪʟᴛᴇʀ & Sᴀᴠᴇ Tʜᴇ Fɪʟᴇs Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Fʀᴏᴍ Cᴜᴀɴɴᴇʟ Tᴏ Gʀᴏᴜᴘ. Yᴏᴜ Cᴀɴ Usᴇ Tʜᴇ Fᴏʟʟᴏᴡɪɴɢ Cᴏᴍᴍᴀɴᴅ Tᴏ ᴏɴ/ᴏғғ Tʜᴇ AᴜᴛᴏFɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ</i>

• /autofilter on - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴇɴᴀʙʟᴇ ɪɴ ʏᴏʀ ᴄʜᴀᴛ
• /autofilter off - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴅɪsᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ

<Ob>Oᴛʜᴇʀ Cᴏᴍᴍᴀɴᴅs:</b>
• /set_template - Sᴇᴛ Iᴍᴅʙ Tᴇᴍᴘʟᴀᴛᴇ Fᴏʀ Yᴏᴜʀ Gʀᴏᴜᴘ 
• /get_template - Gᴇᴛ Cᴜʀʀᴇɴᴛ Iᴍᴅʙ Tᴇᴍᴘʟᴀᴛᴇ Fᴏʀ Yᴏᴜʀ Gʀᴏᴜᴘ"""

    PROGRAMMER_TXT = """ ❃𓊈𒆜Oᴡɴᴇʀ Dᴇᴛᴀɪʟꜱ𒆜𓊉❃   
◈ ᴛɢ ɴᴀᴍᴇ : <a href=https://t.me/firossha>❃𓊈𒆜FIROS 𒆜𓊉❃</a>
◈ ɴɪᴄᴋɴᴀᴍᴇ : ™ᴩʀᴏɢʀᴀᴍᴍᴇʀ™
◈ ᴜꜱᴇʀɴᴀᴍᴇ : @firossha
◈ ʀᴇᴀʟɴᴀᴍᴇ : ғɪʀᴏs
‿︵‿︵‿︵‿୨❤୧‿︵‿︵‿︵‿ """

    CONNECTION_TXT = """<b>Hᴇʟᴘ Fᴏʀ Cᴏɴɴᴇᴄᴛɪᴏɴs</b>

<i> Usᴇᴅ Tᴏ Cᴏɴɴᴇᴄᴛ Bᴏᴛ Tᴏ Pᴍ Fᴏʀ Mᴀɴᴀɢɪɴɢ Fɪʟᴛᴇʀs. Iᴛ Hᴇʟᴘs Tᴏ Aᴠᴏɪᴅ Sᴘᴀᴍᴍɪɴɢ Iɴ Gʀᴏᴜᴘs</i>

<b>Nᴏᴛᴇ:</b>
• Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ A Cᴏɴɴᴇᴄᴛɪᴏɴ.
• Sᴇɴᴅ /connect Fᴏʀ Cᴏɴɴᴇᴄᴛɪɴɢ Mᴇ Tᴏ Uʀ Pᴍ

<Cb>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /connect - Cᴏɴɴᴇᴄᴛ A Pᴀʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ Tᴏ Yᴏᴜʀ Pᴍ
• /disconnect - Dɪsᴄᴏɴɴᴇᴄᴛ Fʀᴏᴍ A Cʜᴀᴛ
• /connections - Lɪsᴛ Aʟʟ Yᴏᴜʀ Cᴏɴɴᴇᴄᴛɪᴏɴs"""

    ADMIN_TXT = """<b>Hᴇʟᴩ Fᴏʀ Aᴅᴍɪɴꜱ</b>
    
<i>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</i>

<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ</b>
• /logs - Tᴏ Gᴇᴛ Tʜᴇ Rᴇᴄᴇɴᴛ Eʀʀᴏʀꜱ
• /delete - Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪꜰɪᴄ Fɪʟᴇ Fʀᴏᴍ DB
• /deleteall - Tᴏ Dᴇʟᴇᴛᴇ Aʟʟ Fɪʟᴇs Fʀᴏᴍ DB
• /users - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Uꜱᴇʀꜱ Aɴᴅ Iᴅꜱ
• /chats - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Cʜᴀᴛꜱ Aɴᴅ Iᴅꜱ
• /channel - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Tᴏᴛᴀʟ Cᴏɴɴᴇᴄᴛᴇᴅ Cʜᴀɴɴᴇʟꜱ
• /broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀꜱᴛ A Mᴇꜱꜱᴀɢᴇ Tᴏ Aʟʟ Uꜱᴇʀꜱ
• /group_broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ A Mᴇssᴀɢᴇ Tᴏ Aʟʟ Cᴏɴɴᴇᴄᴛᴇᴅ Gʀᴏᴜᴘs
• /leave  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Lᴇᴀᴠᴇ Fʀᴏᴍ A Cʜᴀᴛ
• /disable  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Dɪꜱᴀʙʟᴇ A Cʜᴀᴛ
• /invite - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Gᴇᴛ Tʜᴇ Iɴᴠɪᴛᴇ Lɪɴᴋ Oғ Aɴʏ Cʜᴀᴛ Wʜᴇʀᴇ Tʜᴇ Bᴏᴛ Is Aᴅᴍɪɴ
• /ban_user  - Wɪᴛʜ Iᴅ Tᴏ Bᴀɴ A Uꜱᴇʀ
• /unban_user  - Wɪᴛʜ Iᴅ Tᴏ Uɴʙᴀɴ A Uꜱᴇʀ
• /restart - Tᴏ Rᴇsᴛᴀʀᴛ Tʜᴇ Bᴏᴛ
• /clear_junk - Cʟᴇᴀʀ Aʟʟ Dᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ & Bʟᴏᴄᴋᴇᴅ Aᴄᴄᴏᴜɴᴛ Iɴ Dᴀᴛᴀʙᴀsᴇ
• /clear_junk_group - Cʟᴇᴀʀ Aᴅᴅ Rᴇᴍᴏᴠᴇᴅ Gʀᴏᴜᴘ Oʀ Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ Gʀᴏᴜᴘs Oɴ Dʙ"""


    STATUS_TXT = """<b>◉ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
◉ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>  
◉ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
◉ ᴜꜱᴇᴅ ᴅʙ ꜱɪᴢᴇ: <code>{}</code>
◉ ꜰᴇᴇᴇ ᴅʙ ꜱɪᴢᴇ: <code>{}</code></b>"""

    ST_TXT ="""/stickerid ʀᴇᴩʟᴀʏ ᴛᴏ ᴀɴʏ ꜱᴛɪᴄᴋᴇʀ ᴏʀ ᴍᴇᴅɪᴀ ᴛᴏ ɢᴇᴛ ɪᴅ"""

    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

◉ ɢʀᴏᴜᴩ: {a}
◉ ɢ-ɪᴅ: <code>{b}</code>
◉ ʟɪɴᴋ: @{c}
◉ ᴍᴇᴍʙᴇʀꜱ: <code>{d}</code>
◉ ᴀᴅᴅᴇᴅ ʙʏ: {e}

◉ ʙʏ: @{f}</b>"""

    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ
    
◉ ᴜꜱᴇʀ-ɪᴅ: <code>{}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {}
◉ ᴜꜱᴇʀɴᴀᴍᴇ: @{}

◉ ʙʏ: @{}</b>"""

    GROUPMANAGER_TXT = """<b>Hᴇʟᴩ Fᴏʀ GʀᴏᴜᴩMᴀɴᴀɢᴇʀ</b>

<i>Tʜɪꜱ Iꜱ Hᴇʟᴩ Oꜰ Yᴏᴜʀ Gʀᴏᴜᴩ Mᴀɴᴀɢɪɴɢ. Tʜɪꜱ Wɪʟʟ Wᴏʀᴋ Oɴʟʏ Fᴏʀ Gʀᴏᴜᴩ aᴅᴍɪɴꜱ</i>"""

    KICK_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /inkick - Cᴏᴍᴍᴀɴᴅ Wɪᴛʜ Rᴇǫᴜɪʀᴇᴅ Aʀɢᴜᴍᴇɴᴛs Aɴᴅ I Wɪʟʟ Kɪᴄᴋ Mᴇᴍʙᴇʀs Fʀᴏᴍ Gʀᴏᴜᴘ."""

    STATUS2_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /instatus - Tᴏ Cʜᴇᴄᴋ Cᴜʀʀᴇɴᴛ Sᴛᴀᴛᴜs Oғ Cʜᴀᴛ Mᴇᴍʙᴇʀ Fʀᴏᴍ Gʀᴏᴜᴘ."""

    DKICK_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /dkick - Tᴏ Kɪᴄᴋ Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛs"""

    BAN_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /ban - To Bᴀɴ A Uꜱᴇʀ Fᴏʀᴍ Tʜᴇ Gʀᴏᴜᴩ"""

    UNBAN_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /unban - Uɴʙᴀɴ Tʜᴇ Bᴀɴɴᴇᴅ Uꜱᴇʀ"""

    TBAN_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /tban - Tᴇᴍᴩᴏʀᴀʀʏ Bᴀɴ A Uꜱᴇʀ"""

    MUTE_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /mute - To Mᴜᴛᴇ A Uꜱᴇʀ"""

    UNMUTE_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /unmute - To Uɴᴍᴜᴛᴇ Tʜᴇ Mᴜᴛᴇᴅ Uꜱᴇʀ"""

    TMUTE_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /tmute - Wɪᴛʜ Vᴀʟᴜᴇ To Mᴜᴛᴇ Uᴩ To Pᴀʀᴛɪᴄᴜʟᴀʀ Tɪᴍᴇ Eɢ: <code>/tmute 2h</code> To Mᴜᴛᴇ 2Hᴏᴜʀ Vᴀʟᴜᴇꜱ Iꜱ (m/h/d)"""

    PIN_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /pin - Tᴏ Pɪɴ A Mᴇꜱꜱᴀɢᴇ Oɴ Yᴏᴜʀ Cʜᴀᴛ"""

    UNPIN_TXT="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /unpin - Tᴏ Uɴᴩɪɴ Tʜᴇ Mᴇꜱꜱᴀɢᴇ Oɴ Yᴏᴜʀ Cʜᴀᴛ"""

    PURGE_TXT ="""
<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /purge - Dᴇʟᴇᴛᴇ Aʟʟ Mᴇssᴀɢᴇs Fʀᴏᴍ Tʜᴇ Rᴇᴘʟɪᴇᴅ Tᴏ Mᴇssᴀɢᴇ, Tᴏ Tʜᴇ Cᴜʀʀᴇɴᴛ Mᴇssᴀɢᴇ """
    EXTRAMOD2_TXT = """<b>Hᴇʟᴩ Fᴏʀ Exᴛʀᴀ Mᴏᴅᴜʟᴇ</b>

<i>Jᴜꜱᴛ Sᴇɴᴅ Aɴʏ Iᴍᴀɢᴇ Tᴏ Eᴅɪᴛ Iᴍᴀɢᴇ ✨</i>"""

    EXTRAMOD_TXT = """<b>Hᴇʟᴩ Fᴏʀ Exᴛʀᴀ Mᴏᴅᴜʟᴇ</b>

<i>Jᴜꜱᴛ Sᴇɴᴅ Aɴʏ Iᴍᴀɢᴇ Tᴏ Eᴅɪᴛ Iᴍᴀɢᴇ ✨</i>"""

    ID_TXT = """<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /id - Gᴇᴛ Iᴅ Oғ A Sᴘᴇᴄɪғᴇᴅ Usᴇʀ"""

    INFO_TXT = """<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /info  - Gᴇᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴ Aʙᴏᴜᴛ A Usᴇʀ"""

    IMDB_TXT ="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /imdb  - Gᴇᴛ Tʜᴇ Fɪʟᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ Fʀᴏᴍ Iᴍᴅʙ Sᴏᴜʀᴄᴇ"""

    PASTE_TXT ="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /paste [ᴛᴇxᴛ] - Pᴀsᴛᴇ Tʜᴇ Gɪᴠᴇɴ Tᴇxᴛ Oɴ Pᴀsᴛʏ"""
    TTS_TXT ="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /tts [ᴛᴇxᴛ] - Cᴏɴᴠᴇʀᴛ Tᴇxᴛ Tᴏ Sᴘᴇᴇᴄʜ"""
    TELEGRAPH_TXT ="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /telegraph - Sᴇɴᴅ Mᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Rᴇᴘʟʏ Wɪᴛʜ Pɪᴄᴛᴜʀᴇ Oʀ Vɪᴅᴇ Uɴᴅᴇʀ (𝟻ᴍʙ)"""

    JSON_TXT ="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /json - Rᴇᴩʟʏ Wɪᴛʜ Aɴʏ Mᴇꜱꜱᴀɢᴇ Tᴏ Gᴇᴛ Mᴇꜱꜱᴀɢᴇ Iɴꜰᴏ (ᴜꜱᴇꜰᴜʟʟ ꜰᴏʀ ɢʀᴏᴜᴩ)"""

    WRITTEN_TXT ="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /written - Rᴇᴩʟʏ Wɪᴛʜ Tᴇxᴛ Tᴏ Gᴇᴛ Fɪʟᴇ (ᴜꜱᴇꜰᴜʟʟ ꜰᴏʀ ᴄᴏᴅᴇʀꜱ)"""
    CARBON_TXT ="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /carbon - Rᴇᴘʟʏ Wɪᴛʜ Tᴇxᴛ Tᴏ Gᴇᴛ Cᴀʀʙᴏɴᴀᴛᴇᴅ Iᴍᴀɢᴇ"""
    FONT_TXT ="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /font [ᴛᴇxᴛ] - Tᴏ Cʜᴀɴɢᴇ Yᴏᴜʀ Tᴇxᴛ Fᴏɴᴛs Tᴏ Fᴀɴᴄʏ Fᴏɴᴛ"""
    SHARE_TXT ="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /share - Rᴇᴘʟʏ Wɪᴛʜ Tᴇxᴛ Tᴏ Gᴇᴛ Tᴇxᴛ Sʜᴀʀᴀʙʟᴇ Lɪɴᴋ"""
    YOUTUBE_TXT ="""<b>ʏᴏᴜᴛᴜʙᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ</b>
•ᴛʜɪꜱ ᴡɪʟʟ ʜᴇʟᴩ ʏᴏᴜ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏꜱ ᴀɴᴅ ꜱᴏɴɢꜱ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ ᴅɪʀᴇᴄᴛʟʏ"""
    SONG_TXT ="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /song [ɴᴀᴍᴇ] / [ᴜʀʟ] - ᴛᴏ ꜱᴇᴀʀᴄʜ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ʏᴏᴜᴛᴜʙᴇ ꜱᴏɴɢ.
•ɪ ʀᴇᴄᴏᴍᴍᴇɴᴅ ʏᴏᴜ ᴛᴏ ᴜꜱᴇ ᴛʜᴇ ᴜʀʟ ɪɴꜱᴛᴇᴅ ᴏꜰ ɴᴀᴍᴇ
•ɪꜰ ʏᴏᴜ ᴜꜱᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴛʜᴇ ᴩʀᴏᴄᴇꜱꜱ ᴡɪʟʟ ʙᴇ ᴠᴇʀʀʏ ꜱʟᴏᴡ"""
    VIDEO_TXT="""<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /video [ɴᴀᴍᴇ] / [ᴜʀʟ] - ᴛᴏ ꜱᴇᴀʀᴄʜ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ.
•ɪ ʀᴇᴄᴏᴍᴍᴇɴᴅ ʏᴏᴜ ᴛᴏ ᴜꜱᴇ ᴛʜᴇ ᴜʀʟ ɪɴꜱᴛᴇᴅ ᴏꜰ ɴᴀᴍᴇ
•ɪꜰ ʏᴏᴜ ᴜꜱᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴛʜᴇ ᴩʀᴏᴄᴇꜱꜱ ᴡɪʟʟ ʙᴇ ᴠᴇʀʀʏ ꜱʟᴏᴡ"""

    CREATOR_REQUIRED = "❗<b>Yᴏᴜ Hᴀᴠᴇ To Bᴇ Tʜᴇ Gʀᴏᴜᴩ Cʀᴇᴀᴛᴏʀ Tᴏ Dᴏ Tʜᴀᴛ</b>"

    FUN_TXT = "ꜱᴏᴍᴇ ꜰᴜɴ ᴇʟᴇᴍᴇɴᴛꜱ ᴀʀᴇ ʜᴇʀᴇ"

    DISE_TXT = "/dise - ᴜꜱɪɴɢ ᴛʜɪꜱ ʏᴏᴜ ᴄᴀɴ ʀᴏʟʟ ᴛʜᴇ ᴅɪꜱᴇ ᴡɪᴛʜᴏᴜᴛ ᴅɪꜱᴇ"

    TOSS_TXT = "/toss - ᴜꜱɪɴɢ ᴛʜɪꜱ ʏᴏᴜ ᴄᴀɴ ᴛᴏꜱꜱ ᴀ ᴄᴏɪ  ᴡɪᴛʜᴏᴜᴛ ᴄᴏɪɴ"

    INPUT_REQUIRED = "❗ **Aʀɢᴜᴍᴇɴ Rqᴜɪʀᴇᴅ**"

    KICKED = "✔️ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Kɪᴄᴋᴇᴅ {} Mᴇᴍʙᴇʀꜱ Acᴄᴏʀᴅɪɴɢ To Tʜᴇ Aʀɢᴜᴍᴇɴᴛꜱ Prᴏᴠɪᴅᴇᴅ"

    START_KICK = "Rᴇᴍᴏᴠɪɴɢ Iɴᴀᴄᴛɪᴠᴇ Mᴇᴍʙᴇʀs Tʜɪs Mᴀʏ Tᴀᴋᴇ A Wʜɪʟᴇ"

    ADMIN_REQUIRED = "❗<b>Iᴀᴍ Nᴏᴛ Aᴅᴍɪɴ Iɴ Tʜɪꜱ Cʜᴀᴛ Sᴏ Pʟᴇᴀꜱᴇ Aᴅᴅ Mᴇ Aɢᴀɪɴ Wɪᴛʜ Aʟʟ Pᴅᴍɪɴ Pᴇʀᴍɪꜱꜱɪᴏɴ</b>"

    DKICK = "✔️ Kɪᴄᴋᴇᴅ {} Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛꜱ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ"

    FETCHING_INFO = "<b>Wᴀɪᴛ I Wɪʟʟ Tᴀᴋᴇ Tʜᴇ Aʟʟ Iɴꜰᴏ</b>"

    SERVER_STATS = """Sᴇʀᴠᴇʀ Sᴛᴀᴛꜱ:
 
Uᴩᴛɪᴍᴇ: {}
CPU Uꜱᴀɢᴇ: {}%
RAM Uꜱᴀɢᴇ: {}%
Tᴏᴛᴀʟ Dɪꜱᴋ: {}
Uꜱᴇᴅ Dɪꜱᴋ: {} ({}%)
Fʀᴇᴇ Dɪꜱᴋ: {}"""

    BUTTON_LOCK_TEXT = "Hᴇʏ {query}\nTʜɪꜱ Iꜱ Nᴏᴛ Fᴏʀ Yᴏᴜ. Sᴇᴀʀᴄʜ Yᴏᴜʀ Sᴇʟꜰ"

    FORCE_SUB_TEXT = "Sᴏʀʀʏ Bʀᴏ Yᴏᴜʀ Nᴏᴛ Jᴏɪɴᴇᴅ Mʏ Cʜᴀɴɴᴇʟ Sᴏ Pʟᴇᴀsᴇ Cʟɪᴄᴋ Jᴏɪɴ Bᴜᴛᴛᴏɴ Tᴏ Jᴏɪɴ Mʏ Cʜᴀɴɴᴇʟ Aɴᴅ Tʀʏ Aɢᴀɪɴ"

    WELCOM_TEXT = """Hᴇʏ {user} 💞

Wᴇʟᴄᴏᴍᴇ ᴛᴏ {chat}.

ꜱʜᴀʀᴇ & ꜱᴜᴩᴩᴏʀᴛ, ʀᴇqᴜᴇꜱᴛ ʏᴏᴜ ᴡᴀɴᴛᴇᴅ ᴍᴏᴠɪᴇꜱ"""

    IMDB_TEMPLATE = """<b>Qᴜᴇʀʏ: {query}</b>

🏷 Tɪᴛʟᴇ: <a href={url}>{title}</a>
🎭 Gᴇɴʀᴇꜱ: {genres}
📆 Yᴇᴀʀ: <a href={url}/releaseinfo>{year}</a>
🌟 Rᴀᴛɪɴɢ: <a href={url}/ratings>{rating}</a>/10"""


    YTT_TXT ="""/ytthumb - ᴜꜱɪɴɢ ᴛʜɪꜱ ʏᴏᴜ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ.
\n♻️  𝗘𝘅𝗮𝗺𝗽𝗹𝗲:

/ytthumb https://youtu.be/6A49rH9grzk"""

    COUNTRY_TXT="""/country - ᴜꜱɪɴɢ ᴛʜɪꜱ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴛʜᴇ ɢᴇɴᴇʀᴀʟ ᴅᴇᴛᴀɪʟꜱ ᴏꜰ ᴀ ᴄᴏᴜɴᴛʀʏ
\n♻️  𝗘𝘅𝗮𝗺𝗽𝗹𝗲:

/country India"""

    TRANS_TXT="""𝙶𝙾𝙶𝙶𝙻𝙴 𝚃𝚁𝙰𝙽𝚂𝙻𝙰𝚃𝙴𝚁

𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝙲𝙾𝙽𝚅𝙴𝚁𝚃 𝚃𝙴𝚇𝚃 𝚃𝙾 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴.

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝:

Reply any text with /tr

➤ 𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    PASSWD_TXT="""/genpassword - ᴜꜱɪɴɢ ᴛʜɪꜱ ʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ʀᴀɴᴅᴏᴍ ᴩᴀꜱꜱᴡᴏʀᴅꜱ"""





