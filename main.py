import telebot # Подключаем библиотеку телеграмм бота
import config # Подключаем конфиг с расположением токена
from telebot import types

# Токен из телеграмма
bot = telebot.TeleBot(config.token)

# Создаем меню с командами
bot.set_my_commands([
    telebot.types.BotCommand("/start", "Приветствие"),
    telebot.types.BotCommand("/help", "Помощь"),
    telebot.types.BotCommand("/name", "Ваше имя"),
])

# Создаем приветствие для новых пользователей
@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text='Приветствую Вас, новый пользователь!')

# Вызывается при команде /start
@bot.message_handler(commands=['start'])
def start(message): # функция которая принимает сообщение и называть ее лучше так как сверху в декораторе
    bot.send_message(message.chat.id, "Привет")  # обращаемся по id и пишет привет
    # bot.send_message(message.chat.id, "<h3>Привет</h3>", parse_mode="html") # обращаемся по id и пишет привет в формате html

# Вызывается при команде /help
@bot.message_handler(commands=["help"])
def helps(message):
    bot.send_message(message.chat.id, "Помощь!")

# Вызывается при команде /pause
@bot.message_handler(commands=["pause"])
def pause(message):
    bot.send_message(message.chat.id, "На паузе")

# Вызывается при команде /name (отоображает полное имя и фамилию пользователя)
@bot.message_handler(commands=["name"])
def name(message):
    mess = f"Тебя зовут: {message.from_user.first_name} {message.from_user.last_name}"
    bot.send_message(message.chat.id, mess)

# Вызывается при обычном сообщении
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Привет" or message.text == "Прив" or message.text == "Хай":
        bot.send_message(message.from_user.id, "Привет, я бот Frontik. Приятно познакомиться!")
    elif message.text == "Как дела?" or message.text == "Как ты?" or message.text == "Как оно?" or message.text == "Как ты":
        bot.send_message(message.from_user.id, "Я отлично. Спасибо что спросил!")
    else:
        bot.send_message(message.from_user.id, "Извини, я пока не распознаю такого рода сообщения...")

# Запускаем бота в режиме без остановки
bot.polling(none_stop=True)