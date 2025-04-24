from telegram import Update
from telegram.ext import ContextTypes
from utils import extract_headings


async def handle_pdf(update: Update,
                     context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.document and update.message.document.mime_type == 'application/pdf':
        file = await context.bot.get_file(update.message.document.file_id)
        pdf_bytes = await file.download_as_bytearray()

        headings = await extract_headings(pdf_bytes)

        response_text = ""

        for page_num, headings in headings.items():
            if headings:  # Only print pages that have headings
                response_text += f"\n=== Page {page_num + 1} ===\n"
                for i, heading in enumerate(headings, start=1):
                    response_text += f"{i}. {heading}\n"
            else:
                response_text += f"\n=== Page {page_num + 1} === (No headings found)\n"

        await update.message.reply_text(response_text)

    else:
        await update.message.reply_text("Please send a PDF file.")
