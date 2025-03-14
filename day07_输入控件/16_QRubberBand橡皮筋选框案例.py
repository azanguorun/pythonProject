from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def setup_ui(self):
        for i in range(30):
            cb=QCheckBox(self)
            # self.cb=cb
            cb.setText("{}".format(i))
            cb.move(i%4*50,i//4*50)
        self.rb=QRubberBand(QRubberBand.Rectangle,self)

    def mousePressEvent(self, evt):
        self.origin_pos=evt.pos()
        self.rb.setGeometry(QRect(self.origin_pos,QSize()))
        self.rb.show()

    def mouseMoveEvent(self, evt):
        self.rb.setGeometry(QRect(self.origin_pos,evt.pos()).normalized()) #设置几何形状

    def mouseReleaseEvent(self, evt):
        rect=self.rb.geometry() #获取几何形状
        for chlid in self.children(): #获取子控件
            if rect.contains(chlid.geometry()) and chlid.inherits('QCheckBox'): #获取内容矩形
                chlid.toggle() #切换状态
        self.rb.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())