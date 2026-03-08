import uuid
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from services.media_service import detect_platform
PLATFORM_ICONS = {
    "youtube": "▶️ YouTube",
    "tiktok": "🎵 TikTok",
    "instagram": "📸 Instagram",
    "facebook": "📘 Facebook",
}


async def url_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.strip()
    platform = detect_platform(text)

    if not platform:
        await update.message.reply_text(
            "Unsupported URL.\n\n"
            "I support links from:\n"
            "• ▶️ YouTube\n"
            "• 🎵 TikTok\n"
            "• 📸 Instagram\n"
            "• 📘 Facebook"
        )
        return

    url_id = str(uuid.uuid4())[:8]
    context.user_data[url_id] = text

    platform_label = PLATFORM_ICONS[platform]

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎵 Audio (MP3)", callback_data=f"audio:{url_id}"),
            InlineKeyboardButton("🎬 Video (MP4)", callback_data=f"video:{url_id}"),
        ],
        [
            InlineKeyboardButton("🎬 360p", callback_data=f"q:360:{url_id}"),
            InlineKeyboardButton("🎬 720p", callback_data=f"q:720:{url_id}"),
            InlineKeyboardButton("🎬 1080p", callback_data=f"q:1080:{url_id}"),
        ],
        [InlineKeyboardButton("Cancel", callback_data="cancel")]
    ])

    await update.message.reply_text(
        f"*{platform_label} link detected!*\n\nWhat would you like to download?",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "end me a link from YouTube, TikTok, Instagram or Facebook.\n"
        "Type /help to see all commands."
    )