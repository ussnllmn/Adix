import os
import sqlite3
from tkinter import Button
from main import MainWindow
from modules import UIFunctions, AppFunctions


cwd = os.getcwd()


class Main_buttons(MainWindow):
    def defineButtons(self):
        button = self.ui
        button.btn_Home.clicked.connect(self.Main_button_Interface)
        button.btn_Log.clicked.connect(self.Main_button_Interface)
        button.btn_Setting.clicked.connect(self.Main_button_Interface)
        button.btn_Logout.clicked.connect(self.Main_button_Interface)
        button.btn_save_setting.clicked.connect(self.Main_button_Interface)
        button.btn_test_notify.clicked.connect(self.Main_button_Interface)
        button.btn_test_email.clicked.connect(self.Main_button_Interface)
        button.btn_open_file.clicked.connect(self.Main_button_Interface)
        button.yt_download.clicked.connect(self.Main_button_Interface)

    def buttonClick(self):
        button = self.ui
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_Logout":
            self.Logout()

        if btnName == "btn_Home":
            button.stackedWidget.setCurrentWidget(button.Home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_Log":
            button.stackedWidget.setCurrentWidget(button.Log)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_Setting":
            button.stackedWidget.setCurrentWidget(button.Setting)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_test_notify":
            try:
                AppFunctions.notifyMe(
                    self, "Test notify", "Notification work correctly"
                )
                self.ui.Setting_log.append(f"Notification work correctly")
            except Exception as e:
                print(e)
                self.ui.Setting_log.append(f"Fail to notify unknown error.\n{str(e)}")

        if btnName == "yt_download":
            AppFunctions.downloader(
                self,
                self.ui.yt_url.text(),
                None,
                self.ui.yt_audio.isChecked(),
            )
        # PRINT BTN NAME
        # print(f'Button "{btnName}" pressed!')

    def set_custom_theme(self, enable):
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = enable
        themeFile = "bin\themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.ui.btn_Home.setStyleSheet(
            UIFunctions.selectMenu(self.ui.btn_Home.styleSheet())
        )
