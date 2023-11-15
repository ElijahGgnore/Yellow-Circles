import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget

ui_file = 'UI.ui'


class YellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.draw = False
        self.draw_circles.pressed.connect(self.draw_circles_pressed)

    def paintEvent(self, a0):
        if self.draw:
            painter = QPainter(self)
            for _ in range(randint(1, 10)):
                painter.setBrush(Qt.yellow)
                radius = randint(20, 100)
                pos = QPoint(randint(radius, self.width() - radius), randint(radius, self.height() - radius))
                painter.drawEllipse(pos, radius, radius)
        self.draw = False

    def draw_circles_pressed(self):
        self.draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = YellowCircles()
    w.show()
    sys.exit(app.exec_())
