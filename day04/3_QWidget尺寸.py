from gc import collect

from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.resize(500,500)
window.move(100,100)
window.setWindowTitle("QWidget案例")


widget_count=20  ##总控件个数
column_count=5  ##列数

row_count=(widget_count-1)//column_count+1 ##行数

widget_width=window.width()/column_count ##控件宽度
window_height=window.height()/row_count  ##控件高度

for i in range(widget_count):
    w=QWidget(window)
    w.resize(widget_width,window_height)
    widget_x=(i%column_count)*widget_width   ##相除获取余数 01234  控件x坐标
    widget_y=(i//column_count)*window_height  ##相除获取值 0123 控件y坐标
    print(widget_y,i,column_count,i//column_count,widget_width)
    w.move(widget_x,widget_y)
    w.setStyleSheet("background-color:red; border:1px solid black;")
    w.show()


w=QWidget(window)
w.resize(100,100)
w.setStyleSheet("background-color:red;")
w.move(0,0)


window.show()
sys.exit(app.exec_())