from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


def _is_youtube_url(text: str) -> bool:
    return any(domain in text for domain in ["youtube.com/watch", "youtu.be/", "youtube.com/shorts/"])


async def url_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.strip()

    if not _is_youtube_url(text):
        await update.message.reply_text("Please send a valid YouTube URL.")
        return

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎵 MP3 Audio", callback_data=f"audio:{text}"),
            InlineKeyboardButton("🎬 MP4 Video", callback_data=f"video:{text}"),
        ],
        [InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
    ])

    await update.message.reply_text("What format do you want?", reply_markup=keyboard)
