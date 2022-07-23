# MAIN FILE
# ///////////////////////////////////////////////////////////////
import time
import os
from pytube import YouTube
from main import MainWindow, Settings
from plyer import notification
from pypresence import Presence

cwd = os.getcwd()


def on_progress(self, vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size / 1024) / 1024
    totalsz = round(totalsz, 1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion, 2)
    self.ui.yt_logs.append(
        f"Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB"
    )
    print(
        f"Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB"
    )


# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):
    # Youtube downloader
    def downloader(self, video_link, down_dir, audio):
        try:
            tube = YouTube(video_link, on_progress_callback=on_progress)
            title = tube.title
            self.ui.yt_logs.append("Now downloading,  " + str(title))
            print("Now downloading,  " + str(title))
            video = tube.streams.filter(only_audio=audio).first()
            self.ui.yt_logs.append(
                "FileSize : " + str(round(video.filesize / (1024 * 1024))) + "MB"
            )
            print("FileSize : " + str(round(video.filesize / (1024 * 1024))) + "MB")

            if down_dir is not None:
                video.download(down_dir)
            else:
                video.download("/Users/kridsanapong/Downloads")
            print("Download complete, " + str(title))
        except Exception as e:
            print(e)
            print("ErrorDownloadVideo | " + str(video_link))

    # Notification function
    def notifyMe(self, title, message):
        notification.notify(
            title=title,
            message=message,
            timeout=10,
            app_icon=f"{cwd}/bin/Icon/iconTimer.ico",
        )

    # Discord Rich Presence
    def discordRichPresence(self, enable):
        if enable:
            try:
                rpc = Presence("902601121124728884")
                rpc.connect()

                rpc.update(  # details="Make Life Better.",
                    state="Make life better",
                    large_image="logo_new",
                    large_text="Right_posture",
                    small_image="verify",
                    small_text="Verify by right posture team",
                    buttons=[{"label": "Github", "url": "https://github.com/ussnllmn"}],
                    # party_size=[100, 100],
                    start=time.time(),
                )
                self.ui.Setting_log.append("Discord Rich Presence Connected")
                print("Discord Rich Presence Connected")
            except Exception as e:
                self.ui.Setting_log.append("Pipe Not Found - Is Discord Running?")
                print(e)

    # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
    Settings.ENABLE_CUSTOM_TITLE_BAR = True

    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """
        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }"
        )
        self.ui.scrollArea.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }"
        )
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")
