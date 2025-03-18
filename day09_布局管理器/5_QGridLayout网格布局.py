from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()

    def setup_ui(self):
        gl=QGridLayout(self)

        self.setLayout(gl)
        lable1=QLabel('标签1')
        lable1.setStyleSheet('background-color:red;')
        lable2=QLabel('标签2')
        lable2.setStyleSheet('background-color:green;')
        lable3=QLabel('标签3')
        lable3.setStyleSheet('background-color:blue;')
        gl.addWidget(lable1,0,0)
        gl.addWidget(lable2,0,1)
        gl.addWidget(lable3,1,1,3,3)

        lable5 = QLabel('标签5')
        lable5.setStyleSheet('background-color:cyan;')
        lable6 = QLabel('标签6')
        lable6.setStyleSheet('background-color:gray;')
        label7 = QLabel('标签7')
        label7.setStyleSheet('background-color:magenta;')

        v_layout = QVBoxLayout()
        v_layout.addWidget(lable5)
        v_layout.addWidget(lable6)
        v_layout.addWidget(label7)
        gl.addLayout(v_layout,4,0)  # 插入布局

        print(gl.getItemPosition(2)) # 获取控件的位置
        print(gl.itemAtPosition(2, 1).widget().text()) # 获取控件的内容

        gl.setColumnMinimumWidth(0,100) # 设置列的最小宽度
        gl.setRowMinimumHeight(0,100) # 设置行的最小高度
        # gl.setColumnStretch(1,1) # 设置列的拉伸因子
        gl.setSpacing(10) # 设置间距

        print(gl.rowCount())
        print(gl.columnCount())
        print(gl.cellRect(1, 1))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    gl=window.layout()
    print(gl.cellRect(0, 1))
    window.show()

    sys.exit(app.exec_())