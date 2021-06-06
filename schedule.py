import datetime

class timetable:
    mondayTable = ""
    tuesdayTable = ""
    wednesdayTable = ""
    thursdayTable = ""
    fridayTable = ""
    count = [0, 0, 0, 0, 0]
    def __init__(self):
        self.mondayTable = "No schedule!"
        self.tuesdayTable = "No schedule!"
        self.wednesdayTable = "No schedule!"
        self.thursdayTable = "No schedule!"
        self.fridayTable = "No schedule!"
        count = [0, 0, 0, 0, 0]

    def setMonday(self, time, monday):
        monTable = time + " " + monday + "\n"
        if self.count[0] == 0:
            self.mondayTable = monTable
            self.count[0] += 1
        else:
            self.self.mondayTable += monTable
            count[0] += 1

    def setTuesday(self, time, tuesday):
        tuesTable = time + " " + tuesday +"\n"
        if self.count[1] == 0:
            self.tuesdayTable = tuesTable
            self.count[1] += 1
        else:
            self.tusedayTable += tuesTable
            self.count[1] += 1

    def setWednesday(self, time, wednesday):
        wednesTable = time + " " + wednesday + "\n"
        if self.count[2] == 0:
            self.wednesdayTable = wednesTable
            self.count[2] += 1
        else:
            self.wednesdayTable += wednesTable
            self.count[2] += 1

    def setThursday(self, time, thursday):
        thursTable = time + " " + thursday + "\n"
        if self.count[3] == 0:
            self.thursdayTable = thursTable
            self.count[3] += 1
        else:
            self.thursdayTable += thursTable
            self.count[3] += 1

    def setFriday(self, time, friday):
        friTable = time + " " + friday + "\n"
        if self.count[4] == 0:
            self.fridayTable = friTable
            self.count[4] += 1
        else:
            self.fridayTable = friTable
            self.count[4] += 1

    def getTable(self):
        table = "\n" + self.mondayTable + "\n" + self.tuesdayTable + "\n" + \
                self.wednesdayTable + "\n" + self.thursdayTable + "\n" + \
                self.fridayTable

        return table

    def getDayTable(self, day):
        lowerDay = day.lower()
        if lowerDay  == 'monday':
            return self.mondayTable
        elif lowerDay == 'tuesday':
            return self.tuesdayTable
        elif lowerDay == 'wednesday':
            return self.wednesdayTable
        elif lowerDay == 'thursday':
            return self.thursdayTable
        elif lowerDay == 'friday':
            return self.fridayTable
        else:
            return 'No schedule!'
