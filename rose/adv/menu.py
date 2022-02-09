from rose import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

supunma = """
👨‍🔧 **ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴇɴᴜ**

<b>ᴀᴅᴠᴀɴᴄᴇᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ ꜰʀᴏᴍ ᴀᴛᴛᴀᴄᴋᴇʀꜱ ᴀɴᴅ ᴅᴏ ᴍᴀɴʏ ꜱᴛᴜꜰꜰ ɪɴ ɢʀᴏᴜᴘ ꜰʀᴏᴍ ᴀ ꜱɪɴɢʟᴇ ʙᴏᴛ.ʏᴏᴜ ᴄᴀɴ ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ, ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴀ ʙᴜᴛᴛᴏɴ.</b>💡

[ᴀʟ ᴋᴜᴘᴘɪʏᴀ ɢʀᴏᴜᴘ](https://t.me/apealkuppiya).💡
[ᴀʟ ᴋᴜᴘᴘɪʏᴀ ᴄʜᴀɴɴᴇʟ](https://t.me/alevelkuppiya1)🐣

[ᴄʟɪᴄᴋ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ](https://t.me/szteambots/872)
"""

mbuttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton
                (
                    "CAPTCHA🥷🏻", callback_data="_cap"
                ),            
            InlineKeyboardButton
                (
                    "Logo-Tools🖼", callback_data="_logo"
                )
        ],
        [
            InlineKeyboardButton
                (
                    "VC-Player", callback_data="_vc"
                ),            
            InlineKeyboardButton
                (
                    "Telegram", callback_data="_telegram"
                ),  
        ],       
        [
            InlineKeyboardButton
                (
                    "🔙Back", callback_data="bot_commands"
                )
        ]
    ]
)
    

@app.on_callback_query(filters.regex("adv_menu"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunma,
        reply_markup=mbuttons,
        disable_web_page_preview=True,    
    )
    await CallbackQuery.message.delete()
