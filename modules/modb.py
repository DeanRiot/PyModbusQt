import modules.crc16 as crc


def createFrame(modbFrame):
    data = []
    pdu = ''
    for sym in modbFrame:
        data.append(int(sym.encode('ascii')))
        pdu = pdu + chr(int(sym))
    crcSumm = crc.calcString(pdu)
    crcs1 = int(hex(ord(crcSumm[0])), base=16)
    crcs2 = int(hex(ord(crcSumm[1])), base=16)
    data.append(crcs1)
    data.append(crcs2)
    return data


def createStringFrame(byteFrame):
    frame = ''
    for char in byteFrame:
        frame = frame + char
    return frame


def decodeChar(dataString):
    byteArr = []
    for char in dataString:
        data = hex(int(ord(char)))
        byteArr.append(data)
    return byteArr


def parseFrame(stringFrame):
    data = stringFrame.split()
    return data


def parseHexFrame(stringFrame):
    data = parseFrame(stringFrame)
    intData = []
    for cr in data:
        intData.append(str(int(cr, base=16)))
    return intData
