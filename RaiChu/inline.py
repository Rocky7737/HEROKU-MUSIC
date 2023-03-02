
from pyrogram import Client, errors
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from youtubesearchpython import VideosSearch
from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)

def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0

def audio_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="• Iɴʟɪɴᴇ", switch_inline_query_current_chat=""),
    ],
    [
      InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data=f'cls'),
    ],
  ]
  return buttons

def stream_markup(user_id, dlurl):
  buttons = [
    [
      InlineKeyboardButton(text="🇮🇳 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 🇮🇳", url=f"https://t.me/ROCKY_MUSIC_BOT?startgroup=true")
    ],
    [
      InlineKeyboardButton(text="II", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▷", callback_data=f'cbresume | {user_id}'),
      InlineKeyboardButton(text="‣‣I", callback_data=f'cbskip | {user_id}'),
      InlineKeyboardButton(text="▢", callback_data=f'cbstop | {user_id}')
    ],
    [
      InlineKeyboardButton(text="🌷𝐉𝐨𝐢𝐧 𝐏𝐥𝐬🍒", url=f"https://t.me/rockyrishi"),
      InlineKeyboardButton(text="🍒𝐂𝐨𝐦𝐞 𝐁𝐚𝐛𝐲😘", url=f"https://t.me/rocky9042")
    ],
    [
      InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data=f'cls'),
    ],
  ]
  return buttons

def menu_markup(user_id):
  buttons = [
     [
      InlineKeyboardButton(text="🇮🇳 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 🇮🇳", url=f"https://t.me/ROCKY_MUSIC_BOT?startgroup=true")
    ],
     [InlineKeyboardButton(text="II", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▷", callback_data=f'cbresume | {user_id}')],
     [InlineKeyboardButton(text="‣‣I", callback_data=f'cbskip | {user_id}'),
      InlineKeyboardButton(text="▢", callback_data=f'cbstop | {user_id}')
    ],
     [InlineKeyboardButton(text="🔇", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="💞𝐂𝐨𝐦𝐞 𝐁𝐚𝐛𝐲💞", url=f"https://t.me/rocky9042"),
      InlineKeyboardButton(text="🔊", callback_data=f'cbunmute | {user_id}')],
  ]
  return buttons

def song_download_markup(videoid):
    buttons = [
        [
      InlineKeyboardButton(text="🇮🇳 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 🇮🇳", url=f"https://t.me/ROCKY_MUSIC_BOT?startgroup=true")
    ],
        [
            InlineKeyboardButton(
                text="⬇️ ᴀᴜᴅɪᴏ",
                callback_data=f"gets audio|{videoid}",
            ),
            InlineKeyboardButton(
                text="⬇️ ᴠɪᴅᴇᴏ",
                callback_data=f"gets video|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴀᴄᴋ",
                callback_data="cbhome",
            )
        ],
    ]
    return buttons

close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "• ᴄʟᴏsᴇ •", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "• ʙᴀᴄᴋ •", callback_data="cbmenu"
      )
    ]
  ]
)
