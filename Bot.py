import telebot
import config
import Fiz_Graf


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start", "help"])
def start_message(message):
    bot.send_message(message.from_user.id, "Hello")


@bot.message_handler(commands=["new_graph"])
def graph(message):
    bot.send_message(message.from_user.id, "Введите амплитудные значения")
    return True


@bot.message_handler(func=graph)
def input(message):
    bot.send_message(message.from_user.id, "Введите t")


@bot.message_handler(content_types=["text"])
def get_text_message(message):
    bot.send_message(message.from_user.id, "?")


bot.polling(none_stop=True, interval=0)

