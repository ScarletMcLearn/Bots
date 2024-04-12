from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import time
from Environment import TOKEN
# Replace with your bot's access token
BOT_TOKEN = TOKEN

# Username to tag (replace with the actual username)
TARGET_USERNAME = "@scarletmclearn"

# Delay between messages (in seconds) - Adjust as needed, avoid spamming!
MESSAGE_DELAY = 5  # Don't use 5 seconds, consider a higher value

def send_private_message(update, context):
  chat_id = update.effective_chat.id
  message_text = "This is a private message!"
  context.bot.send_message(chat_id=chat_id, text=message_text)
  time.sleep(MESSAGE_DELAY)  # Delay before next message

def send_group_message(update, context):
  chat_id = update.effective_chat.id
  message_text = f"This is a group message! Tagging {TARGET_USERNAME}"
  context.bot.send_message(chat_id=chat_id, text=message_text)
  time.sleep(MESSAGE_DELAY)  # Delay before next message

def start(update, context):
  update.message.reply_text("Bot started!")

def error(update, context):
  print(f"Error: {update.error}")

def main():
  updater = Updater(
    # token=BOT_TOKEN, 
    # use_context=True
    )
  dispatcher = updater.dispatcher

  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(MessageHandler(filters.chat, send_private_message))  # Handles all messages in private chat
  dispatcher.add_handler(MessageHandler(filters.group, send_group_message))  # Handles all messages in groups
  dispatcher.add_error_handler(error)

  updater.start_polling()
  updater.idle()

if __name__ == '__main__':
  main()
