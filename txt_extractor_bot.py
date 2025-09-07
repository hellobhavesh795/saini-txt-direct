import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

logging.basicConfig(level=logging.INFO)
TOKEN = "YOUR_BOT_TOKEN"  # Replace with your Bot's token

def txt_handler(update: Update, context: CallbackContext):
    document = update.message.document
    if document and document.mime_type == "text/plain":
        file = context.bot.get_file(document.file_id)
        txt_content = file.download_as_bytearray().decode("utf-8", errors="ignore")
        update.message.reply_text(f"Extracted TXT Content:\n\n{txt_content}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.document.mime_type("text/plain"), txt_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()