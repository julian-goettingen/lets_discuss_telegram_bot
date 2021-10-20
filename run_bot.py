import os
import telegram
from telegram.ext import Updater, CommandHandler

import json

def pprint(name, obj):

    try:
        s = json.dumps(obj, indent=4)
    except Exception as e:
        s = "no json: " + str(obj)

    print("---")
    print(name, ": ", s)
    print("---")

def hello(update, context):
    
    pprint("context", context)
    pprint("update", update)
    pprint("chat_data", context.chat_data)

    text = update["message"]["text"]
    print(text)

    msg = "Hello " + update["message"]["chat"]["first_name"] + "!"

    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


def main():

    api_key = os.getenv("TELEGRAM_BOT_TOKEN")
    bot = telegram.Bot(token=api_key)
    print(bot.get_me())

    updater = Updater(token=api_key, use_context=True)

    hello_handler = CommandHandler("hello", hello)
    updater.dispatcher.add_handler(hello_handler)
    updater.start_polling()


if __name__=="__main__":
    main()


