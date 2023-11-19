import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsView, QGraphicsScene, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi('UI.ui', self)

        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.create_random_circle)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.view.setAlignment(Qt.AlignTop)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())