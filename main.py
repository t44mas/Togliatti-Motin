import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        R = randint(20, 100)
        x = randint(0, self.width() - R)
        y = randint(0, self.height() - R)
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        qp.setBrush(QColor(red, green, blue))
        qp.drawEllipse(QPointF(x, y), R / 2, R / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
