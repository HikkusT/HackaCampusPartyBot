from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

def start(update, context):
    print(update.message.chat_id)
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def main():
    updater = Updater(token='841166799:AAG-HKf9gZKLLmaG6mp_4dgn4NNS2NIRRN8', use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()