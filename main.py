import telebot

import config
import special_messages as mes
from input_amplitude_values import in_amp_val


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler()
def comands_handler(message):
    match message.text:

        case "/start" | "/help":
            mes.start(message)

        case "/new_graph":
            in_amp_val(message)

        case _ :
            bot.send_message(message.from_user.id, "?")


bot.polling(none_stop=True, interval=0)

