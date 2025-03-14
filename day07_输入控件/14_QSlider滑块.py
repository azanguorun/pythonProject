from PyQt5.Qt import *
import sys

class Slider(QSlider):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setTickPosition(QSlider.TicksBothSides) #设置刻度位置
        self.setup_ui()

    def setup_ui(self):
        self.lable = QLabel(self)
        self.lable.setText("0")
        self.lable.setStyleSheet("background-color:red;")
        self.lable.hide()

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt) #调用父类的方法
        x=(self.width()-self.lable.width())/2
        y=int((1-self.value()/(self.maximum()-self.minimum()))*self.height()-self.lable.height())
        self.lable.show()
        self.lable.move(x,y)

    def mouseMoveEvent(self, evt):
        super().mouseMoveEvent(evt) #调用父类的方法
        x = (self.width() - self.lable.width()) / 2
        y = int((1 - self.value() / (self.maximum() - self.minimum())) * (self.height()-self.lable.height()) - self.lable.height())
        self.lable.move(x,y)

        self.lable.setText(str(self.value()))
        self.lable.adjustSize() #自动调整大小

    def mouseReleaseEvent(self, evt): #鼠标释放事件
        super().mouseReleaseEvent(evt) #调用父类的方法
        self.lable.hide() #隐藏标签



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def setup_ui(self):
        sld=Slider(self)
        sld.move(100,100)
        sld.resize(100,300)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())