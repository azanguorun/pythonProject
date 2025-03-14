from PyQt5.Qt import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.move(100, 100)
        self.setWindowTitle("QWidget案例")

        # window.setCursor(Qt.BusyCursor) #设置鼠标形状2

        label = QLabel(self)
        label.setText("标签")
        label.resize(100, 20)
        label.setStyleSheet("background-color:red;")
        label.setCursor(Qt.ForbiddenCursor)  # 设置鼠标形状2
        self.label=label
        self.cursor().setPos(100, 100)  # 设置鼠标位置
        print('鼠标位置', self.cursor().pos())

        cursor = QCursor(QPixmap("1.jpg"))
        self.setCursor(cursor)  # 设置鼠标形状2

        self.unsetCursor()  # 恢复鼠标原样


    def mouseMoveEvent(self, a0):  #按下鼠标移动
        print('鼠标移动了',a0.x(),a0.y())
        self.label=self.findChild(QLabel)
        self.label.move(a0.localPos().x(),a0.localPos().y())   #父控件查找子控件




app=QApplication(sys.argv)
window=MyWindow()



window.show()
sys.exit(app.exec_())