from PyQt5.Qt import *
import sys


class MyDoubleSB(QDoubleSpinBox):
    def textFromValue(self, p_float):
        return str(p_float)+"￥"

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()

    def setup_ui(self):
        dsb=MyDoubleSB(self)
        dsb.resize(100,30)
        dsb.move(100,100)
        dsb.setAccelerated(True) #加速

        dsb.setMaximum(88.88)
        dsb.setMinimum(11.11)
        dsb.setRange(11.11,88.88) #范围
        dsb.setSingleStep(0.01)
        dsb.setDecimals(2) #小数位数

        dsb.setWrapping(True) #循环
        dsb.setPrefix("$") #前缀
        dsb.setSuffix("￥") #后缀

        btn=QPushButton(self)
        btn.move(100,150)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda :dsb.setValue(66.56))
        btn.clicked.connect(lambda :print(dsb.value(),dsb.cleanText(),dsb.lineEdit().text()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())