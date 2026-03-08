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
            "❌ Unsupported URL.\n\n"
            "I support links from:\n"
            "• ▶️ YouTube\n"
            "• 🎵 TikTok\n"
            "• 📸 Instagram\n"
            "• 📘 Facebook"
        )
        return

    platform_label = PLATFORM_ICONS[platform]

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎵 Audio (MP3)", callback_data=f"audio:{text}"),
            InlineKeyboardButton("🎬 Video (MP4)", callback_data=f"video:{text}"),
        ],
        [
            InlineKeyboardButton("🎬 360p", callback_data=f"quality:360:{text}"),
            InlineKeyboardButton("🎬 720p", callback_data=f"quality:720:{text}"),
            InlineKeyboardButton("🎬 1080p", callback_data=f"quality:1080:{text}"),
        ],
        [InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
    ])

    await update.message.reply_text(
        f"*{platform_label} link detected\!*\n\nWhat would you like to download?",
        reply_markup=keyboard,
        parse_mode="MarkdownV2"
    )


async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "❓ Send me a link from YouTube, TikTok, Instagram or Facebook.\n"
        "Type /help to see all commands."
    )