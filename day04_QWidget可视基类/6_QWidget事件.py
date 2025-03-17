'''


QWidget 事件机制
'''
from PyQt5.Qt import *
import sys
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget案例")
        self.resize(500, 500)
        self.move(100, 100)
        self.move_flag = False

    def setup_ui(self):
        pass

    def showEvent(self, a0):
        print('窗口显示')

    def closeEvent(self, a0):
        print('窗口关闭')

    def moveEvent(self, a0):
        print('窗口移动了')

    def resizeEvent(self, a0):
        print('窗口大小改变了')

    def enterEvent(self, a0):
        print('鼠标进入了')
        self.setStyleSheet("background-color:red;")

    def leaveEvent(self, a0):
        print('鼠标离开了')
        self.setStyleSheet("background-color:green;")

    def mousePressEvent(self, a0):
        if a0.button() == Qt.LeftButton: #左键
            self.move_flag = True
            print('鼠标按下了')
            self.mouse_x=a0.globalX()
            self.mouse_y=a0.globalY()
            print(self.mouse_x,self.mouse_y)

        self.origin_x=self.x()
        self.origin_y=self.y()


    def mouseReleaseEvent(self, a0):
        self.move_flag = False
        print('鼠标释放了')

    def mouseDoubleClickEvent(self, a0):
        print('鼠标双击了')

    def mouseMoveEvent(self, a0):
        if self.move_flag:
            print('鼠标移动了',a0.globalX(),a0.globalY())
            move_x=a0.globalX()-self.mouse_x  #鼠标移动的距离
            move_y=a0.globalY()-self.mouse_y
            self.move(self.origin_x+move_x,self.origin_y+move_y)

    def keyPressEvent(self, a0):
        print('键盘按下了')

    def keyReleaseEvent(self, a0):
        print('键盘释放了')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setup_ui()

    window.show()
    sys.exit(app.exec_())


