from cProfile import label

from PyQt5.Qt import *
import sys



class MyLabel(QLabel):
    def enterEvent(self, a0):
        print('鼠标进入了')
        self.setText("欢迎光临")


    def leaveEvent(self, a0):
        print('鼠标离开了')
        self.setText("谢谢惠顾")


    def keyPressEvent(self, evt):
        # key 普通键 modifiers 组合键
        print('判断是否是tab键',evt.key()==Qt.Key_Tab)
        print('判断是否是ctrl+S',evt.modifiers()==Qt.ControlModifier and evt.key()==Qt.Key_S)
        print('判断是否是shift',evt.modifiers()==Qt.ShiftModifier)
        print('判断是否是alt',evt.modifiers()==Qt.AltModifier)
        print('键盘被按下了')


app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 400)
window.setWindowTitle("QWidget案例")


label=MyLabel(window)
label.setText("标签")
label.resize(100,100)
label.move(100,100)
label.setStyleSheet("background-color:red;")
label.setFocusPolicy(Qt.StrongFocus) #设置焦点策略

window.show()
sys.exit(app.exec_())