#reference:
#https://www.instructables.com/Set-up-Telegram-Bot-on-Raspberry-Pi/

import telepot

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    print("got command: %s" % command)
    print ('Got chat_id: %s' % chat_id)
    
    if command == 'Hi':
        bot.sendMessage(chat_id, "Hi good morning")
    elif command == 'Good afternoon':
        bot.sendMessage(chat_id, "Hi good afternoon")

bot = telepot.Bot('YOUR OWN TELEBOT TOKEN')
#bot.getMe()
bot.message_loop(handle)
print("i amm listening...")
bot.sendMessage('CHAT ID YOU WANT TO SEND', "Hi good morning")

# ANOTHER CODE YOU COULD TRY
# import time
# import random
# import datetime
# import telepot
# from telepot.loop import MessageLoop
# 
# """
# After **inserting token** in the source code, run it:
# ```
# $ python2.7 diceyclock.py
# ```
# [Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
# teaching you how to setup a bot on Raspberry Pi. This simple bot does nothing
# but accepts two commands:
# - `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
# - `/time` - reply with the current time, like a clock.
# """
# 
# def handle(msg):
#     chat_id = msg['chat']['id']
#     command = msg['text']
# 
#     print ('Got command: %s' % command)
#     print ('Got chat_id: %s' % chat_id)
#     #print ('Got id: %s' % id)
# 
#     if command == '/roll':
#         bot.sendMessage(chat_id, random.randint(1,6))
#     elif command == '/time':
#         bot.sendMessage(chat_id, str(datetime.datetime.now()))
# 
# bot = telepot.Bot('YOUR OWN TELEBOT TOKEN')
# 
# MessageLoop(bot, handle).run_as_thread()
# print ('I am listening ...')
# 
# while 1:
#     time.sleep(10)
