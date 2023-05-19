import sys
from PyQt6 import QtWidgets
from forms.main import MainFrom

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainFormWindow = MainFrom.MainView()
    MainFormWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__': main()
