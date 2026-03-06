from telegram.ext import CommandHandler, ApplicationBuilder, CallbackQueryHandler
from handlers.callbacks import format_choice_callback, quality_choice_callback, cancel_callback
import logging
from handlers.download import conv_handler
from handlers.start import start_handler 
from config import Settings

settings = Settings()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )

def main():
    app = ApplicationBuilder().token(settings.TOKEN).build()
    app.add_handler(CommandHandler('start', start_handler))
    app.add_handler(CallbackQueryHandler(format_choice_callback, pattern="^audio:|^video:"))
    app.add_handler(CallbackQueryHandler(quality_choice_callback, pattern="^quality:"))
    app.add_handler(CallbackQueryHandler(cancel_callback, pattern="^cancel$"))

    app.run_polling()

if __name__ == '__main__':    main()