from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram import ChatAction
from Environment import TOKEN 

# Telegram bot token obtained from BotFather
# TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Create an Updater object to fetch updates from Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define a command handler for the start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot.")

# Define a private message handler
def private_message(update, context):
    username = update.effective_user.username
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello @{username}! This is a private message.")

# Define a group message handler
def group_message(update, context):
    # Get the username mentioned in the message
    mentioned_username = update.message.text.split()[1]
    chat_id = update.effective_chat.id
    user_id = None
    
    # Check if the mentioned username is in the group
    for member in context.bot.get_chat_members(chat_id):
        if member.user.username == mentioned_username:
            user_id = member.user.id
            break
    
    # If user is in the group, mention them using their ID
    if user_id:
        context.bot.send_message(chat_id=chat_id, text=f"@{mentioned_username}, you have been mentioned in this group!")
    # If user is not in the group, mention the username only
    else:
        context.bot.send_message(chat_id=chat_id, text=f"@{mentioned_username} has been mentioned in this group!")

# Register handlers for commands and messages
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

private_message_handler = MessageHandler(Filters.private, private_message)
dispatcher.add_handler(private_message_handler)

group_message_handler = MessageHandler(Filters.group, group_message)
dispatcher.add_handler(group_message_handler)

# Start the bot
updater.start_polling()
updater.idle()
