from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from melody_generate import *
import sys
import webbrowser
import pygame

pygame.init()
pygame.mixer.init()
sounda = pygame.mixer.Sound("./music/BackGround_Music/Background_music16s.wav")
sounda.play()


# CURRENT_DIR = os.path.dirname(os.path.realpath
#                               ("./music/BackGround_Music/BackgroundMusic1.wav"))
# filename = os.path.join(CURRENT_DIR, 'BackgroundMusic1.wav')
# QtMultimedia.QSound.play(filename)


class SubWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SubWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("MuseLab")
        self.setFixedWidth(1159)
        self.setFixedHeight(700)
        self.center()
        self.UiComponents()
        self.setStyleSheet("background-image: url(./image/melody_generate.jpg);")
        app_icon = QIcon("./image/muselab_icon.jpg")
        self.setWindowIcon(app_icon)

        self.show()
        self.string = ""  # passed string from MainWindow

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def UiComponents(self):
        button1 = QPushButton("Re-Orchestrate", self)
        button1.setGeometry(460, 225, 250, 50)
        button1.setFixedWidth(250)
        button1.setFixedHeight(50)
        font = QtGui.QFont()
        font.setFamily("Orange LET")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(75)
        button1.setFont(font)
        # button1.setStyleSheet("color: rgb(255, 255, 255);")
        button1.setStyleSheet(
            "background-color: transparent; border: 0px; color: rgb(255, 255, 255);")
        button1.clicked.connect(self.ChordState)
        button2 = QPushButton("Own Creation", self)
        button2.setGeometry(460, 300, 250, 50)
        button2.setFixedWidth(250)
        button2.setFixedHeight(50)
        font = QtGui.QFont()
        font.setFamily("Orange LET")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(75)
        button2.setFont(font)
        # button2.setStyleSheet("color: rgb(255, 255, 255);")
        button2.setStyleSheet(
            "background-color: transparent; border: 0px; color: rgb(255, 255, 255);")
        button2.clicked.connect(self.LabState)

        button3 = QPushButton("Go Back", self)
        button3.setGeometry(460, 375, 250, 50)
        # button3.setIcon(QIcon("./image/return-icon2.jpg"))
        button3.setFixedWidth(250)
        button3.setFixedHeight(50)
        font = QtGui.QFont()
        font.setFamily("Orange LET")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(75)
        button3.setFont(font)
        button3.clicked.connect(self.Return)

    def ChordState(self):
        print("Viewing Chords")
        fp = self.string
        MuseScore = melody_generate(fp)
        self.sub = Retry_tip()
        self.sub.show()
        if MuseScore == 0:
            self.sub1 = MuseScore_tip()
            self.sub1.show()

    def LabState(self):
        msg = QMessageBox()
        msg.setStyleSheet("QLabel{min-width: 300px;}")
        msg.setWindowTitle("Testing")
        msg.setText("To Be Continue....")
        print(self.string)
        msg.setInformativeText("To Be Continue......")
        msg.exec_()

    def Return(self):
        mainWindows.show()
        self.close()


