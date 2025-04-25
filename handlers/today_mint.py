from telegram import Update
from telegram.ext import ContextTypes
from db.mongo_handler import mongo_handler
from utils import json_to_response
from datetime import datetime


async def today_mint(update: Update,
                     context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        entries = mongo_handler.get_today_mint_entries()

        if not entries:
            await update.message.reply_text("No 'mint' files found for today.")
            return

        # Get today's date in dd-mm-yyyy format
        today_date = datetime.now().strftime("%d-%m-%Y")

        response = f"Today's Mint ({today_date}):\n\n"
        for idx, entry in enumerate(entries):
            articles = entry['articles']
            response_text = json_to_response(articles)
            response += response_text

        await update.message.reply_text(response)

    except Exception as e:
        await update.message.reply_text(f"🚨 Error fetching data: {str(e)}")
