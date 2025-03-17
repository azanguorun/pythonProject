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

        #创建布局管理器对象
        layout = QBoxLayout(QBoxLayout.LeftToRight) # 水平布局

        #把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)   # 给窗口设置布局

        #添加需要布局的子控件到布局管理器中
        layout.addWidget(lable1, stretch=1) # stretch 拉伸因子
        # layout.addSpacing(10) # 添加间隔
        layout.addStretch(2)
        layout.addWidget(lable2, stretch=1)
        layout.addWidget(lable3, stretch=1)
        layout.addWidget(lable4, stretch=1)
        layout.insertSpacing(3, 20) # 添加空白
        # layout.insertWidget(0, lable4) # 插入控件

        layout.setStretchFactor(lable3,1) # 设置拉伸因子2

        timer = QTimer(self)
        def test():
            #layout.direction()  是枚举值 1 2 3 4
            layout.setDirection((layout.direction()+1)%4) # 布局方向
        timer.timeout.connect(test)
        timer.start(1000)

        lable5 = QLabel('标签5')
        lable5.setStyleSheet('background-color:cyan;')
        lable6 = QLabel('标签6')
        lable6.setStyleSheet('background-color:gray;')
        label7 = QLabel('标签7')
        label7.setStyleSheet('background-color:magenta;')

        h_layout = QBoxLayout(QBoxLayout.TopToBottom)
        h_layout.addWidget(lable5)
        h_layout.addWidget(lable6)
        h_layout.addWidget(label7)
        layout.insertLayout(2, h_layout) # 插入布局

        # layout.removeWidget(lable2) # 移除控件
        # lable2.setParent(None) # 移除布局


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())