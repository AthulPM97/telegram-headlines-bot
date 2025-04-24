from telegram import Update
from telegram.ext import ContextTypes
import json


async def handle_headings_json(update: Update,
                               context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.document and update.message.document.mime_type == 'application/json':
        try:
            # Download JSON file
            json_file = await update.message.document.get_file()
            json_bytes = await json_file.download_as_bytearray()

            # Parse JSON
            headings_data = json.loads(json_bytes.decode('utf-8'))

            # Format response
            response_text = ""
            for page_num, headings in headings_data.items():
                if headings:
                    response_text += f"\n=== Page {int(page_num) + 1} ===\n"
                    for i, heading in enumerate(headings, start=1):
                        response_text += f"{i}. {heading}\n"
                else:
                    response_text += f"\n=== Page {int(page_num) + 1} === (No headings found)\n"

            await update.message.reply_text(response_text)

        except json.JSONDecodeError:
            await update.message.reply_text(
                "Invalid JSON format! Please send a valid headings JSON file.")
        except Exception as e:
            await update.message.reply_text(f"Error processing file: {str(e)}")
    else:
        await update.message.reply_text(
            "Please send a JSON file with headings data.")
