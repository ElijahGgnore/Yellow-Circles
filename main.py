import sys
from random import randint

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget

from CirclesUI import Ui_Circles


def random_color():
    return QColor(randint(0, 255), randint(0, 255), randint(0, 255))


class Circles(QWidget, Ui_Circles):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.draw = False
        self.draw_circles.pressed.connect(self.draw_circles_pressed)

    def paintEvent(self, a0):
        if self.draw:
            painter = QPainter(self)
            for _ in range(randint(1, 10)):
                painter.setBrush(random_color())
                radius = randint(20, 100)
                pos = QPoint(randint(radius, self.width() - radius), randint(radius, self.height() - radius))
                painter.drawEllipse(pos, radius, radius)
        self.draw = False

    def draw_circles_pressed(self):
        self.draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Circles()
    w.show()
    sys.exit(app.exec_())
