from telegram.ext import (CommandHandler)


class Start(object):
    def __init__(self):
        self.START_HANDLER = CommandHandler('start', self.start)

    def start(self, bot, update):
        message = "Hello father, Let's get to work..."
        username = update.message.from_user.username

        if username != 'humble_D':
            message = ('Hello %s, I was created by Aakash Mallik and I am here to help...' %
                       update.message.from_user.first_name)

        bot.send_message(chat_id=update.message.chat_id,
                         text=message)
