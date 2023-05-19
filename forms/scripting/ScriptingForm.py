from PyQt6 import QtWidgets
from forms.scripting.ScriptingFormDesigner import Ui_ScriptingForm
from controller.sender import FrameSender
from forms.comand_systems.ChoiseComand.ChoiseComandForm import ChoiseComandForm
import asyncio

class ScriptingForm(QtWidgets.QWidget, Ui_ScriptingForm):
    def __init__(self,f_sender:FrameSender):
        super(ScriptingForm, self).__init__()
        self.setupUi(self)
        self.setupCallbacks()
        self.f_sender = f_sender
        
    def setupCallbacks(self):
        self.AddCommandButton.clicked.connect(self.onAddCommandButtonClick)
        self.ClearScriptButton.clicked.connect(self.onClearScriptButtonClick)
        self.ClearOutputButton.clicked.connect(self.onClearOutputButtonClick)
        self.RunScriptButton.clicked.connect(self.onRunScriptButtonClick)
        self.CmdSystemShowButton.clicked.connect(self.onCmdSystemShowButtonClick)
        self.DeleteSelectedButton.clicked.connect(self.onDeleteSelectedButtonClick)

    def onAddCommandButtonClick(self):
      self.ScriptListView.addItem(self.FrameInput.text())

    def onClearScriptButtonClick(self):
        self.ScriptListView.clear()

    def onClearOutputButtonClick(self):
        self.OutputListView.clear()

    def onDeleteSelectedButtonClick(self):
        selected = self.ScriptListView.selectedIndexes()
        if len(selected)!=0 :
            self.ScriptListView.takeItem(selected[0].row())   

    def onRunScriptButtonClick(self):
        for i in range(self.ScriptListView.count()):
           data = self.sendFrame(self.ScriptListView.item(i).text())
           if not data.status: return
           self.OutputListView.addItem(data.request)
           self.OutputListView.addItem(data.response)
           self.OutputListView.addItem('_'*32)

    def sendFrame(self, text):
        frameData = text
        out_repr = 'hex'
        return self.f_sender.sendAndReceive(frameData, out_repr) 
    
    def onCmdSystemShowButtonClick(self):
        global form
        form = ChoiseComandForm()
        form.show()