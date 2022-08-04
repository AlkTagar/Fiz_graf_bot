import telebot

import config


bot = telebot.TeleBot(config.TOKEN)


def start(message):
    bot.send_message(
        message.from_user.id,
        "Hello, I'm fiz graf bot\n",
        "press /new_graph to\n",
        "create new graf\n"
    )


bot.polling(none_stop=True, interval=0)

