from telegram.ext import CommandHandler, MessageHandler, Updater, Filters
from vote import kick
from clear import clear_message
from filters import status_update


class AdminBot():
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.dp = self.updater.dispatcher

    def error(self, bot, update, error):
        try:
            raise error
        except BaseException as e:
            print(e)

    def run(self):
        self.dp.add_handler(CommandHandler('kick', kick))
        self.dp.add_handler(MessageHandler(status_update, clear_message))
        self.dp.add_error_handler(self.error)
        self.updater.start_polling()
