
from PySide6.QtWidgets import QWidget, QDialog
from ui.log_alma_screen.log_alma_screen import LogScreenWindow
from ui.auto_offline.auto_offline_dialogs import AutoOfflineDialogs





class AutoOfflineWindow(LogScreenWindow):
    def __init__(self):
        super().__init__(2)
        
        self.dialogs = AutoOfflineDialogs()
        


    def callDialog(self):
        return self.dialogs.runDialogs()
        
    

    





