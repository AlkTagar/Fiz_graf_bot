import telebot

import config


bot = telebot.TeleBot(config.TOKEN)


def in_amp_val(message):

    def start_graph(message):
        bot.send_message(
                message.from_user.id,
                "Поочерёдно введите амплитудные значения")

        bot.send_message(
                message.from_user.id,
                "Время в микросекундах t = ")

        bot.register_next_step_handler(message, get_T)


    T = 0
    def get_T(message): # время
        global T

        T = float(message.text)

        bot.send_message(
                message.from_user.id,
                "Индуктивность катушки в наногенри L = ")

        bot.register_next_step_handler(message, get_L)

    L = 0
    def get_L(message): # индуктивность
        global L

        L = float(message.text)

        bot.send_message(
                message.from_user.id,
                "Электроёмкость конденсатора в миллифарадах C = ")

        bot.register_next_step_handler(message, get_C)

    C = 0
    def get_C(message): # электроёмкость
        global C

        C = float(message.text)

        bot.send_message(
                message.from_user.id,
                "Сила тока в амперах I = ")

        bot.register_next_step_handler(message, get_I)

    I = 0
    def get_I(message): # сила тока
        global I

        I = float(message.text)

    start_graph(message)

    return T, L, C, I


bot.polling(none_stop=True, interval=0)

