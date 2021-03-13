import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import tokens

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Fetch bot token
BOT_TOKEN = tokens.BOT_TOKEN

logger = logging.getLogger(__name__)

def main():
    updater = Updater(BOT_TOKEN)

    updater.start_polling()

if __name__ == '__main__':
    main()