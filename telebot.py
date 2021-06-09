import time
import sys
from pytz import timezone
import datetime
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup as MU
from telepot.namedtuple import InlineKeyboardButton as BT
import weather
import airpollution
import schedule
import coin

symbol = ""

#Start Message
startMessage = 'Welcome to Useful Information Bot!\n' + \
        'This is a personal assistant telegram bot.\n' + \
        'Please press any of the following buttons you want to know:\n' + \
        ' - date : Date of today\n' + \
        ' - time : Current time\n' + \
        ' - weather : Current weather of Pohang\n' + \
        ' - airquality : Current air quality of Pohang\n' + \
        ' - add schedule : Add your schedule\n' + \
        ' - check schedule : Check your schedule\n' + \
        ' - coin : Check current price and weather ascending field or not of Cryptocurrency'

scheduleMsg = "Today's schedule!\n\n"

addMessage = "Enter your schedule"

coinMessage = "Enter any of the following commands you want.\n" \
        
coinNameMessage = "Choose the cryptocurrency's name.\n"

#Your own Telegram's token and ID
teleToken = 'YOUR_OWN_TOKEN'
teleID = 'YOUR_OWN_ID'

#Your own encode key
airKey = 'YOUR_OWN_KEY'
weatherKey = 'YOUR_OWN_KEY'

#Add key to weather class
wMsg = weather.weather(weatherKey)
#Add key to airpollution class
aMsg = airpollution.airpollution(airKey)
#Execute coin class
upbit = coin.coin()
coinMsg = ''
#Execute schedule class
timetable = schedule.schedule()
#Execute telepot with your token
bot = telepot.Bot(teleToken)

#Handle messages on telegram
def handle(msg):
    input_chat = msg['text']

    if input_chat == '/help':
        bt1 = BT(text = "Date", callback_data = "1")
        bt2 = BT(text = "Time", callback_data = "2")
        bt3 = BT(text = "Weather", callback_data = "3")
        bt4 = BT(text = "Air pollution", callback_data = "4")
        bt5 = BT(text = "Add schedule", callback_data = "5")
        bt6 = BT(text = "Check schedule", callback_data = "6")
        bt7 = BT(text = "Coin", callback_data = "7")
        bt8 = BT(text = "Exit", callback_data = "8")
        mu = MU(inline_keyboard = [[bt1, bt2], [bt3, bt4], [bt5, bt6], [bt7, bt8]])
        bot.sendMessage(teleID, startMessage, reply_markup = mu)
    else:
        timetable.setSchedule(input_chat)

#Handle button's messgae
def query_ans(msg):
    query_id = msg["id"]
    query_data = msg["data"]
    if query_data == "1":
        bot.sendMessage(teleID, "Current date: " + datetime.datetime.today().strftime("%B %d, %Y"))
        print("Send current date")
    elif query_data == "2":
        bot.sendMessage(teleID, "Current time: " + datetime.datetime.today().strftime("%H:%M"))
        print("Send current time")
    elif query_data == "3":
        bot.sendMessage(teleID, wMsg.getData())
        print("Send weather message")
    elif query_data == "4":
        bot.sendMessage(teleID, aMsg.getData())
        print("Send air message")
    elif query_data == "5":
        bot.sendMessage(teleID, addMessage)
        print("Send get timetable")
    elif query_data == "6":
        bot.sendMessage(teleID, scheduleMsg + timetable.getSchedule())
        print("Send check schedule")
    elif query_data == "7":
        btc = BT(text = "Bitcoin", callback_data = "BTC")
        eth = BT(text = "Ethereum", callback_data = "ETH")
        xrp = BT(text = "Ripple", callback_data = "XRP")
        ada = BT(text = "Cardano (ADA)", callback_data = "ADA")
        coinmu = MU(inline_keyboard = [[btc, eth], [xrp, ada]])
        bot.sendMessage(teleID, coinNameMessage, reply_markup = coinmu)
        print("Send coin data")
    elif query_data == "8":
        bot.sendMessage(teleID, "Bye!")
        print("Send exit")
        sys.exit()
    elif query_data == "BTC":
        coinMsg = upbit.getData("KRW-BTC")
        bot.sendMessage(teleID, coinMsg)
        print("Send Bitcoin data")
    elif query_data == "ETH":
        coinMsg = upbit.getData("KRW-ETH")
        bot.sendMessage(teleID, coinMsg)
        print("Send ethereum data")
    elif query_data == "XRP":
        coinMsg = upbit.getData("KRW-XRP")
        bot.sendMessage(teleID, coinMsg)
        print("Send ripple data")
    elif query_data == "ADA":
        coinMsg = upbit.getData("KRW-ADA")
        bot.sendMessage(teleID, coinMsg)
        print("Send ada data")

print('I am listening...')

#Loop
MessageLoop(bot, {'chat' : handle, "callback_query" : query_ans}).run_as_thread()

while True:
    time.sleep(10)
