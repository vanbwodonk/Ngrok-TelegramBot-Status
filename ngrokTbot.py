#!/usr/bin/env python3
import json
import requests
import time, datetime
import telepot
from telepot.loop import MessageLoop

def getConnectionDetails():
    connection_list = []
    output = "_____ PC ______\n"
    
    #offline test data
    #with open('example.json') as f:
    #    data = json.load(f)
    #api data
    response = requests.get("http://localhost:4040/api/tunnels")
    data = json.loads(response.text)

    data = data['tunnels']
    for item in data:
        connection_details = {"name":None, "public_url":None}
        connection_details['name'] = item['name']
        connection_details['public_url'] = item['public_url']
        connection_list.append(connection_details)
        output += str(item['name']) + ': ' + str(item['public_url']) + '\n'
    return output

conn = getConnectionDetails()
print(conn)

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Received: %s' % command)

    if command == '/status':
        conn = getConnectionDetails()
        telegram_bot.sendMessage (chat_id, conn)

telegram_bot = telepot.Bot('===YOUR BOT TOKEN===')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running....')

while 1:
    time.sleep(10)