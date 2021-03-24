# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from UI_Design import *
from PyQt5 import QtMultimedia

CURRENT_DIR = os.path.dirname(os.path.realpath
                              ("./music/BackGround_Music/BackgroundMusic1.wav"))
filename = os.path.join(CURRENT_DIR, 'BackgroundMusic1.wav')
QtMultimedia.QSound.play(filename)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.show()

sys.exit(app.exec_())
