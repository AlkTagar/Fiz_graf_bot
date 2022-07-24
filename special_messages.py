import telebot

import config


bot = telebot.TeleBot(config.TOKEN)


def start(message):
    bot.send_message(
            message.from_user.id, """
Hello, I'm fiz graf bot
  press /new_graph to
    create new graf
            """)


bot.polling(none_stop=True, interval=0)

