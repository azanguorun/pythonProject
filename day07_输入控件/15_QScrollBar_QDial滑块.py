from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()

    def setup_ui(self):
        sb=QScrollBar(self)
        sb.resize(30,200)
        sb.move(100,100)

        sb2=QScrollBar(Qt.Horizontal,self)
        sb2.resize(200,30)
        sb2.move(200,100)

        lable=QLabel(self)
        lable.setText("设置值改变信号")
        lable.move(100,400)

        dia=QDial(self)
        dia.resize(200,200)
        dia.move(200,200)
        dia.setRange(0,200)
        def test(val):
            lable.setStyleSheet("font-size:{}px;".format(val))
            lable.adjustSize() #自动调整大小
        dia.valueChanged.connect(test) #设置值改变信号
        dia.setNotchesVisible(True) #设置刻度可见
        dia.setMinimum(10) #设置最小值
        dia.setMaximum(100) #设置最大值
        dia.setPageStep(10) #设置页面步长
        dia.setSingleStep(1) #设置单步长
        dia.setWrapping(True) #设置环绕
        dia.setTracking(True) #设置追踪
        dia.setNotchTarget(10) #设置刻度目标
        dia.setNotchesVisible(True) #设置刻度可见
        dia.setStyleSheet("background-color:red;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())