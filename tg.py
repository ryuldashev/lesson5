# coding: utf8
'''
Here is the module for testing functions and telegram integration
'''

import telegram
bot = telegram.Bot(token='656974486:AAFhijLPV10bnge-n8buRhRxKsfpaDYP43I')  # it's a private! Don't steal it!

# just getting info about bot
print(bot.get_me())


# getting updates - unread messages
updates = bot.get_updates()
print([u.message.text for u in updates])



def send_text_to_me(text):
    # sending message to me
    # chat_id = bot.get_updates()[-1].message.chat_id  # тот, с кем у бота была переписка
    chat_id = 82493329
    bot.send_message(chat_id=chat_id, text=text, parse_mode='HTML')


# списки
list1 = range(25, 100, 20)

# print(list1)

for number in list1:
    type_of_number = ''
    if type(number) is int:
        number = number * 1000
        type_of_number = 'ЧИСЛО'
    else:
        type_of_number = 'СТРОКА'

    send_text_to_me('Привет «{}» - {}'.format(number, type_of_number))

# print(list1)
