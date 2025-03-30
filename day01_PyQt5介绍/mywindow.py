# coding:utf-8
"""
Project    : python_text
Time       ：2025/1/14 下午4:27
File       : mywindow.py
目的: 
内容:
结果:
"""

from PyQt5.Qt import * # 导入PyQt5的所有常用的一些库

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5')
        self.resize(500,500)

        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText('按钮')


if __name__ == '__main__':

    '''
    测试代码   调用不执行
    '''
    import sys
    app = QApplication(sys.argv) # 初始化操作 创建一个图形界面应用程序  传入参数

    window=Window()
    window.show()

    sys.exit(app.exec_()) # 退出
