import telebot
from main import functions
from decouple import config

BOT_TOKEN = config("token")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, """
    /start ---> start the bot
    /meme ---> Get random meme every click

""")

@bot.message_handler(commands=["meme"])
def get_meme(message):
    functions.photosave()
    bot.send_photo(message.chat.id, photo=open("photo.png", "rb"))
    bot.send_message(message.chat.id, "صاحب البوت غير مسؤول إذا كانت الميمز تحتوي على محرمات")
    bot.send_message(message.chat.id, "The bot owner is not responsible if the meme contains prohibited content")


bot.infinity_polling()