from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()

    def setup_ui(self):
        print(QAbstractSlider.__subclasses__())
        sd=QSlider(self)
        sd.move(100,100)

        label=QLabel(self)
        label.move(200,100)
        label.resize(100,30)
        label.setText("0")
        sd.valueChanged.connect(lambda val:label.setText(str(val))) #值改变
        sd.sliderMoved.connect(lambda val:print("滑块移动了",val)) #滑块移动了
        sd.actionTriggered.connect(lambda val:print("动作触发了",val)) #动作触发了
        sd.rangeChanged.connect(lambda min,max:print("范围改变了",min,max)) #范围改变了

        sd.setMaximum(10)
        sd.setMinimum(0)
        sd.setValue(5)
        sd.setSingleStep(2) #设置步长
        sd.setPageStep(4) #设置页长
        sd.setTracking(True) #设置是否追踪
        sd.setOrientation(Qt.Horizontal) #设置方向
        sd.setTickInterval(1) #设置刻度间隔
        sd.setTickPosition(QSlider.TicksBothSides) #设置刻度位置
        sd.setInvertedAppearance(True) #设置是否反向
        sd.setInvertedControls(True) #设置是否反向控制


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())