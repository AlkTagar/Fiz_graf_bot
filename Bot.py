import telebot

import config
from Fiz_Graf import *


bot = telebot.TeleBot(config.TOKEN)


# start|help message
@bot.message_handler(commands=["start", "help", "new_graph"])
def comands_handler(message):
    match message.text:
        case "/start" | "/help":
            bot.send_message(
                    message.from_user.id,
                    """
Hello,I'm Fiz bot
it's my stard message
press /new_graph to create new graph
                    """
                    )
        case "/new_graph":
            start_graph(message)
        case _ :
            bot.send_message(
                    message.from_user.id,
                    "?"
                    )


# graph
def start_graph(message): # start
    bot.send_message(
            message.from_user.id,
            "Поочерёдно введите амплитудные значения"
            )
    bot.send_message(
            message.from_user.id,
            "Время в микросекундах t = "
            )
    bot.register_next_step_handler(message, get_T)

# ввод амплотудных значений
T = 0
def get_T(message): # время
    global T
    T = float(message.text)
    bot.send_message(
            message.from_user.id,
            "Индуктивность катушки в наногенри L = "
            )
    bot.register_next_step_handler(message, get_L)

L = 0
def get_L(message): # индуктивность
    global L 
    L = float(message.text)
    bot.send_message(
            message.from_user.id,
            "Электроёмкость конденсатора в миллифарадах C = "
            )
    bot.register_next_step_handler(message, get_C)

C = 0
def get_C(message): # электроёмкость
    global C
    C = float(message.text)
    bot.send_message(
            message.from_user.id,
            "Сила тока в амперах I = "
            )
    bot.register_next_step_handler(message, get_I)

I = 0
def get_I(message): # сила тока
    global I
    I = float(message.text)
    graph(T, L, C, I)


@bot.message_handler(content_types=["text"])
def get_text_message(message):
    bot.send_message(message.from_user.id, "?")


bot.polling(none_stop=True, interval=0)

