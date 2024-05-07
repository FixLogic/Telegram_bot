import telebot
import time
import datetime
from texts import late_text, hello_text, bye_text
from telebot import types


# Код не пригоден для использования так как он специально сломан чтобы никто постороних им не воспользовался
# pip install pytelegrambotapi
token = '#'
# date_ = datetime.datetime(2024,4,20,13,30)
date_ = datetime.datetime.now(#)
bot = telebot.TeleBot(token)
chat_id = '#'
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtim(x))
anonymousMode = True


# Telegram bot: Get My Id

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, text= str(hello_text))

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, text=str())

@bot.message_handler(func=lambda message: True)

def echo_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Да', callback_data='question_no')
    item2 = types.InlineKeyboardButton('Нет', callback_data='question_yes')
    markup.add(item, item2)

    user:User = message.from_user
    if date_.weekday() == 5:
        if date_.hour >= 12 and dte_.hour <= 15:
            if anonymousMode == False:
                bot.send_message(
                    chat_id=chat_id,
                    text="Вопрос: | " + str(message.text) + " | Информация об авторе: @" +
                         str(user.username) + " Имя: " + str(user.first_name) + " Фамилия: " +
                         str(user.last_name) + " User_ID: " + str(user.id) + " Message_date: " +
                         str(tconv(message.date)))
            else:
                bot.send_message(chat_id=chat_id,
                                 text="Вопрос: | " + str(message.text) +
                                      " | Дата отправки: " + str(tconv(message.date)) +
                                      " | Включен режим анонимности")

                bot.send_message(messag.chat.id, 'Вы хотите что-то добавить к вашему вопросу?', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text= str(late_text))

    print(message.date)




@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'question_no':
            bot.delete_message(chat_i=call.message.chat.id, message_id=call.message.id)
        elif call.data == 'question_yes':

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= str(bye_text), disable_web_page_preview=True)



bot.poling()

