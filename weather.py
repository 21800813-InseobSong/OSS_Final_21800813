import time
import sys
import datetime
import requests
import xml.etree.ElementTree as et
import re

class weather:
    weatherURL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?'
    weatherKey = ''
    today = ""
    base_date = ""
    base_time = ''
    nx = ''
    ny = ''

    def __init__(self, key):
        self.weatherKey = key
        self.today = datetime.datetime.today()
        self.base_date = self.today.strftime("%Y%m%d")
        self.base_time = self.parseTime()
        self.nx = '102'
        self.ny = '96'

    def getData(self):
        weather_load = 'serviceKey=' + self.weatherKey + '&numOfRows=1000&pageNo=1' + \
                '&base_date=' + self.base_date + '&base_time=' + self.base_time + '&nx=' + self.nx + '&ny=' + self.ny
        response = requests.get(self.weatherURL + weather_load)
        text = response.text
        root = et.fromstring(text)
        childs = root.getiterator("item")
        string = ''
        maintime = self.maintime()
        maindate = self.maindate()
        weatherString = "As of Pohang, " + maintime + " on " + maindate.strftime("%B %d, %Y") + "\n"
        for i in childs:
            string = et.tostring(i).decode('utf-8')
            removeTag = re.sub('<.+?>', ' ', string, re.I|re.S)
            splitString = removeTag.split()
            if "T3H" in string: 
                if splitString[3] == maindate.strftime("%Y%m%d")  and splitString[4] == maintime in string:
                    weatherString = weatherString + "Current temperature : " + splitString[5] + " degrees\n"
            if "TMX" in string:
                if splitString[3] == maindate.strftime("%Y%m%d") in string:
                    weatherString = weatherString + "Highest temperature : " + splitString[5] + " degrees\n"
            if "POP" in string:
                if splitString[3] == maindate.strftime("%Y%m%d") and splitString[4] == maintime in string:
                    weatherString = weatherString + "Current Rainfall probability : " +splitString[5] + "%\n"
        return weatherString

    def parseTime(self):
        time = self.today.strftime("%H%M")
        if time < '0200':
            self.base_date = str(int(self.base_date)-1)
            return '2300'
        elif time < '0500':
            return '0200'
        elif time < '0800':
            return '0500'
        elif time < '1100':
            return '0800'
        elif time < '1400':
            return '1100'
        elif time < '1700':
            return '1400'
        elif time < '2000':
            return '1700'
        elif time < '2300':
            return '2000'
        else:
            return time

    def maintime(self):
        time = self.today.strftime("%H%M")
        if time < '0200' or time >= '2300':
            return '0300'
        elif time < '0500':
            return '0600'
        elif time < '0800':
            return '0900'
        elif time < '1100':
            return '1200'
        elif time < '1400':
            return '1500'
        elif time < '1700':
            return '1800'
        elif time < '2000':
            return '2100'
        elif time < '2300':
            return '0000'
    
    def maindate(self):
        date = self.today
        time = self.today.strftime("%H%M")
        if time >= '2000':
            date = date + datetime.timedelta(days=1)
            return date
        else:
            return date
