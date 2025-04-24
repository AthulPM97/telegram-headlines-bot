from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers.commands import start
# from handlers.pdf import handle_pdf
from dotenv import load_dotenv
import os

load_dotenv()


def main() -> None:
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    # app.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))

    app.run_polling()


if __name__ == "__main__":
    main()
