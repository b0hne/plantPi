import time
import telepot as pot
import serial
from telepot.loop import MessageLoop

"""
pybot for telegram control
"""
num_plants = 5
lines = ['']*num_plants
telegram_id = 'users telegramid'

def check():
    for i in range(num_plants):
        lines[i] = str(ser.readline())[2:-5]
        if float((lines[i][0:5])) < 45:
            bot.sendMessage(telegram_id, lines[i])

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=200)
bot = pot.Bot('<bot-id>')
def handle(msg):
    chat_id = msg['chat']['id']
    if msg == 'recheck':
        check()
    bot.sendMessage(chat_id, lines)


pot.loop.MessageLoop(bot, handle).run_as_thread()
timer = 0
while 1:
    if timer == 0:
        bot.sendMessage(telegram_id, 'I am still alife')
    timer += 1
    timer %= 48
    check()
    time.sleep(1800)
