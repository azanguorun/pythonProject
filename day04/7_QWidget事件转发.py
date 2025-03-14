from cProfile import label

from PyQt5.Qt import *
import sys




class Window(QWidget):
    def mousePressEvent(self, evt):
        print('鼠标被按下了')

class MidWindow(QWidget):
    #pass 中间件不处理，转发到父控件处理
    def mousePressEvent(self, evt):
        print('中间控件的鼠标被按下了')
        print('判断事件是否被接收',evt.isAccepted()) #

class Label(QLabel):
    #pass 中间件不处理，转发到父控件处理
    def mousePressEvent(self, evt):
        print('标签的鼠标被按下了')
        print('判断事件是否被接收',evt.isAccepted()) #
        evt.accept() #事件被接收，不转发

app=QApplication(sys.argv)

window=Window()
window.resize(500,500)
window.setWindowTitle("QWidget案例")


mid_window=MidWindow(window)
mid_window.resize(200,200)
mid_window.setAttribute(Qt.WA_StyledBackground,True)
mid_window.setStyleSheet("background-color:yellow;")

label=Label(mid_window)
label.resize(100,100)
label.setText("标签")
label.setStyleSheet("background-color:red;")
label.move(50,50)


btn=QPushButton(mid_window)
btn.setText("按钮")
btn.move(100,100)




window.show()

sys.exit(app.exec_())



