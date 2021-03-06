import logging
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, CallbackQueryHandler

from vote import kick, vote
from clear import clear_message
from filters import status_update
from start import start


class AdminBot():
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.dp = self.updater.dispatcher

    def error(self, bot, update, error):
        try:
            raise error
        except BaseException as e:
            logging.error(e)

    def run(self):
        self.dp.add_handler(CommandHandler('start', start))
        self.dp.add_handler(CommandHandler('kick', kick))
        self.dp.add_handler(CallbackQueryHandler(vote))
        self.dp.add_handler(MessageHandler(status_update, clear_message))
        self.dp.add_error_handler(self.error)
        self.updater.start_polling()
