from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        p=QProgressBar(self)
        p.move(100,100)
        p.resize(200,10)
        p.setRange(0,100) #设置范围
        p.setValue(50) #设置值
        print(p.maximum())
        print(p.minimum())
        p.setFormat('完成：%p%  总共：%m%' ) #设置格式

        btn=QPushButton(self)
        btn.setText('测试按钮')
        btn.move(100,350)
        btn.clicked.connect(lambda :p.reset()) #步进

        timer=QTimer(p)
        def time_out():
            if p.value()>=p.maximum():
                timer.stop()
            p.setValue(p.value()+1)
        timer.timeout.connect(time_out)
        timer.start(100)

        p.valueChanged.connect(lambda val:print('当前进度：',val)) #值改变信号



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())