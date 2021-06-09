# 2021-1 Open-source Software Laboratories Final project

## What does this project do?
This program is presonal telegram bot, which shows useful information.
We can run this program with Raspberry Pi and Python, and you could use this bot anytime, anywhere while this program is running.
It uses Open API, so you could see the data in text, instead of capturing site.

## Then, what information does this project show?
At the first time you run the bot, you can see how to use this program.
After that, the bot will wait your command.
You can get the following informations from this bot.
 - Date : Date of today
 - Time : Current time
 - Weather : Current weather of Pohang
 - Airquality : Current air quality of Pohang
 - Add schedule : Add your schedule
 - Check schedule : Check your schedule
 - Coin : Check current price and weather ascending field or not of Cryptocurrency
        
## How to run this program?
1. Prepare your own Raspberry Pi and make it usable
2. Clone this repository to your Raspberry Pi
3. Install libraries.
   ```
   $ sudo apt-get update
   $ sudo apt-get install python3
   $ sudo pip3 install pyupbit
   $ sudo apt-get install python-bs4
   $ sudo pip3 install telepot
   $ sudo pip3 install datetime
   $ sudo pip3 install requests
   ```
4. Create your own Telegram account.
5. In telegram, type 'BotFather' in the search bar.
6. Enter followings to create your own bot.
   + `/start`
   + `/newbot`
   + bot name
   + user name for bot
7. Get your bot's token to access your bot, and insert your token into `teleToken = 'YOUR_OWN_TOKEN'` instead of `YOUR_OWN_TOKEN`
8. Type `@get_id_bot` in the search bar to get your own telegram id number.
9. Enter `/start`, and insert your telegram id into `teleID = 'YOUR_OWN_ID'` instead of `YOUR_OWN_ID`
10. Go to `https://www.data.go.kr/` and create new account.
11. Log in `https://wwwldata.go.kr/` and go to `https://www.data.go.kr/data/15057682/openapi.do`
12. Click the `Request (활용신청)` button and choose all the check button.
13. Copy your `Encoding (일반인증키)` and paste into `weatherKey = 'YOUR_OWN_KEY'` instead of `YOUR_OWN_KEY`
14. Go to `https://www.data.go.kr/data/15073861/openapi.do` and click the button `활용신청` button and choose all the check button.
15. Copy your `Encoding (일반인증키)` and paste into `airKey = 'YOUR_OWN_KEY'` instead of `YOUR_OWN_KEY`
16. If you want to know other cryptocurrency's information, go to `query_ans(msg)` and modify `elif query_data == "BTC":` part to what you want to know.
17. When you change coin part, you should enter the ISO 4217 code.
18. Go to Raspberry Pi console, and go to this program's directory.
19. Enter `$ python3 telebot.py` to run this program, and now, bot is ready.
20. In telegram, enter your bot's name in search bar, and enter `/help` to see help menu.

## References
 - [Make GUI in telegram bot](https://minmong.tistory.com/312)
 - [How to use 'Public Data Portal' data in Python](https://blog.naver.com/PostView.nhn?blogId=pk3152&logNo=221367298814)
 - [Distinguish between rising and falling fields](https://wikidocs.net/21882)
 - [How to remove HTML Tag](http://zeany.net/46)

## New work I added in this project
 - Implemented GUI to use easier.
 - Get weather information by using Open API, and show in text to ㅎet the information you need right away.
 - Get air pollution information by using Open API, and show in text to ㅎet the information you need right away.
 - Make current time and date button to know Korean Standart Time(KST).
 - Get current time with datetime module, and cut into `Hour:Minute`
 - Get current date with datetime module, and cut into `Month Day, Year`
 - When you enter your schedule, it will add your schedule
 - Implemented ascending or descending field of specific cryptocurrency.

## How to ask more about this project?
If you need more help, please send email to `21800813@handong.edu`

## Youtube link
I will add it later
