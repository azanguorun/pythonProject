from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        sl=QStackedLayout(self)
        self.setLayout(sl)  # 给窗口设置布局
        lable1=QLabel('标签1')
        lable1.setStyleSheet('background-color:red;')
        lable2=QLabel('标签2')
        lable2.setStyleSheet('background-color:green;')
        lable3=QLabel('标签3')
        lable3.setStyleSheet('background-color:blue;')


        sl.addWidget(lable1)
        sl.addWidget(lable2)
        sl.addWidget(lable3)
        # sl.setCurrentIndex(2) # 设置当前显示的控件
        # lable1.hide()
        # sl.removeWidget(lable1) # 移除控件
        timer=QTimer(self)
        timer.timeout.connect(lambda :sl.setCurrentIndex((sl.currentIndex()+1)%3))
        timer.start(1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())