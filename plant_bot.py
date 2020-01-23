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

bot = pot.Bot('<bot id>')
pot.loop.MessageLoop(bot, handle).run_as_thread()

i = 0
while 1:
    time.sleep(50)
    lines[i] = str(ser.readline())[2:-5]

    if float((lines[i][0:5])) < 60:
        print(float((lines[i][0:5])))
        bot.sendMessage(433881991, lines[i])
    i = (i+1)%3
