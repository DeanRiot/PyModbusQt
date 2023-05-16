import modules.receiveProcessing as receiveProcessing
import time
import asyncio

import socket

def Connect(adr, port, default_timeout:int, async_timeout:int):
    global RD_TMOUT 
    RD_TMOUT = async_timeout
    connection = socket.socket()
    connection.settimeout(default_timeout)
    connection.connect((adr, port))
    return connection


async def SendFrame(frameString, connection, out_rep):
    if connection is not None:
        try:
            await asyncio.wait_for(Send(frameString, connection), RD_TMOUT)
        except Exception as e:
            return readAs([0, 0, 0, 0], out_rep)
        time.sleep(RD_TMOUT/1000)
        data = await Receive(connection, out_rep)
        return data


async def Receive(connection, out_rep):
    if connection is not None:
        data = []
        try:
            data = await asyncio.wait_for(Recv(connection), timeout=RD_TMOUT)
            return readAs(data, out_rep)
        except Exception as e:
            return readAs([00, 00, 00, 00], out_rep)


async def Send(frameString, connection):
    connection.send(frameString)


async def Recv(conn):
    conn.setblocking(False)
    data = conn.makefile().read(-1) 
    conn.setblocking(True)
    return str.encode(data)


def readAs(dataBytes, out_rep):
    if out_rep == 'dateTime':
        return receiveProcessing.getDateTime(dataBytes)
    elif out_rep == 'Ascii':
         returnreceiveProcessing.getAscii(dataBytes)
    elif out_rep == 'hex':
        return receiveProcessing.getHex(dataBytes)
    else:
        return receiveProcessing.getHex(dataBytes)


def Close(connection):
    connection.close()

