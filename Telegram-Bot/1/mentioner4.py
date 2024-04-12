import time
from telegram import Bot
from Environment import TOKEN

bot = Bot(token=TOKEN)

# while True:
#     # Send a private message to a user
#     bot.send_message(chat_id='USER_ID', text='Hello, this is a private message.')

#     # Send a group message and tag a user
#     bot.send_message(chat_id='GROUP_ID', text='Hello @USERNAME, this is a group message.')

#     # Wait for 5 seconds
#     time.sleep(5)


import asyncio
from telegram import Bot

bot = Bot(token=TOKEN)


# List of user IDs who have interacted with the bot
user_ids = ['6878658109', 
# 'USER_ID2', 'USER_ID3', ...
]

async def send_messages():
    while True:
        # # Send a private message to a user
        # await bot.send_message(chat_id='6878658109', text='Hello @GetRatulNow, this is a private message.')

        # Send a group message and tag a user
        await bot.send_message(chat_id='-4191657913', text='Hello @GetRatulNow, this is a group message.')



        for user_id in user_ids:
            # Send a private message to each user
            await bot.send_message(chat_id=user_id, text='Hello @GetRatulNow, this is a private message.')

        # Wait for 5 seconds
        await asyncio.sleep(5)

# Run the async function using asyncio
asyncio.run(send_messages())
