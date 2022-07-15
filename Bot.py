import telebot
import config
from Fiz_Graf import *


bot = telebot.TeleBot(config.TOKEN)


# start|help message
@bot.message_handler(commands=["start", "help"])
def start_message(message):
    bot.send_message(message.from_user.id, """
Hello,
I'm Fiz bot
        """)


# graph
@bot.message_handler(commands=["new_graph"])
def start_graph(message): # start
    bot.send_message(message.from_user.id, "Поочерёдно введите амплитудные значения")
    bot.send_message(message.from_user.id, "Время в микросекундах t = ")
    bot.register_next_step_handler(message, get_T)

# ввод амплотудных значений
T = 0
def get_T(message): # время
    global T
    T = float(message.text)
    bot.send_message(message.from_user.id, "Индуктивность катушки в наногенри L = ")
    bot.register_next_step_handler(message, get_L)

L = 0
def get_L(message): # индуктивность
    global L 
    L = float(message.text)
    bot.send_message(message.from_user.id, "Электроёмкость конденсатора в миллифарадах C = ")
    bot.register_next_step_handler(message, get_C)

C = 0
def get_C(message): # электроёмкость
    global C
    C = float(message.text)
    bot.send_message(message.from_user.id, "Сила тока в амперах I = ")
    bot.register_next_step_handler(message, get_I)

I = 0
def get_I(message): # сила тока
    global I
    I = float(message.text)
    print(f"T= {T}")
    print(f"L= {L}")
    print(f"C= {C}")
    print(f"I= {I}")
    graph(T, L, C, I)


@bot.message_handler(content_types=["text"])
def get_text_message(message):
    bot.send_message(message.from_user.id, "?")


bot.polling(none_stop=True, interval=0)

