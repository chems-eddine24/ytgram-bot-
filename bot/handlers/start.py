from telegram import Update
from telegram.ext import ContextTypes

START_TEXT = """
*Welcome to YTGram Bot*

I can download YouTube videos and audio directly to your Telegram chat\.

* What I can do:*
`/audio <url>` Download as MP3
`/video <url>` Download as MP4
`/start` — Show this menu
`/help` — How to use the bot

*⚡ Quick example:*
`/audio https://youtube.com/watch?v=...`

Paste any YouTube URL and I'll handle the rest\.
"""


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    await update.message.reply_text(
        f"*Welcome, {user.first_name}\!*\n" + START_TEXT,
        parse_mode="MarkdownV2"
    )