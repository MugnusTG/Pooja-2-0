class script(object):
    START_TXT = """𝐻𝑒𝑙𝑙𝑜 {},
𝐻𝑜𝑤 𝐴𝑟𝑒 𝑌𝑜𝑢 𝐷𝑢𝑑𝑒 🤩 𝑁𝑖𝑐𝑒 𝑇𝑜
𝑀𝑒𝑒𝑡 𝑌𝑜𝑢 ☺️ 𝐼 𝑎𝑚 𝐽𝑢𝑠𝑡 𝐴 𝑆𝑖𝑚𝑝𝑙𝑒 𝑃𝑟𝑒 𝐹𝑢𝑛𝑐𝑡𝑖𝑜𝑛𝑒𝑑 𝐴𝑢𝑡𝑜𝐹𝑖𝑙𝑡𝑒𝑟𝐵𝑜𝑡
𝑌𝑜𝑢 𝑐𝑎𝑛 𝑎𝑑𝑑 𝑡𝑜 𝑚𝑒 𝑦𝑜𝑢 𝑔𝑟𝑜𝑢𝑝☺️

©𝑀𝑎𝑖𝑛𝑡𝑎𝑖𝑛𝑒𝑑 𝑏𝑦: <a href=https://t.me/MagnusTG>𝑴agnus TG 🇮🇳</a>"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
➪ 𝑪𝒓𝒆𝒂𝒕𝒐𝒓 : <a href=https://t.me/MagnusTG>𝑴agnus TG 🇮🇳</a>
➪ 𝑳𝒊𝒃𝒓𝒂𝒓𝒚 : <a href=https://docs.pyrogram.org/>𝑷𝚈𝚁𝙾𝙶𝚁𝙰𝙼 📜</a>
➪ 𝑺𝒐𝒖𝒓𝒄𝒆 𝑪𝒐𝒅𝒆 : <a href=https://t.me/hagayhwvwhtf> 𝑪𝙻𝙸𝙲𝙺 𝑯𝙴𝚁𝙴</a>
➪ 𝑪𝒓𝒆𝒅𝒊𝒕𝒔 : 𝙴𝚟𝚎𝚛𝚢𝚘𝚗𝚎 𝚒𝚗 𝚝𝚑𝚒𝚜 𝚓𝚘𝚞𝚛𝚗𝚎𝚢
➪ 𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆 : 𝑷𝚈𝚃𝙷𝙾𝙽 𝟹
➪ 𝑫𝒂𝒕𝒂 𝒃𝒂𝒔𝒆 : <a href=https://www.mongodb.com>𝑴𝙾𝙽𝙶𝙾 𝙳𝙱</a>
➪ 𝑩𝒐𝒕 𝒔𝒆𝒓𝒗𝒆𝒓 : <a href=https://dashboard.heroku.com/>𝑯𝙴𝚁𝙾𝙺𝚄</a>
➪ 𝑩𝒖𝒊𝒍𝒅 𝑺𝒕𝒂𝒕𝒖𝒔 : <code> v2.0.1 [ 𝙱𝙴𝚃𝙰 ] </code>

🔖 𝑸𝒖𝒐𝒕𝒆: ആരും പേടിക്കേണ്ട എല്ലാവർക്കും കിട്ടും"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://t.me/MyGithubSorceCode 

<b>DEVS:</b>
- <a href=https://t.me/MagnusTG>Magnus TG 🇮🇳</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /telegraph - <code>photo to link</code>"""
    TELEGRAPH_TXT = """Help: <b>Telegraph mods</b>    
    
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
