from PyQt6 import QtWidgets
from forms.communicaton_settings.RTUSettings.RTUSettingsDesigner import Ui_RTUSettings
import modules.SerialWorker as SerialWorker
from forms.connection_status_dialogs.connection_ok_dialog.ConnectionOkDialog import ConnectionOkDialog
from forms.connection_status_dialogs.connection_fail_dialog.ConnectionFailDialog import ConnectionFailDialog 

class RTUConnectionsForm(QtWidgets.QWidget, Ui_RTUSettings):
    def __init__(self):
        super(RTUConnectionsForm, self).__init__()
        self.setupUi(self)

        pairity = ["NONE", "ODD", "EVEN", "MARK", "SPACE"]
        data_bits = ["5", "6", "7", "8"]
        stop_bits = ["1", "2"]

        self.comboBox_4.clear()  # ports
        self.lineEdit.clear()  # speed
        self.comboBox.clear()  # pair
        self.comboBox_2.clear()  # data
        self.comboBox_3.clear()  # stop

        self.comboBox_4.insertItems(0, SerialWorker.serial_ports())
        self.lineEdit.setText('9600')
        self.comboBox.insertItems(0, pairity)
        self.comboBox_2.insertItems(0, data_bits)
        self.comboBox_3.insertItems(0, stop_bits)
        self.ConnectButton.clicked.connect(self.onRtuConnectButton)

    def setupForms(self):
        self.ConnectionFailDialog = ConnectionFailDialog()
        self.ConnectionOkDialog = ConnectionOkDialog()

    def onRtuConnectButton(self):
        try:
            SerialWorker.connect(_port=self.comboBox_4.currentText(),
                                 speed=self.lineEdit.text(),
                                 pairity=self.comboBox.currentText(),
                                 data_bits=self.comboBox_2.currentText(),
                                 stop_bits=self.comboBox_3.currentText())
            self.ConnectionOkDialog.show()
        except Exception as e:
            print(str(e))
            self.ConnectionFailDialog.show()
    