
"""
* Hello everybody.
* This bot will respond if you call / start and / hello.
* The answer is https://api.advicesLip.com/advic from this site.
* Python methods used googletrans, requests and telebot.
* You can get similar methods of Python from PyPi.org.
* PyPi.org has 310,597 new users.
* much useful information can be obtained with the requests method.
* The googletrans method also translates the entered text into any language.
* The telebot method is a method that creates bots in Python.
"""
"""
* Привет всем.
* Этот бот ответит, если вы позвоните / start и / hello.
* Ответ https://api.advicesLip.com/advic с этого сайта.
* Методы Python использовали googletrans, запросы и телебот.
* Вы можете получить аналогичные методы Python на PyPi.org.
* На PyPi.org 310 597 новых пользователей.
* много полезной информации можно получить с помощью метода запросов.
* Метод googletrans также переводит введенный текст на любой язык.
* Метод телебота - это метод, который создает ботов на Python.
"""
"""
* Assalomu alaykum.
* Bu botga /start va  /salom deb murojjat qilsangiz javob qaytaradi.
* Javob esa https://api.advicesLip.com/advic shu saytdan qaytadi.
* Pythonning methodlaridan googletrans, requests va telebot dan foydalanilgan.
* Pythonning shunga o'xshash methodlarini PyPi.org saytidan olishingiz mumkin.
* PyPi.org sayitida 310,597 shuncha yangi mezodlari bor.
* requests methodi bilan anchagina foydali ma'lumotlarni olsa bo'ladi.
* googletrans methodi ham kiritgan matnni istalgan tilga tarjima qilib beradi.
* telebot methodi Pythonda bot yaratadigan methoddir.
"""
import googletrans
import requests
import telebot

TOKEN = "1705700560:AAEFaay7JIkSfrKOL5BmGGZJIfTOZvMgs1U"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
@bot.message_handler(commands=['start','salom'])
def send_welcome(message):
    url = "https://api.advicesLip.com/advice"
    tranlator = googletrans.Translator()
    r = requests.get(url)
    advice = r.json()['slip']['advice']

    startbot = advice+'\n'
    tarjima = tranlator.translate(advice,dest='uz')
    startbot +=tarjima.text
    bot.reply_to(message,startbot)

bot.polling()

