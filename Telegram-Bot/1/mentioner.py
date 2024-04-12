from telegram import Bot, Update
from telegram.constants import ParseMode

from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def private_message(update: Update, context: CallbackContext) -> None:
    """Send a private message to a user."""
    username = context.args[0]
    message = ' '.join(context.args[1:])
    context.bot.send_message(chat_id=username, text=message)

def group_message(update: Update, context: CallbackContext) -> None:
    """Mention a user in a group message."""
    username = context.args[0]
    message = ' '.join(context.args[1:])
    update.message.reply_text(f'@{username} {message}', parse_mode=ParseMode.MARKDOWN)

from Environment import TOKEN 

def main() -> None:
    """Start the bot."""
    updater = Updater(TOKEN, 
    # use_context=True
    
    )

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("private_message", private_message))
    dp.add_handler(CommandHandler("group_message", group_message))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
