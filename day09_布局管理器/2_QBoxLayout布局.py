from cProfile import label

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()

    def setup_ui(self):
        lable1 = QLabel('标签1')
        lable1.setStyleSheet('background-color:red;')
        lable2 = QLabel('标签2')
        lable2.setStyleSheet('background-color:green;')
        lable3 = QLabel('标签3')
        lable3.setStyleSheet('background-color:blue;')
        lable4 = QLabel('标签4')
        lable4.setStyleSheet('background-color:yellow;')


        layout = QVBoxLayout(self)
        self.setLayout(layout)
        layout.addWidget(lable1)
        layout.addWidget(lable2)
        layout.addWidget(lable3)
        layout.setSpacing(10) # 设置间距
        # layout.setContentsMargins(100, 100, 100, 100) # 给布局设置边距
        print(layout.contentsMargins().left())

        # layout.replaceWidget(lable2, lable4) # 替换控件
        lable2.destroyed.connect(lambda :print('标签2被释放了'))  # 控件被释放

        lable5 = QLabel('标签5')
        lable5.setStyleSheet('background-color:cyan;')
        lable6 = QLabel('标签6')
        lable6.setStyleSheet('background-color:gray;')
        label7 = QLabel('标签7')
        label7.setStyleSheet('background-color:magenta;')

        h_layout = QBoxLayout(QBoxLayout.LeftToRight)
        h_layout.addWidget(lable5)
        h_layout.addWidget(lable6)
        h_layout.addWidget(label7)

        layout.addWidget(lable1)
        layout.addLayout(h_layout)
        layout.addWidget(lable2)
        layout.addWidget(lable3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())