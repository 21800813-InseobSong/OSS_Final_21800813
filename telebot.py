import time
import sys
from pytz import timezone
import datetime
import telepot
import requests
from telepot.loop import MessageLoop
from selenium import webdriver
import configparser
from xml.etree.ElementTree import parse
import urllib.request as ul
import xmltodict
import json
import io
import weather
import airpollution

#reload(sys)
#sys.setdefaultencoding('utf-8')

symbol = ""
startMessage = 'Welcome to Useful Information Bot!\n' + \
        'This is a personal assistant telegram bot.\n' + \
        'Please enter any of the following commands you want to know:\n' + \
        ' - date : Date of today\n' + \
        ' - time : Current time\n' + \
        ' - weather : Current weather of Handong\n' + \
        ' - airquality : Current air quality of Handong\n' + \
        ' - timetable : Add or check your timetable\n' + \
        ' - coin : Check current price or weather ascending field or not of Cryptocurrency'

tableMessage = 'Enter any of the following commands you want\n' + \
        ' - add : Add your timetable\n' + \
        ' - check : Check your timetable\n'

addMessage = "Enter your timetable in \"Day:Time:Schedule\""

checkMessage = "Enter any of the following commands you want.\n" \
        " - today : Today's timetable\n" \
        " - monday : Monday timetable\n" \
        " - tuesday : Tuesday timetable\n" \
        " - wednesday : Wednesday timetable\n" \
        " - thursday : Thursday timetable\n" \
        " - friday : Friday timetable\n" \

coinMessage = "Enter any of the following commands you want.\n" \
        " - price : Check the cryptocurrency's price\n" \
        " - field : Check the cryptocurrency is in ascending field"

coinNameMessage = "Enter the cryptocurrency's name in ISO Code.\n" \
        "Example : BTC for Bitcoin, ETH for Ethereum"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

weatherKey = 'A8Va%2FzSPCsfzf%2BDnvqP5h8Ork4rjNwCQqkLFeuAdaX%2FVXd1u3XKBg1SIYxUNlpC1vECangTGtRyyw8ki2LkllQ%3D%3D'

airKey = 'A8Va%2FzSPCsfzf%2BDnvqP5h8Ork4rjNwCQqkLFeuAdaX%2FVXd1u3XKBg1SIYxUNlpC1vECangTGtRyyw8ki2LkllQ%3D%3D'

teleToken = '1804852796:AAHbt8n0eAYyM7cuGX38ytc5W94x5TBU-lw'
teleID = '1824568207'
bot = telepot.Bot(teleToken)

wMsg = weather.weather(weatherKey)
aMsg = airpollution.airpollution(airKey)

print(wMsg.getData())

bot.sendMessage(teleID, aMsg.getData())
