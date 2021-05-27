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

puppies = []

def del_puppy(update: Update, context: CallbackContext) -> None:
    if not context.args[0] or not context.args[0].startswith('@'):
        update.message.reply_text("Command usage: \"/delpuppy @username\"")

    username = context.args[0]
    
    if username in puppies:
        puppies.remove(username)
        update.message.reply_text("User {username} is no longer a puppy.")
    else:
        update.message.reply_text("User {username} is not currently a puppy.")

def set_puppy(update: Update, context: CallbackContext) -> None:
    if not context.args[0] or not context.args[0].startswith('@'):
        update.message.reply_text("Command usage: \"/setpuppy @username\"")

    username = context.args[0]
    
    if username in puppies:
        update.message.reply_text("User {username} is already a puppy.")
    else:
        puppies.append(username)
        update.message.reply_text("User {username} is now a puppy. Good pup!")

def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher    

    # register handlers
    dispatcher.add_handler(CommandHandler("setpuppy", set_puppy))
    dispatcher.add_handler(CommandHandler("delpuppy", del_puppy))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()