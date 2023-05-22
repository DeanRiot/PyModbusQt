import modules.receiveProcessing as receiveProcessing
import time
import asyncio

import socket
class TCPClient(object):
    def __init__(self):
        self.connection = None
    
    def Connect(self, adr, port, default_timeout:int, async_timeout:int):
        self.RD_TMOUT = async_timeout/1000
        self.connection = socket.socket()
        self.connection.settimeout(default_timeout)
        self.connection.connect((adr, port))

    def SendFrame(self, frameString, out_rep):
        if self.connection is not None:
            try:
                self.Send(frameString)
                time.sleep(self.RD_TMOUT)
                data = self.Receive(out_rep)
            except Exception as e:
                print(str(e))
                return self.readAs([0, 0, 0, 0], out_rep)
            return data
    
    def Receive(self, out_rep):
        if self.connection is not None:
            data = []
            try:
                data = self.Recv()
                print(data)
                return self.readAs(data, out_rep)
            except Exception as e:
                print(str(e))
                return self.readAs([00, 00, 00, 00], out_rep)

    def Send(self,frameString):
        self.connection.send(frameString)

    def Recv(self):
        self.connection.setblocking(False)
        data = self.connection.makefile('rb', encoding='utf-8').read(-1)
        print(data)
        self.connection.setblocking(True)
        return data

    def readAs(self,dataBytes, out_rep):
        if out_rep == 'dateTime':
            return receiveProcessing.getDateTime(dataBytes)
        elif out_rep == 'Ascii':
            return receiveProcessing.getAscii(dataBytes)
        elif out_rep == 'hex':
            return receiveProcessing.getHex(dataBytes)
        else:
            return receiveProcessing.getHex(dataBytes)
        
    def Close(self,connection):
        connection.close()

