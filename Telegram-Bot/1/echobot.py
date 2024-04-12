# import telegram.ext 

# TOKEN = "6927590544:AAEIE5ifKSj-s26wjXUWGv6CEkCKud_h5fs"

# updater = telegram.ext.Updater(TOKEN, use_context=True)

# dispatcher = updater.dispatcher

# def start(update, context):
#     update.message.reply_text("Hello! Welcome to the ProjectWheel Telegram Bot!")


# def help(update, context):
#     update.message.reply_text("""
#     /start -> Welcome message 
#     /help -> Help message
#     /content -> Random content 
#     """
#     )


# def content(update, context):
#     update.message.reply_text("Content message from Bot!")


# dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
# # dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
# dispatcher.add_handler(telegram.ext.CommandHandler('content', content))


# updater.start_polling()
# updater.idle()






#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


async def tester(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""

    user = update.effective_user

    await update.message.reply_text(
         rf"Hiyaa {user.mention_html(), update.message.text}!",
        # reply_markup=ForceReply(selective=True),
        )


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6927590544:AAEIE5ifKSj-s26wjXUWGv6CEkCKud_h5fs").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.add_handler(CommandHandler("tester", tester))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()