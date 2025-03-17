from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def setup_ui(self):
        LCD=QLCDNumber(8,self) #数字位数
        LCD.move(100,100)
        LCD.resize(200,200)
        LCD.display(1234)

        LCD.setDigitCount(8) #设置数字位数
        LCD.setMode(QLCDNumber.Bin) #设置进制
        # LCD.setSegmentStyle(QLCDNumber.Flat) #设置样式
        # LCD.setSmallDecimalPoint(True) #设置小数点
        LCD.checkOverflow(123456789) #检查溢出
        LCD.overflow.connect(lambda :print('溢出')) #溢出信号
        LCD.setSegmentStyle(QLCDNumber.Filled) #设置样式

        btn=QPushButton(self)
        btn.setText('测试按钮')
        btn.move(100,350)
        btn.clicked.connect(lambda :print(LCD.value())) #获取选中的数字
        btn.clicked.connect(lambda :print(LCD.intValue())) #获取选中的数字


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())