import telebot

import config
import special_messages
from input_amplitude_values import start_graph


print("start")
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=["text"])
def comands_handler(message):
    print("get text")
    match message.text:

        case "/start" | "/help":
            print("start case")
            special_messages.start(message)

        case "/new_graph":
            print("new case")
            start_graph(message)

        case _ :
            bot.send_message(message.from_user.id, "?")


bot.polling(none_stop=True, interval=0)

