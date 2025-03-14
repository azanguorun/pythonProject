from cProfile import label

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def mousePressEvent(self, evt):
        local_x=evt.x()
        local_y=evt.y()
        sub_widget=self.childAt(local_x,local_y)
        if sub_widget is not None:
            sub_widget.setStyleSheet("background-color: blue;")
            print('鼠标被按下了',local_x,local_y)

class Label(QLabel):
    def mousePressEvent(self, evt):
        # self.setStyleSheet("background-color:red;")
        evt.ignore() #事件忽略，不处理

app = QApplication(sys.argv)

window = Window()
window.resize(500, 500)
window.setWindowTitle("QWidget案例")
window.move(100, 100)



for i in range(1,11):
    label=Label(window)
    label.setText("标签"+str(i))
    label.move(50*i,50*i)


print('获取鼠标位置的子控件',window.childAt(55, 55)) #获取鼠标位置的子控件
print('获取父控件',label.parentWidget()) #获取父控件
print('获取所有子控件的位置',window.childrenRect()) #获取所有子控件的位置

window.show()
sys.exit(app.exec_())