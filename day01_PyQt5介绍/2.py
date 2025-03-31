# coding:utf-8
"""
Project    : python_text
Time       ：2025/1/14 上午11:56
File       : pyuic5转换类.py
目的: 
内容:
结果:
"""

import sys
from PyQt5.Qt import * # 导入PyQt5的所有常用的一些库

from mywindow import Window  # 导入自定义的窗口类


app = QApplication(sys.argv) # 初始化操作 创建一个图形界面应用程序  传入参数

window=Window()


window.show()

sys.exit(app.exec_()) # 退出

