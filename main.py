import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget,\
    QGraphicsEllipseItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5 import uic
import random


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

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def create_random_circle(self):
        diameter = random.randint(20, 100)
        color = QColor(Qt.yellow)

        circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        circle.setBrush(color)
        self.scene.addItem(circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
