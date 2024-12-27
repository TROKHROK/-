import telebot
from random import randint
bot=telebot.TeleBot("6733903978:AAEDybcBR4uQUvk5kdCVySaglqNudR7gNAQ")

game_arr=dict()
game_setting_arr=dict()
users_arr=list()
# Функция callback_query_handler вносится один раз для обработки всех событий
kb1 = telebot.types.InlineKeyboardMarkup(row_width=1)
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    print(call.data)
    '''
    '''
@bot.message_handler(content_types=['text'])
def start_message(message):
    global users_arr
    if message.text=="Game" and len(users_arr)<1 and game_arr.keys() in f" {message.chat.id}":
        bot_checkers = "⚪️"
        gamer = "⚫️"
        kb1 = telebot.types.InlineKeyboardMarkup(row_width=8)
        for i in range(3):
            if i%2==1:
                kb1.add(telebot.types.InlineKeyboardButton(text=f'{bot_checkers}',callback_data=f'{8-i}a_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{8-i}b_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{bot_checkers}',callback_data=f'{8-i}c_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ',callback_data=f'{8-i}d_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{bot_checkers}', callback_data=f'{8-i}e_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{8-i}f_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{bot_checkers}', callback_data=f'{8-i}g_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{8-i}h_btn')
                                                           )
            else:
                kb1.add(telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{8-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{bot_checkers}', callback_data=f'{8-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{8-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{bot_checkers}', callback_data=f'{8-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{8-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{bot_checkers}', callback_data=f'{8-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{8-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{bot_checkers}', callback_data=f'{8-i}_btn')
                        )
        kb1.add(telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn')
                    )
        kb1.add(telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                    telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),

                telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn'),
                telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{i}_btn')
                )
        for i in range(3):
            if i % 2 == 1:
                kb1.add(telebot.types.InlineKeyboardButton(text=f"{gamer}", callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{gamer}', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{gamer}', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{gamer}', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{4-i}_btn')
                        )
            else:
                kb1.add(telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{gamer}', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{gamer}', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{gamer}', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f' ', callback_data=f'{4-i}_btn'),
                        telebot.types.InlineKeyboardButton(text=f'{gamer}', callback_data=f'{4-i}_btn')
                        )
        bot.send_message(message.chat.id, 'Game:\n', reply_markup=kb1)
    elif message.text == "/start":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        if len(users_arr) < 1:
            users_arr.append(message.chat.id)
        else:
            if (randint(0, 1) == 1):
                gamer2 = "⚪️"
                gamer1 = "⚫️"
            else:
                gamer2 = "⚫️"
                gamer1 = "⚪️"
            gamer_arr[f"{message.chat.id}"]= users_arr[0]
            game_arr[f"{users_arr[0]}"] = message.chat.id
            game_setting_arr[users_arr[0]] = gamer1
            game_setting_arr[message.chat.id] = gamer2
            users_arr = list()
        print(users_arr)
        item1 = telebot.types.KeyboardButton("Game")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
    elif len(users_arr) > 0:
        bot.send_message(message.chat.id, 'Ожидайте начала игры!')

    class App:
        def __init__(self):
            bot.polling(none_stop=True)

    if __name__ == '__main__':
        App()