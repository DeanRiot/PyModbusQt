import sys
import asyncio
import datetime
import modules.modb as modbus
import modules.TCPClient as TCPClient
from PyQt6 import QtWidgets

import modules.dateTimeProcessing as dateTimeCalc
import modules.SerialWorker as SerialWorker

from forms.main import MainFrom

TcpConnection = None


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainFormWindow = MainFrom.MainView()
    MainFormWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
