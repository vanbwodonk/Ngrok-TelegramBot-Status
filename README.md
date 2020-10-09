# Ngrok-TelegramBot-Status
Ngrok free account always change public url connection every new connection. So we need to open ngrok web status if we want to know it. This script just simple parse connection status from localhost:4040/api/tunnels, then send status via telegram bot. So we must already have running ngrok service. 

## Requirements
- Python3.
- Running Ngrok services.
- Telepot. https://telepot.readthedocs.io/en/latest/

## Usage
- Change `('===YOUR BOT TOKEN===')` this script with your bot token. Please create one from botFather(https://telegram.me/BotFather) if you don't have it. 
- Run script `python3 ngrokTbot.py`. 
- Open telegram bot from your Telegram APP(Android/IOS/Desktop/Web), then send `/status` command.

## Output Example
This output example on Telegram App.
```
_____ NGROK STATUS ______
aria: tcp://0.tcp.ap.ngrok.io:17547
ssh: tcp://0.tcp.ap.ngrok.io:13224
webserver: https://49a2d9ab.ap.ngrok.io
webserver (http): http://49a2d9ab.ap.ngrok.io
```
