# Ngrok-TelegramBot-Status
Ngrok free account always change public url connection every new connection. So we need to open ngrok web status if we want to know it. This script just simple parse connection status from localhost:4040/api/tunnels, then send status via telegram bot. So we must already have running ngrok service. 

## Requirements
- Python3.
- Running Ngrok services.
- Telepot. https://telepot.readthedocs.io/en/latest/

## Requirements
Open telegram bot, then send `/status` command.
