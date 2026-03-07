from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import re

YOUTUBE_REGEX = re.compile(
    r"(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)[\w\-]+"
)


async def url_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    if not YOUTUBE_REGEX.match(text):
        await update.message.reply_text(
            "❌ That doesn't look like a valid YouTube URL.\nSend me a YouTube link to get started."
        )
        return

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎵 MP3 Audio", callback_data=f"audio:{text}"),
            InlineKeyboardButton("🎬 MP4 Video", callback_data=f"video:{text}"),
        ],
        [
            InlineKeyboardButton("🎬 360p", callback_data=f"quality:360:{text}"),
            InlineKeyboardButton("🎬 720p", callback_data=f"quality:720:{text}"),
            InlineKeyboardButton("🎬 1080p", callback_data=f"quality:1080:{text}"),
        ],
        [InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
    ])

    await update.message.reply_text(
        "🎯 *What format do you want?*",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "❓ I only understand YouTube URLs and commands.\nType /help to see what I can do."
    )
