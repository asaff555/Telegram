
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am @Man_uellaBot, and I am ready to assist.")

def test(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("The bot is working perfectly!")

def main():
    # Fetch the bot token from environment variables
    TOKEN = os.getenv("BOT_TOKEN", "7840102420:AAERfijF8vYeof58NIMXiamn9_oGoHFPguo")

    # Initialize the Updater with the bot token
    updater = Updater(TOKEN, use_context=True)

    # Register command handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("test", test))

    # Start the bot
    updater.start_polling()

    # Keep the bot running
    updater.idle()

if __name__ == "__main__":
    main()
