# coding:utf-8
"""
Project    : python_text
Time       ：2025/1/13 下午5:22
File       : 1.py
目的: 
内容:
结果:
"""
from PyQt5.Qt import * # 导入PyQt5的所有常用的一些库
import sys # 导入系统库

#1.创建一个应用程序对象
print(sys.argv) # 命令行参数 ['E:\\ldea\\python_text\\python02_PyQT\\text01\\1.py']
#代码执行方式 1.直接运行 2.命令行 python  代码名称   当别人执行命令行选定列表中有参数时，可选择执行的文件
app = QApplication(sys.argv) # 初始化操作 创建一个图形界面应用程序  传入参数
# qApp  qApp = QApplication()  全局变量
# print(qApp.arguments())  # ['E:\\ldea\\python_text\\python02_PyQT\\text01\\1.py']
# print(app.arguments())  # ['E:\\ldea\\python_text\\python02_PyQT\\text01\\1.py']

#2.控件的操作
#2.1  创建控件
#创建控件没有父控件,就把它当顶层控件,系统会自动给窗口添加一些装饰
window = QWidget() # 创建窗口 window 就是父控件
# window = QPushButton() # 创建按钮
# window = QLabel() # 创建标签

#2.2 设置控件
window.setWindowTitle("第一个PyQt5程序") # 标题
window.resize(500, 500) # 大小
window.move(400, 200) # 位置

label = QLabel(window) # 标签  传入window 作为父控件
label.setText("hello PyQt5") #  文本
label.move(200, 200) # 位置
label.setWindowTitle("hello PyQt5") # 标题

label.show() #会展示一个控件,如果前面QLabel()父控件,所以会被系统自动给窗口添加一些装饰
#控件也可以作为容器,承载子控件


#2.3 展示控件
window.show() # 显示显示完消失

#3.应用程序的执行，进入到消息循环
# sys.exit() # 退出  打印退出码 进程已结束，退出代码为 0
# app.exec_() # 执行应用程序的消息循环 检测用户的操作
sys.exit(app.exec_()) # 退出
