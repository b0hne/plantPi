import time
import telepot as pot
import serial

from telepot.loop import MessageLoop

"""
pybot for telegram control
"""
lines = ['']*3

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=200)

def handle(msg):
    chat_id = msg['chat']['id']
    
    bot.sendMessage(chat_id, lines)
    print(lines)

bot = pot.Bot('<bot-token>')
pot.loop.MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')
time.sleep(2)
i = 0
while 1:
    time.sleep(2)    
    print(str(ser.readline())[2:-5])
    lines[i] = str(ser.readline())[2:5]

    if float(((lines[i])[:6])) < 60:
        bot.sendMessage(433881991, lines[i])
    i = (i+1)%3
