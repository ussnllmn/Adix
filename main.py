import sys
import os

from modules import *
from widgets import *

from PySide6.QtWidgets import QApplication

from modules.app_temp import version

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

version.thisVersion = "1.2.1.3"
# /////////////////////////////////////////////
counter = 0
CircularProgress_timer = 300
# /////////////////////////////////////////////


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        UIFunctions.Function_Main_Setup(self)
        Main_buttons.defineButtons(self)
        self.show()
        Main_buttons.set_custom_theme(self, False)

    # UPDATE PROGRESS BAR
    def update(self):
        global counter
        self.progress.set_value(counter)
        if counter >= 100:
            print("counter")
        else:
            counter += 1

    # BUTTONS INTERFACE TO app_button_main
    def Main_button_Interface(self):
        Main_buttons.buttonClick(self)

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

    def Logout(self):
        print("logout")


def set_counter(value):
    global counter
    counter = value


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    windows = MainWindow()
    sys.exit(app.exec())
