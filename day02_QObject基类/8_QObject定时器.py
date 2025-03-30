# coding:utf-8
"""
Project    : python_text
Time       ：2025/1/22 上午11:19
File       : 8.py
目的:        定时器
内容:
结果:
"""

from PyQt5.Qt import * # 导入PyQt5的所有常用的一些库
import sys # 导入系统库


class MyObject(QObject):
    def timerEvent(self, evt):
        print('定时器事件')
        print(evt)
        print(self)


#1.创建一个应用程序对象
app = QApplication(sys.argv) # 初始化操作 创建一个图形界面应用程序  传入参数

#2.控件的操作
window = QWidget() # 创建窗口 window 就是父控件

#2.2 设置控件
window.setWindowTitle("QObject的使用") # 标题
window.resize(500, 500) # 大小

obj=MyObject()

timer_id=obj.startTimer(1000) # 1秒

obj.timerEvent(timer_id)


window.move(400, 200) # 位置

label = QLabel(window) # 标签  传入window 作为父控件
label.setText("") #  文本
label.move(200, 200) # 位置
label.setWindowTitle("hello PyQt5") # 标题

#2.3 展示控件
window.show() # 显示 显示完消失

#3.应用程序的执行，进入到消息循环
sys.exit(app.exec_()) # 退出