import time
import random
import telepot
from time import strftime


#Создание словаря
def CreateDictionary(filepath, dictNameDay, dictNameAbout, dictNameDescription):
    f = open(filepath, 'r')
    for line in f:
        line1 = line.strip(' \n')
        linelist = line1.split(';')
        dictkey = linelist[0]
        dictNameDay[dictkey] = linelist[1]
        dictNameAbout[dictkey] = linelist[2]
        if len(linelist) == 4:
            dictNameDescription[dictkey] = linelist[3]
    f.close()

def GetDayFromKalnedar(strdate, dictNameDay, dictNameAbout, dictNameDescription):
    print(strdate)
    if dictNameDay.get(strdate) != None:
        datestring = dictNameDay[strdate] + ': ' + dictNameAbout[strdate] + '. \n'
        if dictNameDescription.get(strdate) != None:
            datestring = datestring + 'Что делать: ' + dictNameDescription[strdate] + '.'
    else:
        datestring = 'Такой даты в календаре нет :('
    return datestring

def WhoAmI(filepath):
    namelist = []
    f = open(filepath, 'r')
    for line in f:
        line1 = line.strip(' \n')
        namelist.append(line1)
    rnd = random.randint(0, len(namelist)-1)
    return namelist[rnd]
        
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id, msg)

    if content_type == 'text':
        rnd = random.randint(1,100)
        if 78 <= rnd <= 80:
            bot.sendSticker(chat_id, "BQADAgADVgADrL-mDN855AFbwOvBAg")
        if 'What time is it?' in msg['text']:
            bot.sendSticker(chat_id, "BQADAgADeAcAAlOx9wOjY2jpAAHq9DUC")
        if msg['text'][0:6] == '/start':
            bot.sendMessage(chat_id, msg['from']['first_name'] + ', я использую команды /data и /whoami')
        if msg['text'][0:7] == '/whoami':
            bot.sendMessage(chat_id, msg['from']['first_name'] + ', ты ' + WhoAmI('data/whoami.txt') + '!')
        if msg['text'][0:5] == '/data':
            kalendar = GetDayFromKalnedar(strftime("%d.%m"), KalendarDay, KalendarAbout, KalendarDescription)
            bot.sendMessage(chat_id, kalendar)

TOKEN = '284057330:AAGXX0cc5NdO-oqPmtvptyQcxKFDsrTgZk0'  # get token from command-line
bot = telepot.Bot(TOKEN)
KalendarDay = {}
KalendarAbout = {}
KalendarDescription = {}
CreateDictionary('data/kalendar.txt', KalendarDay, KalendarAbout, KalendarDescription)



bot.message_loop(handle)


print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
