import datetime


def calcBytes():
    return bytes(datetime.datetime.utcnow() + datetime.timedelta(hours=3))


def calcHex():
    date = (datetime.datetime.utcnow() + datetime.timedelta(hours=3)).timestamp()
    return hex(int(date))
