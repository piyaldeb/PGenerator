import telebot
import pyqrcode
from PIL import Image
import time
import qrcode
from io import BytesIO

token = "6010556651:AAHmWV5HtzjOVyrEuyhHeBeg8os-EKc9DHw"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def se(msg):##for getting the starting message
    bot.send_chat_action(msg.chat.id, 'typing')
    bot.send_message(msg.chat.id, 'Hey There,\n Use /QR_Code_Gen by Ranak_Debnath to generate QR CODE and it will  be workabe with any scanner ')


@bot.message_handler(commands=['QR_Code_Gen'])
def qr_code_handler(message):
    ##bot.send_chat_action(message.chat.id, 'typing')
    sent = bot.send_message(message.chat.id, "Send only Url(www.youtube.com/xyz)")
    bot.register_next_step_handler(sent, qrcode)


def qrcode(message):
    url = pyqrcode.create(message.text)
    url.png('qrcode.png', scale=15)
    bot.send_document(message.chat.id, open('qrcode.png', 'rb'))


while True:
    try:
        bot.polling(True)
    except Exception:

        time.sleep(1)
