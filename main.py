import telebot
import time
from telebot import types

# pip install pytelegrambotapi
token = '7044432793:AAEIaYwlNC8gTe5_fXD5GTRpCrUPMncggIA'
bot = telebot.TeleBot(token)
chat_id = '-1001915050902'  # Например chat_id = '223344'
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))


# Telegram bot: Get My Id

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, text="""Мы рады Вас видеть!😊
    Если Вы перешли по этой ссылке, значит у Вас точно есть к нам вопросы❤️
    
    Мы благодарны Вам за доверие и будем рады помочь 🙏
    
    Здесь Вы можете написать нам свои любые вопросы, касающиеся родительства, воспитания, развития детей, отношений, именно то, что Вас беспокоит сейчас больше всего.
    
    Пишите смело. Искренне. То, что сейчас заставляет Вас испытывать отрицательные эмоции, то с чем Вы не можете справиться в своем родительстве и личной жизни.
    
    Все вопросы наши специалисты прицельно изучат и на самые актуальные мы будем отвечать своими постами в специальной рубрике "Отвечаем на вопросы читателей".
    
    А сейчас мы ждём Ваш вопрос. Задавайте⬇️""")


@bot.message_handler(func=lambda message: True)

def echo_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Да', callback_data='question_no')
    item2 = types.InlineKeyboardButton('Нет', callback_data='question_yes')
    markup.add(item, item2)

    user:User = message.from_user

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
        
    bot.send_message(message.chat.id, 'Вы хотите что-то добавить к вашему вопросу?', reply_markup=markup)

    print(message.date)

    # markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item11 = types.KeyboardButton('Задать вопрос')
    # markup1.add(item11)
    # bot.send_message(message.chat.id, 'Error', reply_markup=markup1)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'question_no':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
        elif call.data == 'question_yes':

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= """Ваш вопрос успешно принят и направлен специалистам!

Благодарим Вас за доверие!

Мы будем публиковать ответы на самые популярные вопросы постами в наших официальных сообществах:

1. ВКонтакте: https://vk.com/up4brain

2. В телеграм канале: https://t.me/neyroparents

Мы рады, что Вы с нами!

Если вы хотите задать еще один вопрос или у вас есть предложение - откройте меню слева от строки ввода или просто напишите свой вопрос.""", disable_web_page_preview=True)



bot.polling()
