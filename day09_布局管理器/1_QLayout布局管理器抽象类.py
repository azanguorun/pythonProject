from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        lable1=QLabel('标签1')
        lable1.setStyleSheet('background-color:red;')
        lable2=QLabel('标签2')
        lable2.setStyleSheet('background-color:green;')
        lable3=QLabel('标签3')
        lable3.setStyleSheet('background-color:blue;')
        # lable2.hide()

        timer=QTimer(self)
        timer.timeout.connect(lambda :lable1.setText(lable1.text()+'标签1\n'))
        timer.start(1000)

        # v_layout=QVBoxLayout(self)
        v_layout=QHBoxLayout(self) # 水平布局

        v_layout.addWidget(lable1)
        v_layout.addWidget(lable2)
        v_layout.addWidget(lable3)
        v_layout.setContentsMargins(0,0,0,0) # 给布局设置边距
        v_layout.setSpacing(0) # 设置间距
        self.setLayout(v_layout) # 给窗口设置布局
        self.setLayoutDirection(Qt.RightToLeft) # 设置布局方向


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())