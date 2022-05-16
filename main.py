import telebot
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")
configfile = "config.cfg"  # Подключаем файл конфигурации

bot = telebot.TeleBot(config["Telegram"]["Token"])  # Создаём экземпляр бота Telegram

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Welcome to Useless Shit!\nGitHub Link: https://github.com/Windozer/UselessTGTools\nCoded by Windozer")

@bot.message_handler(content_types=["sticker"])
def send_sticker(message):
    sticker_id = message.sticker.file_id
    bot.send_message(message.chat.id, f'Sticker Info\nID: {sticker_id}')

@bot.message_handler(commands=["user"])
def send_sticker(message):
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    UID = message.from_user.id
    bot.send_message(message.chat.id, f'User Info\nNickname: @{username}\nFirst Name: {first_name}\nLast Name: {last_name}\nID: {UID}')

bot.polling(none_stop=True, interval=0)  # Запускаем бота