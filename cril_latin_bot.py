
from transliterate import to_latin, to_cyrillic
import telebot

TOKEN="1881218661:AAFiw22Ozu94jNPDR29ZQgdjwSvfcGDGEDA"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    startbot="Assalomu alaykum. Xush kelibsiz :)"
    tanishuv="""Siz bu botga yuborgan lotin matnni- кирил (кирил матнни lotin) matnga aylantirib beradi."""
    tanishuv+=" Sinash uchun istalgan matn yozing !"
    bot.reply_to(message, startbot)
    bot.reply_to(message, tanishuv)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg=message.text
    if msg.isascii():
        javob=to_cyrillic(msg)
    else:
        javob=to_latin(msg)
    bot.reply_to(message, javob)

bot.polling()

