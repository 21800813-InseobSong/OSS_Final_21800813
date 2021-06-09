import requests
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup as bs

class airpollution:
    airKey = ""
    airURL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?"

    def __init__(self, key):
        self.airKey = key

    def getData(self):
        air_load = 'serviceKey=' + self.airKey + '&returnType=xml&numOfRows=1&pageNo=1&stationName=%ED%8F%AC%ED%95%AD%ED%95%AD&dataTerm=DAILY&ver=1.0'
        loadURL = self.airURL + air_load
        response = requests.get(loadURL)
        text = response.text
        root = et.fromstring(text)
        childs = root.getiterator("item")
        string = ''
        airString = ''
        for i in childs:
            string = et.tostring(i).decode('utf-8')
            removeTag = bs(string, "lxml").text
            splitString = removeTag.split()
            airString = "At Handong, " + splitString[11] + ", " + splitString[10] + \
                    "\nCurrent PM10 concentration: " + splitString[4] + "\nCurrent PM2.5 concentration: " + \
                    splitString[7]
            if splitString[14] == "1":
                airString = airString + "\nCurrent PM10 state is good"
            elif splitString[14] == "2":
                airString = airString + "\nCurrent PM10 state is normal"
            elif splitString[14] == "3":
                airString = airString + "\nCurrent PM10 state is bad"
            elif splitString[14] == "4":
                airString = airString + "\nCurrent PM10 state is very bad"

            if splitString[9] == "1":
                airString = airString + "\nCurrent PM2.5 state is good"
            elif splitString[9] == "2":
                airString = airString + "\nCurrent PM2.5 state is good"
            elif splitString[9] == "3":
                airString = airString + "\nCurrent PM2.5 state is good"
            elif splitString[9] == "4":
                airString = airString + "\nCurrent PM2.5 state is good"
        return airString
