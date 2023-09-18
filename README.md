# characterai-telegram-bot
 CharacterAI telegram chatbot. Made using Aiogram 3.


[<img src="https://img.shields.io/badge/Telegram-%40character__chat__bot-blue">](https://t.me/character_chat_bot)
[![wakatime](https://wakatime.com/badge/user/4d0cc4aa-e1c1-483b-8c80-199c9ea5d0c5/project/48718457-e1e9-4031-9742-4ddb44895d9d.svg)](https://wakatime.com/badge/user/4d0cc4aa-e1c1-483b-8c80-199c9ea5d0c5/project/48718457-e1e9-4031-9742-4ddb44895d9d)

![Aiogram](https://img.shields.io/badge/aiogram-14354C?style=for-the-badge&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

 # Contents
 1. <a href="#install">Install</a>
  * <a href="#prequisites">Prequisites</a> 
  * <a href="#basic-startup">Basic startup</a>
  * <a href="#adding-characters">Adding characters to bot</a>
  * <a href="#systemd">Systemd</a>


## Install

### Prequisites
1. Python 3.11 or higher
2. Systemd (if you want to run bot as service)
3. character.ai token

### Basic startup
Clone the repository and install all dependencies by:
```bash
pip install -r requirements.txt
```
Acessing API:
1. Login into character.ai and open DevTools in your browser (F12).
2. Go to Storage -> Local Storage -> char_token, copy value and paste it into .env CHARACTERAI_TOKEN.

Also paste your telegram bot token form @BotFather into .env and start bot:
```bash
python main.py
```

### Adding characters
If you want to add some characters to the /characters menu, you need to get name and id and paste into keyboards.choose_character.characters.
To get id simply copy it form link:
<img src="https://450793928-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FlU2oCgIGdxANM94UL528%2Fuploads%2Fk9H5wKICdt3VMAmThulr%2Fimage_2023-06-08_12-52-52.png?alt=media&token=f0da7a88-11bd-4f2a-bb06-a7cb10f3ff61"/>

### Systemd
Replace '.example' from characterai-bot.service.example so it's just characterai-bot.service.
Then just copy service file to /etc/systemd/system/
```bash
sudo systemctl start characterai-bot.service
```

