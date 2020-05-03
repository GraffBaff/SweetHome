import telebot
import datetime

bot = telebot.TeleBot('1283903527:AAHhQ7q2fPw7yH5LjdRHRq0kW_c_3r-cTKw')
time = datetime.datetime.today()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Графство Разврата')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "время":
        bot.send_message(message.from_user.id, time.strftime("%H.%M.%S"))
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Иди в жопу")


bot.polling(none_stop=True, interval=0)
