import telebot
import sqlite3
import os

db = sqlite3.connect('testDB.db', check_same_thread=False)
cur = db.cursor()
bot = telebot.TeleBot('5529782450:AAGaTfAwSzOuBsffIrQk2slEGL2dBDsTXSQ')

def convert(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Отправь фото')

@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'photos' + message.photo[1].file_id + '.jpg')
    print(filename)
    with open(filename, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Фото добавлено")

bot.polling()