class MuseScore_tip(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MuseScore_tip, self).__init__(*args, **kwargs)
        self.setWindowTitle("Show Score Error")
        self.setFixedWidth(530)
        self.setFixedHeight(250)
        self.up_center()
        self.setStyleSheet("background-image: url(./image/Dialog_Background_1.jpg);")
        app_icon = QIcon("./image/muselab_icon.jpg")
        self.setWindowIcon(app_icon)
        self.UiComponents()
        self.show()

    def up_center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def UiComponents(self):
        label1 = QLabel("Can't show the new music Score", self)
        label2 = QLabel("Make sure you have MuseScore3", self)
        label1.setFixedHeight(30)
        label1.setFixedWidth(335)
        label2.setFixedHeight(30)
        label2.setFixedWidth(500)
        label1.move(99, 40)
        label1.setAlignment(QtCore.Qt.AlignCenter)
        label1.setAlignment(QtCore.Qt.AlignVCenter)
        label2.move(95, 120)
        label2.setAlignment(QtCore.Qt.AlignCenter)
        label2.setAlignment(QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(23)
        font.setBold(True)
        font.setWeight(75)
        label1.setFont(font)
        label2.setFont(font)
        label1.setStyleSheet("color: rgb(255, 255, 255);")
        label2.setStyleSheet("color: rgb(255, 255, 255);")

        button1 = QPushButton("Download", self)
        button1.setGeometry(90, 200, 170, 35)
        button1.setFixedWidth(150)
        button1.setFixedHeight(35)
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        button1.setFont(font)
        button1.setStyleSheet("color: rgb(255, 255, 255);")
        button1.clicked.connect(self.MuseScore_website)

        button2 = QPushButton("Ok", self)
        button2.setGeometry(295, 200, 170, 35)
        button2.setFixedWidth(150)
        button2.setFixedHeight(35)
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        button2.setFont(font)
        button2.setStyleSheet("color: rgb(255, 255, 255);")
        button2.clicked.connect(self.CloseState)

    def MuseScore_website(self):
        webbrowser.open('https://musescore.org/zh-hans')

    def CloseState(self):
        self.close()


class Retry_tip(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Retry_tip, self).__init__(*args, **kwargs)
        self.setWindowTitle("Re-orchestration Completed")
        self.setFixedWidth(520)
        self.setFixedHeight(250)
        self.center()
        self.setStyleSheet("background-image: url(./image/Dialog_Background_1.jpg);")
        app_icon = QIcon("./image/muselab_icon.jpg")
        self.setWindowIcon(app_icon)
        self.UiComponents()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def UiComponents(self):
        label1 = QLabel("Re-orchestration completed!", self)
        label2 = QLabel("Test it in the music/Output file!", self)
        label1.setFixedHeight(30)
        label1.setFixedWidth(335)
        label2.setFixedHeight(30)
        label2.setFixedWidth(400)
        label1.move(99, 40)
        label1.setAlignment(QtCore.Qt.AlignCenter)
        label2.move(75, 120)
        label2.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPixelSize(23)
        font.setBold(True)
        font.setWeight(75)
        label1.setFont(font)
        label2.setFont(font)
        label1.setStyleSheet("color: rgb(255, 255, 255);")
        label2.setStyleSheet("color: rgb(255, 255, 255);")

        button2 = QPushButton("Ok", self)
        button2.setGeometry(207, 200, 170, 35)
        button2.setFixedWidth(100)
        button2.setFixedHeight(35)
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        button2.setFont(font)
        button2.setStyleSheet("color: rgb(255, 255, 255);")
        button2.clicked.connect(self.CloseState)

    def CloseState(self):
        self.close()


class HelpScreen(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(HelpScreen, self).__init__(*args, **kwargs)

        self.setWindowTitle("How to use the program")
        self.setFixedWidth(520)
        self.setFixedHeight(250)
        self.center()
        self.setStyleSheet("background-image: url(./image/Dialog_Background_1.jpg);")
        app_icon = QIcon("./image/muselab_icon.jpg")
        self.setWindowIcon(app_icon)
        self.UiComponents()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def UiComponents(self):
        self.label = QLabel("1. Provide a MIDI File to MuseLab", self)
        self.label2 = QLabel("2. Select the Music Style You Want", self)
        self.label3 = QLabel("3. Enjoy Your Music Journey!", self)
        self.label.setFixedWidth(335)
        self.label.setFixedHeight(30)
        self.label2.setFixedWidth(335)
        self.label2.setFixedHeight(30)
        self.label3.setFixedWidth(335)
        self.label3.setFixedHeight(30)
        self.label.move(90, 30)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.move(90, 90)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.move(90, 150)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label2.setFont(font)
        self.label3.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label3.setStyleSheet("color: rgb(255, 255, 255);")

        button1 = QPushButton("OK", self)
        button1.setGeometry(207, 200, 170, 35)
        button1.setFixedWidth(100)
        button1.setFixedHeight(35)
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        button1.setFont(font)
        button1.setStyleSheet("color: rgb(255, 255, 255);")
        button1.clicked.connect(self.CloseWindow)

    def CloseWindow(self):
        self.close()


def CloseMainWindow():
    sys.exit()


class Ui_Exit_Dialog(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Ui_Exit_Dialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Closing")
        self.setFixedWidth(530)
        self.setFixedHeight(250)
        self.center()
        self.setStyleSheet("background-image: url(./image/Dialog_Background_1.jpg);")
        app_icon = QIcon("./image/muselab_icon.jpg")
        self.setWindowIcon(app_icon)
        self.UiComponents()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def UiComponents(self):
        label = QLabel(" Do you really want to close this window?", self)
        label.setGeometry(30, 50, 475, 27)
        font = QtGui.QFont()
        font.setPixelSize(22)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        label.setStyleSheet("color: rgb(255, 255, 255);")

        button1 = QPushButton("YES", self)
        button1.setGeometry(60, 150, 170, 35)
        button1.setFixedWidth(170)
        button1.setFixedHeight(35)
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        button1.setFont(font)
        button1.setStyleSheet("color: rgb(255, 255, 255);")
        button1.clicked.connect(CloseMainWindow)

        button2 = QPushButton("No", self)
        button2.setGeometry(300, 150, 170, 35)
        button2.setFixedWidth(170)
        button2.setFixedHeight(35)
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        button2.setFont(font)
        button2.setStyleSheet("color: rgb(255, 255, 255);")
        button2.clicked.connect(self.CloseState)

    def CloseState(self):
        self.close()


def Website():
    webbrowser.open('https://prescottlai.wixsite.com/website-1/contact')


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MuseLab")
        MainWindow.resize(1125, 748)
        MainWindow.setMaximumSize(QtCore.QSize(1125, 748))
        MainWindow.setStyleSheet("background-image: url(./image/music.jpg);")
        # originally it is :/music.jpg, but it is wrong with“ ：”， should be "."
        app_icon = QIcon("./image/muselab_icon.jpg")
        MainWindow.setWindowIcon(app_icon)
        self.center()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectFile = QtWidgets.QPushButton(self.centralwidget)
        self.selectFile.setGeometry(QtCore.QRect(470, 270, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPixelSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.selectFile.setFont(font)
        self.selectFile.setStyleSheet("color:rgb(255, 170, 0); background-color: rgb(229, 251, 255)")
        self.selectFile.setObjectName("selectFile")
        self.selectFile.setToolTip("Click and Open the file dialog")
        self.welcomeSentence = QtWidgets.QLabel(self.centralwidget)
        self.welcomeSentence.setGeometry(QtCore.QRect(320, 150, 511, 41))
        # self.welcomeSentence = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Pyunji R")
        font.setPixelSize(28)
        self.welcomeSentence.setFont(font)
        self.welcomeSentence.setAutoFillBackground(False)
        self.welcomeSentence.setStyleSheet("color: #ef9072; border: rgb(255, 255, 255)")
        self.welcomeSentence.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeSentence.setObjectName("welcomeSentence")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 26))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("color:white")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRecent = QtWidgets.QMenu(self.menuFile)
        self.menuRecent.setObjectName("menuRecent")
        self.menuImport = QtWidgets.QMenu(self.menuFile)
        self.menuImport.setObjectName("menuImport")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuProperties = QtWidgets.QMenu(self.menubar)
        self.menuProperties.setObjectName("menuProperties")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewProject = QtWidgets.QAction(MainWindow)
        self.actionNewProject.setEnabled(True)
        self.actionNewProject.setObjectName("actionNewProject")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actionOpenFIle = QtWidgets.QAction(MainWindow)
        self.actionOpenFIle.setCheckable(True)
        self.actionOpenFIle.setEnabled(False)
        font = QtGui.QFont()
        self.actionOpenFIle.setFont(font)
        self.actionOpenFIle.setObjectName("actionOpenFIle")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionMIDI_File = QtWidgets.QAction(MainWindow)
        self.actionMIDI_File.setObjectName("actionMIDI_File")
        self.actionMuseLab_File = QtWidgets.QAction(MainWindow)
        self.actionMuseLab_File.setObjectName("actionMuseLab_File")
        self.actionProperties = QtWidgets.QAction(MainWindow)
        self.actionProperties.setObjectName("actionProperties")
        self.actionWindow_SIze = QtWidgets.QAction(MainWindow)
        self.actionWindow_SIze.setObjectName("actionWindow_SIze")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionMaximize = QtWidgets.QAction(MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionMinimize_2 = QtWidgets.QAction(MainWindow)
        self.actionMinimize_2.setObjectName("actionMinimize_2")
        self.actionMaximize_2 = QtWidgets.QAction(MainWindow)
        self.actionMaximize_2.setObjectName("actionMaximize_2")
        self.actionContact_Us = QtWidgets.QAction(MainWindow)
        self.actionContact_Us.setObjectName("actionContact_Us")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuRecent.addAction(self.action_2)
        self.menuImport.addAction(self.actionMIDI_File)
        self.menuImport.addAction(self.actionMuseLab_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNewProject)
        self.menuFile.addAction(self.menuRecent.menuAction())
        self.menuFile.addAction(self.actionOpenFIle)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuSetting.addAction(self.actionProperties)
        self.menuSetting.addAction(self.actionWindow_SIze)
        self.menuHelp.addAction(self.actionContact_Us)
        self.menuHelp.addAction(self.actionHelp)
        self.menuProperties.addAction(self.actionMinimize_2)
        self.menuProperties.addAction(self.actionMaximize_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuProperties.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.selectFile.clicked.connect(self.buttonClicked)
        # self.actionClose.triggered.connect(MainWindow.close)
        self.actionClose.triggered.connect(self.closeState)
        self.actionHelp.triggered.connect(self.HelpScreen)
        self.actionContact_Us.triggered.connect(Website)
        # self.actionNewProject.triggered.connect(MainWindow.buttonClicked)
        # self.actionMinimize.triggered.connect(MainWindow.showMinimized)
        # self.actionMaximize.triggered.connect(MainWindow.showMaximized)
        # self.actionProperties.triggered.connect(MainWindow.buttonClicked)
        # self.actionOpenFIle.triggered.connect(MainWindow.buttonClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # PLAY BACKGROUND MUSIC

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeState(self):
        print("close for sure?")
        self.sub = Ui_Exit_Dialog()
        self.sub.show()

    def HelpScreen(self):
        self.sub = HelpScreen()
        self.sub.show()
        # self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MuseLab"))
        self.selectFile.setText(_translate("MainWindow", "Select MIDI File"))
        self.welcomeSentence.setText(_translate("MainWindow", "Welcome  To  The  MuseLab"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRecent.setTitle(_translate("MainWindow", "Recent"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuProperties.setTitle(_translate("MainWindow", "Window"))
        self.actionNewProject.setText(_translate("MainWindow", "New Project"))
        self.action_2.setText(_translate("MainWindow", "......"))
        self.actionOpenFIle.setText(_translate("MainWindow", "Open File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Esc"))
        self.actionMIDI_File.setText(_translate("MainWindow", "MIDI File"))
        self.actionMuseLab_File.setText(_translate("MainWindow", "MuseLab File"))
        self.actionProperties.setText(_translate("MainWindow", "Properties"))
        self.actionWindow_SIze.setText(_translate("MainWindow", "Window SIze"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        self.actionMinimize_2.setText(_translate("MainWindow", "Minimize"))
        self.actionMaximize_2.setText(_translate("MainWindow", "Maximize"))
        self.actionContact_Us.setText(_translate("MainWindow", "Contact Us"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))

    def buttonClicked(self):
        # print("Button pressed!")
        self.open_dialog_box()

    def open_dialog_box(self):
        Filename = QFileDialog.getOpenFileName()
        path = Filename[0]
        test_path = path.lower()
        if test_path.endswith(".mid") is False and path != "":  # invalid file input
            errormsg = QMessageBox()
            errormsg.setStyleSheet("QLabel{min-width: 300px;}")
            errormsg.setWindowTitle("Invalid File!")
            errormsg.setText("Error")
            errormsg.setInformativeText('Requires MIDI file as input!')
            errormsg.exec_()

        elif test_path.endswith(".mid"):  # correct input
            fp = path
            print(fp)
            self.sub = SubWindow()
            self.sub.string = path  # passes the string to new window
            # self.sub.show()
            mainWindows.hide()


if __name__ == '__main__':
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont(os.path.dirname(__file__) + "/Font/Segoe Script.ttf")
    QFontDatabase.addApplicationFont(os.path.dirname(__file__) + "/Font/Pyunji R.ttf")
    QFontDatabase.addApplicationFont(os.path.dirname(__file__) + "/Font/Orange LET.ttf")
    mainWindows = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindows)
    # sound_file = "./music/BackGround_Music/Background_music16s.wav"
    # winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
    mainWindows.show()
    database = QFontDatabase()
    # Checking the Font database. Debug
    for f in database.families():
        if f == "Segoe Script" or f == "Pyunji R" or f == "Orange LET":
            print(f)

sys.exit(app.exec_())
