import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def main():
    updater = Updater("PUT_TOKEN_HERE_EVENTUALLY")

    updater.start_polling()

if __name__ == '__main__':
    main()