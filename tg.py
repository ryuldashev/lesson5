# coding: utf8
'''
Here is the module for testing functions and telegram integration
'''

import telegram
bot = telegram.Bot(token='656974486:AAFhijLPV10bnge-n8buRhRxKsfpaDYP43I')  # it's a private! Don't steal it!
CHAT_ID_WITH_RUSLAN = 82493329


def send_text_to_me():
    # sending message to me
    chat_id = CHAT_WITH_RUSLAN

    last_message = bot.get_updates()[-1].message.text

    if last_message == '1':
        text = 'Вы прислали мне цифру один'
    elif last_message == '2':
        text = '<b>TWO IS MY FAVORITE</b>'
    else:
        text = 'Вы мне прислали такой текст: «{}»'.format(last_message)

    bot.send_message(chat_id=chat_id, text=text, parse_mode='HTML')


send_text_to_me()
