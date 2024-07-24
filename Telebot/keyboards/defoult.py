from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def country_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    country = KeyboardButton('Country')
    markup.add(country)
    return markup
