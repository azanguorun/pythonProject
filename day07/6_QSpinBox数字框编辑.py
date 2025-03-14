from PyQt5.Qt import *
import sys

class SB(QSpinBox):
    def textFromValue(self, v):
        return str(v) + "岁"


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()

    def setup_ui(self):
        sb=SB(self) #数字框  默认0-99
        sb.resize(100,30)
        sb.move(100,100)
        sb.valueChanged[str].connect(lambda val:print("值改变了",val))
        self.sb=sb

        btn=QPushButton(self)
        btn.setText("测试按钮")
        btn.move(100,150)
        btn.clicked.connect(lambda :self.显示的进制设置())


    def 设置以及获取数值(self):
        self.sb.setValue(10) #设置值
        print(self.sb.value()) #获取值
        print(self.sb.text()) #获取文本

    def 显示的进制设置(self):
        self.sb.setDisplayIntegerBase(8) #设置显示的进制
        self.sb.setRange(0,6) #设置范围

    def 前缀和后缀(self):
        self.sb.setRange(0,6)
        self.sb.setPrefix("周") #设置前缀
        self.sb.setSuffix("天") #设置后缀
        self.sb.setSpecialValueText("周日") #设置特殊值的文本

    def 步长设置(self):
        self.sb.setSingleStep(3) #设置步长

    def 数值循环(self):
        self.sb.setWrapping(True) #循环

    def 最大值最小值(self):
        self.sb.setMinimum(10) #设置最小值
        self.sb.setMaximum(100) #设置最大值
        self.sb.setRange(10,100) #设置范围
        self.sb.setSingleStep(2) #设置步长


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())