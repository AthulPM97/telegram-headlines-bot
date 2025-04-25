from telegram import Update
from telegram.ext import ContextTypes
import json
from utils import json_to_response


async def handle_headings_json(update: Update,
                               context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.document and update.message.document.mime_type == 'application/json':
        try:
            # Download JSON file
            json_file = await update.message.document.get_file()
            json_bytes = await json_file.download_as_bytearray()

            # Parse JSON
            headings_data = json.loads(json_bytes.decode('utf-8'))

            response_text = json_to_response(headings_data)

            await update.message.reply_text(response_text)

        except json.JSONDecodeError:
            await update.message.reply_text(
                "Invalid JSON format! Please send a valid headings JSON file.")
        except Exception as e:
            await update.message.reply_text(f"Error processing file: {str(e)}")
    else:
        await update.message.reply_text(
            "Please send a JSON file with headings data.")
