import modules.SerialWorker as SERIAL
from modules.TCPClient import TCPClient
from modules.modb import Modbus
from type.IO_data import IO_DATA
import asyncio 
import datetime

class FrameSender(object):
    def __init__(self, connection:TCPClient) -> None:
        self.modbus = Modbus()
        self.connection = connection

    def setSerial(self):
        pass

    def setTCP(self, connection:TCPClient):
        self.connection = connection

    def sendAndReceive(self, frame_data:str, out_repr:str)->IO_DATA:
        response = ''
        data_bytes = self.___getDataBytes___(frame_data)

        if SERIAL.ser is not None and SERIAL.isConnected():
            isConnectionEstablished = True
            response = asyncio.run(SERIAL.writeSerial(data_bytes, out_repr))

        if self.connection is not None :
            isConnectionEstablished = True
            response = self.connection.SendFrame(data_bytes, out_repr)

        req_hex = self.___getHexRepr___(frame_data)
        data = IO_DATA(req_hex, response, isConnectionEstablished)
        return data
    
    def ___getDataBytes___(self,frame_data:str):
        frame = self.modbus.createFrame(frame_data)
        return bytes(frame)
    
    def ___getHexRepr___(self,frame_data:str):
        converted_frame = str(datetime.datetime.now()) + " >> "
        frame = self.modbus.createFrame(frame_data)
        for byte in frame: converted_frame += hex(byte) + " "
        return converted_frame

    