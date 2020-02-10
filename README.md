# Ngrok-TelegramBot-Status
Ngrok free account always change public url connection every new connection. So we need to open ngrok web status if we want to know it. This script just simple parse connection status from localhost:4040/api/tunnels, then send status via telegram bot. So we must already have running ngrok service. 

## Requirements
- Python3.
- Running Ngrok services.
- Telepot. https://telepot.readthedocs.io/en/latest/

## Usage
- Change `('===YOUR BOT TOKEN===')` this script with your bot token. Please create one from botFather(https://telegram.me/BotFather) if you don't have it. 
- Run script `python3 ngrokTbot.py`. 
- Open telegram bot from your Telegram APP(Android/IOS/Desktop/Web whatever), then send `/status` command.
