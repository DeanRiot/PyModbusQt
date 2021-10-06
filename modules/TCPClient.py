import socket


def Connect(adr, port):
    connection = socket.socket()
    connection.connect((adr, port))
    return connection


def Send(frameString, connection):
    connection.send(frameString)


def Receive(connection, bytesLen):
    data = connection.recv(bytesLen)
    return data


def Close(connection):
    connection.close()
