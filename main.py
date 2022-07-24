import telebot

import config
import special_messages as mes
from input_amplitude_values import in_amp_val


print("start")
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=["text"])
def comands_handler(message):
    print("get text")
    match message.text:

        case "/start" | "/help":
            print("start case")
            mes.start(message)

        case "/new_graph":
            print("new case")
            in_amp_val(message)

        case _ :
            bot.send_message(message.from_user.id, "?")


bot.polling(none_stop=True, interval=0)

