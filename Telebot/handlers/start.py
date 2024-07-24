from telebot.types import Message
from loader import bot
from countryinfo import CountryInfo
from keyboards.defoult import country_btn

@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    markup = country_btn()
    bot.send_message(chat_id, f"Hi, {first_name}!👋", reply_markup=markup)

@bot.message_handler(commands=['help'])
def command_help(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    bot.send_message(chat_id, f"{first_name}, what kind of help do you need?🧐")