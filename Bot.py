import telebot
import config
import Fiz_Graf


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start", "help"])
def start_message(message):
    bot.send_message(message.from_user.id, "Hello")


@bot.message_handler(commands=["new_graph"])
def start_graph(message):
    bot.send_message(message.from_user.id, "Поочерёдно введите амплитудные значения")
    bot.send_message(message.from_user.id, "Время в микросекундах t = ")
    bot.register_next_step_handler(message, get_T)

def get_T(message):
    global T
    T = float(message.text)
    print(f"T= {T}")
    bot.send_message(message.from_user.id, "Индуктивность катушки в наногенри L = ")
    bot.register_next_step_handler(message, get_L)

def get_L(message):
    global L
    L = float(message.text)
    print(f"L= {L}")
    bot.send_message(message.from_user.id, "Электроёмкость конденсатора в миллифарадах C = ")
    bot.register_next_step_handler(message, get_C)

def get_C(message):
    global C
    C = float(message.text)
    print(f"C= {C}")
    bot.send_message(message.from_user.id, "Сила тока в амперах I = ")
    bot.register_next_step_handler(message, get_I)

def get_I(message):
    global I
    I = float(message.text)
    print(f"I= {I}")
    # bot.register_next_step_handler(message, get_L)


@bot.message_handler(content_types=["text"])
def get_text_message(message):
    bot.send_message(message.from_user.id, "?")


bot.polling(none_stop=True, interval=0)

