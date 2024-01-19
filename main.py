#########################
# this is the main file #
#########################

from PySide6 import QtWidgets
from ui.main_screen.main_screen_window import mainScreenWindow

import sys

app = QtWidgets.QApplication(sys.argv)

ui = mainScreenWindow()

ui.show()
app.exec()
