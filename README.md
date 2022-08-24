# Currency Telegram Bot

<p align="center"> 
<img src="![photo_2022-08-24_04-38-10](https://user-images.githubusercontent.com/85646058/186297479-aeabe60c-e3f5-475d-9b3d-0da4b4bdc48b.jpg)" width="800">
</p>

Telegram Bot shows the rates of the main currencies of various banks in Batumi

## Contents

1. telegram bot [[link](https://github.com/ArtKrup/currency_tbot/edit/master/currency_tbot.py)]
  main files contens commands for telegram bot
2. database queries [[link](https://github.com/ArtKrup/currency_tbot/blob/master/queries.py)]
  postgres database with adding and updating data functions 
3. parser [[link](https://github.com/ArtKrup/currency_tbot/blob/master/requests_banks.py)]
  parser for getting bank rates from websites

## Installing

1. Install Python-libraries:

`$ pip install -r requirements.txt`

2. Create Telegram Bot via [Bot Father (https://t.me/BotFather)]

3. Add valid TELEGRAM TOKEN ID in [currency_tbot.py (https://github.com/ArtKrup/currency_tbot/edit/master/currency_tbot.py)]

4. Add valid css classes in [parser (https://github.com/ArtKrup/currency_tbot/blob/master/requests_banks.py)]

5. Create new app in [Heroku (https://dashboard.heroku.com/apps)]
  5.1 Choose deploy method "Connect to GitHub"
  5.2 Input 'currency_tbot' into repo-name
  5.3 Push 'Deploy Branch'
  
