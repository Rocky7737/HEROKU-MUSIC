from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from Process.filters import other_filters2
from time import time
from Process.filters import command
from datetime import datetime
from Process.decorators import authorized_users_only


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐚𝐦 𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲
𝐍𝐨 𝐋𝐚𝐠 𝐕𝐂 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐁𝐨𝐭.

┏━━━━━━━━━━━━━━━━━━━┓
┣★ 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 : @Rocky8904 
┣★ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 » : @rockyrishi
┣★ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 » : @rocky9042
┗━━━━━━━━━━━━━━━━━━━┛

💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝
𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐌𝐮𝐬𝐢𝐜.
━━━━━━━━━━━━━━━━━━━━━━━━
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "🌷𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯🌷", url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    ),
                ],
                [
                    InlineKeyboardButton(
                       "🍒𝐉𝐨𝐢𝐧 𝐁𝐚𝐛𝐲🥀", url=f"https://t.me/rockyrishi"
                    ),
                    InlineKeyboardButton(
                       "😇𝐂𝐨𝐦𝐞 𝐇𝐞𝐫𝐞⛦⃕‌🇮🇳", url=f"https://t.me/rocky9042"
                    )
                ],[
                    InlineKeyboardButton(
                        "★ 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 ★",
                        url=f"https://t.me/Rocky8904",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/53299d9b822f47eff93f4.jpg",
        caption=f"""🍒𝐇𝐞𝐫𝐞 𝐈𝐬 𝐓𝐡𝐞 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 𝐅𝐨𝐫𝐤 𝐀𝐧𝐝 𝐆𝐢𝐯𝐞 𝐒𝐭𝐚𝐫𝐬✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹𝐇𝐄𝐑𝐎𝐊𝐔 𝐌𝐔𝐒𝐈𝐂🌹", url=f"https://github.com/THE-VIP-BOY-OP/HEROKU-MUSIC")
                ]
            ]
        ),
    )
