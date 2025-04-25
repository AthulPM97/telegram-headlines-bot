from telegram import Update
from telegram.ext import ContextTypes
from db.mongo_handler import mongo_handler
from utils import json_to_response
from datetime import datetime


async def today_hindu(update: Update,
                      context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        entries = mongo_handler.get_today_hindu_entries()

        # Get today's date in dd-mm-yyyy format
        today_date = datetime.now().strftime("%d-%m-%Y")

        if not entries:
            await update.message.reply_text(
                f"No Hindu/TH files found for {today_date}.")
            return

        # future concern: if multiple hindu editions have been uploaded to db for same date then formatting won't be proper

        for entry in entries:
            articles = entry['articles']
            response_chunks = json_to_response(articles)
            for chunk in response_chunks:
                await update.message.reply_text(chunk)

    except Exception as e:
        await update.message.reply_text(f"🚨 Error fetching data: {str(e)}")
