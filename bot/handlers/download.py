
import asyncio
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes
from services.youtube_service.yt_download import download_youtube_audio
waiting_for_link = 1
async def audio_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send Me The Link")
    return waiting_for_link

async def receive_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if url[0:17] != "https://youtu.be/":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid Youtube Url. Try again...")

    await update.message.reply_text("Downloading...")
    loop = asyncio.get_running_loop()
    audio_path = await loop.run_in_executor(None, download_youtube_audio, url)

    with open(audio_path, "rb") as audio:
        await context.bot.send_audio(update.effective_chat.id, audio)
    return ConversationHandler.END

conv_handler = ConversationHandler(
        entry_points=[CommandHandler("audio", audio_download)],
        states={
            waiting_for_link: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, receive_link)
            ],
        },
        fallbacks=[],
    )

