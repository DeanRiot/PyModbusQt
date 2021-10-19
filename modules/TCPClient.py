import modules.receiveProcessing as receiveProcessing

import asyncio

import socket

RD_TMOUT = 0.1
RD_LEN = 512


def Connect(adr, port):
    connection = socket.socket()
    connection.connect((adr, port))
    return connection


async def SendFrame(frameString, connection, form):
    if connection is not None:
        try:
            await asyncio.wait_for(Send(frameString, connection), RD_TMOUT)
        except asyncio.TimeoutError:
            readAs([1, 0, 0, 0], form)
        except:
            readAs([1, 0, 0, 1], form)
        await Receive(connection, form)


async def Receive(connection, form):
    if connection is not None:
        data = []
        try:
            data = await asyncio.wait_for(Recv(connection, RD_LEN), timeout=RD_TMOUT)
            readAs(data, form)
        except asyncio.TimeoutError:
            readAs([00, 00, 00, 00], form)
        except:
            readAs([00, 00, 00, 00], form)


async def Send(frameString, connection):
    connection.send(frameString)


async def Recv(conn, length):
    data = conn.recv(length)
    return data


def readAs(dataBytes, form):
    ctext = form.decodeAsComboBox.currentText()
    if ctext == 'dateTime':
         text = receiveProcessing.getDateTime(dataBytes)
    elif ctext == 'Ascii':
         text = receiveProcessing.getAscii(dataBytes)
    elif ctext == 'hex':
         text = receiveProcessing.getHex(dataBytes)
    else:
        text = receiveProcessing.getHex(dataBytes)
    form.listWidget.addItem(text)


def Close(connection):
    connection.close()

