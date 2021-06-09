import datetime

class schedule:
    todaySchedule = ""
    count = 0
    def __init__(self):
        self.todaySchedule = "No schedule!"
        self.count = 0

    def getSchedule(self):
        return self.todaySchedule

    def setSchedule(self, data):
        if self.count == 0:
            self.todaySchedule = data
            self.count += 1
        else:
            self.todaySchedule = self.todaySchedule + "\n" + data
            self.count += 1
