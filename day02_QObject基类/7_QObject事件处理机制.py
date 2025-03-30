# coding:utf-8
"""
Project    : python_text
Time       ：2025/1/21 下午4:38
File       : 7.py
目的:         事件处理机制
内容:
结果:
"""

from PyQt5.Qt import * # 导入PyQt5的所有常用的一些库
import sys # 导入系统库



#继承父类,重写
class App(QApplication):
    def notify(self, receiver, event):        #receiver 接收者  event 事件
        if receiver.inherits('QPushButton') and event.type() == QEvent.MouseButtonPress:
            #receiver继承QPushButton 并且 事件类型是鼠标按下
            print('QPushButton')
        return super().notify(receiver, event) # 继续执行父类的notify方法 处理

class btn(QPushButton):
    def event(self, event):
        if event.type() == QEvent.MouseButtonPress:
            print('按钮被点击了')
        return super().event(event)

    def mousePressEvent(self, e):
        print('按钮被按下了')
        return super().mousePressEvent(e)

app = App(sys.argv) # 初始化操作 创建一个图形界面应用程序  传入参数

window=QWidget() # 创建一个窗口

btn = btn(window) # 创建一个按钮

btn.setText('按钮') # 设置按钮的文本
btn.move(100,100) # 设置按钮的位置
def btn_click():
    print('按钮被点击了')

btn.pressed.connect(btn_click) # 绑定信号


window.show() # 显示窗口


sys.exit(app.exec_()) # 退出程序
