from telegram.ext import CommandHandler, Updater
from vote import kick


class AdminBot():
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

    def error(self, bot, update, error):
        try:
            raise error
        except BaseException as e:
            print(e)

    def run(self):
        self.dispatcher.add_handler(CommandHandler('kick', kick))
        self.dispatcher.add_error_handler(self.error)
        self.updater.start_polling()
