from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QRect, QSize
from ui.auto_offline.ui_offline_dialogs import Ui_Dialog
from lib.utils.JSONReader.jsonReader import JSONReader


class AutoOfflineDialogs(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMinimumSize(720,480)
        # print(self)
        '''self.nextButton.clicked.connect(self.nextButtonClicked)
        self.backToMainScreenButton.clicked.connect(self.backToMainScreen)
        
        self.oldSwNameComboBox.currentTextChanged.connect(self.onSwNameChanged)
        self.oldSwNameComboBox.currentTextChanged
        self.rejected.connect(self.onRejected)
        self.accepted.connect(self.onAccepted)

        namevar = JSONReader()
        for index, name in enumerate(namevar.nameVar["names"]):
            self.oldSwNameComboBox.addItem(name[0])
            if name[1]:
                self.oldSwNameComboBox.setCurrentText(name[0])'''

    def runDialogs(self):
        return self.exec()
    
    def dialog1(self):
        pass


    '''def onSwNameChanged(self):
        self.lineEdit.setText(self.oldSwNameComboBox.currentText())


    
    def onRejected(self):
        
        pass

    def nextButtonClicked(self):
        self.accept()
        pass

    def onAccepted(self):
        pass

    def backToMainScreen(self):
        self.reject()
        pass'''

    def resizeEvent(self, arg__1: QResizeEvent) -> None:
        self.stackedWidget.setGeometry(QRect(0, 0, self.width(), self.height()))
        self.firstDialog.setGeometry(QRect(0, 0, self.width(), self.height()))
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, self.width(), 120))
        self.widget.setGeometry(QRect(0, 120, self.width(), self.height() - 200))
        self.horizontalLayoutWidget.setGeometry(QRect(0, self.height() - 80, self.width(), 80))
        return super().resizeEvent(arg__1)
