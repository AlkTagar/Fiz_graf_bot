import telebot
import config


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=["text"])
def get_text_message(message):
    match message.text:
        case "/start":
            bot.send_message(message.from_user.id, "Hello")
        case _:
            bot.send_message(message.from_user.id, "?")


bot.polling(none_stop=True, interval=0)

