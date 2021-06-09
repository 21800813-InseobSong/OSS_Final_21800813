import pyupbit

class coin:
    data = ''
    def __init__(self):
        self.data = ''

    def getList(self):
        return pyupbit.get_tickers(fiat="KRW")

    def getData(self, name):
        price = pyupbit.get_current_price(name)
        field = self.getField(name)
        data = "Current price of " + name + " : " + str(price) + "\n" + field
        return data

    def getField(self, name):
        previousPrice = pyupbit.get_ohlcv(name)
        ma5 = previousPrice['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]

        currentPrice = pyupbit.get_current_price(name)

        if currentPrice > last_ma5:
            return "It is at ascending field!"
        else:
            return "It is at descending field..."
