from cProfile import label

from PyQt5.Qt import *
import sys


class Lable(QLabel):
    def minimumSizeHint(self) -> 'QSize':
        return QSize(200,200)

    def sizeHint(self) -> 'QSize':
        return QSize(200,200)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        lable1 = Lable('标签1')
        lable1.setStyleSheet('background-color:red;')
        lable2 = QLabel('标签2')
        lable2.setStyleSheet('background-color:green;')
        lable3 = QLabel('标签3')
        lable3.setStyleSheet('background-color:blue;')

        layout = QVBoxLayout()
        self.setLayout(layout)  # 给窗口设置布局
        layout.addWidget(lable1)
        layout.addWidget(lable2)
        layout.addWidget(lable3)
        # layout.setStretch(0,1) # 设置控件的拉伸因子

        lable2.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())