from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start, handle_pdf, handle_headings_json  # Cleaner import
# from handlers.pdf import handle_pdf
from dotenv import load_dotenv
import os

load_dotenv()


def main() -> None:
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))
    app.add_handler(
        MessageHandler(filters.Document.MimeType("application/json"),
                       handle_headings_json))

    app.run_polling()


if __name__ == "__main__":
    main()
