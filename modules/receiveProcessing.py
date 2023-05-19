import datetime

def getHex(dataBytes):
    text = ''
    for byte in dataBytes: text += hex(byte) + ' '
    return str(datetime.datetime.now()) + " << " + text


def getDateTime(dataBytes):
    data = []
    summ = ''
    for byteIndex in range(4, 8):
        data.append(dataBytes[byteIndex])
        summ += hex(dataBytes[byteIndex])[2:]
    unixDate = datetime.datetime(1970, 1, 1, 00, 00, 00)
    unixDate += datetime.timedelta(seconds=int(summ, 16), hours=3)
    result = str(unixDate)
    return str(datetime.datetime.now()) + "<< " + result


def getAscii(dataBytes):
    result = ''
    for char in dataBytes: result += chr(int(char))
    return str(datetime.datetime.now()) + "<< " + result