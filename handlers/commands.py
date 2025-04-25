from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Send me a PDF, and I will extract the major headings from each page!\n\nCommands: \n/todayMint\n/todayHindu'
    )
