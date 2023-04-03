# Добавить функционал боту:
# Кнопки:
#     Хочу анекдот - показывает текстовый анекдот
#     Хочу спать
#     Прощание с ботом
#     Приветствие бота

import telebot
from telebot import types

token = '6149922565:AAGtomaxvbxLvDTI_82n2xJV6fpi5sg9sSU'
bot = telebot.TeleBot(token)
def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Хочу  пить', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу  есть', callback_data='2')
    anegdot_btn = types.InlineKeyboardButton(text='Хочу анекдот', callback_data='3')
    spat_btn = types.InlineKeyboardButton(text='Хочу спать', callback_data='4')
    proshanie_btn = types.InlineKeyboardButton(text='Пока, друг!', callback_data='5')
    privetstvie_btn = types.InlineKeyboardButton(text='Привет, друг!', callback_data='6')
    keyboard.add(drink_btn, eat_btn, anegdot_btn, spat_btn, proshanie_btn, privetstvie_btn  )
    return keyboard
@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Приветствую, друг. Что вы хотите: ',
                     reply_markup=create_keyboard())
@bot.callback_query_handler(func=lambda call:True)
def collback_inline(call):
    if call.message:
        if call.data == '1':
            img = 'https://kartinkin.net/uploads/posts/2022-12/1670611768_17-kartinkin-net-p-kartinka-vodi-dlya-detei-vkontakte-18.jpg'
            bot.send_photo(chat_id=call.message.chat.id, photo=img,
                           caption='Картика воды', reply_markup=create_keyboard())

        if call.data == '2':
            img = 'https://mobimg.b-cdn.net/v3/fetch/b2/b24b4018d1495ab049bddaeda5e0b344.jpeg'
            bot.send_photo(chat_id=call.message.chat.id, photo=img,
                           caption='Картика еды', reply_markup=create_keyboard())

        if call.data == '3':
            bot.send_message(chat_id=call.message.chat.id, text='''— Если бы кто—нибудь сел на вашу шляпу, которую вы положили рядом с собой на скамейке, что бы вы ему сказали?
             — Что он мудак и козел, а что?
             — А то, что вы только что сели на мою шляпу.''', reply_markup=create_keyboard())

        if call.data == '4':
            img = 'https://fikiwiki.com/uploads/posts/2022-02/1645012521_26-fikiwiki-com-p-bistro-spat-prikolnie-kartinki-26.jpg'
            bot.send_photo(chat_id=call.message.chat.id, photo=img,
                            reply_markup=create_keyboard())

        if call.data == '5':
            bot.send_message(chat_id=call.message.chat.id, text='''Всего доброго, друг.''', reply_markup=create_keyboard())

        if call.data == '6':
            bot.send_message(chat_id=call.message.chat.id, text='''Здравствуй, друг.''', reply_markup=create_keyboard())

bot.polling(none_stop=True)