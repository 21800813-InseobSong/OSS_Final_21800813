import requests
import xml.etree.ElementTree as et
import xmltodict
import re
import urllib.request

class airpollution:
    airKey = ""
    airURL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?"

    def __init__(self, key):
        self.airKey = key

    def getData(self):
        air_load = 'serviceKey=' + self.airKey + '&returnType=xml&numOfRows=1&pageNo=1&stationName=%ED%8F%AC%ED%95%AD%ED%95%AD&dateTerm=DAILY&ver=1.0'
        loadURL = self.airURL + air_load
        print(loadURL + '\n')

        request = urllib.request.Request(loadURL)
        response = urllib.request.urlopen(request)
        return response.read().decode('utf-8')
        #response = requests.get(loadURL)
        #text = response.text
        #root = et.fromstring(text)
        #print(text)
        #childs = root.getiterator("item")
        #string = ''
        #for i in childs:
            #string = et.tostring(i).decode('utf-8')
            #removeTag = re.sub('<.+?>', ' ', string, re.I|re.S)
            #splitString = removeTag.split()
            #print(removeTag)
        #return(text)
