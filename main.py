from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start, handle_pdf, handle_headings_json, today_mint
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")


def main() -> None:
    print("I'm alive!")
    app = ApplicationBuilder().token(bot_token).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))
    app.add_handler(
        MessageHandler(filters.Document.MimeType("application/json"),
                       handle_headings_json))
    app.add_handler(CommandHandler("todayMint", today_mint))

    app.run_polling()


if __name__ == "__main__":
    main()
