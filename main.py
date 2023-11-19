import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi('UI.ui', self)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())