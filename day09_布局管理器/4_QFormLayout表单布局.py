from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()

    def setup_ui(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(QRadioButton('男'))
        h_layout.addWidget(QRadioButton('女'))

        layout = QFormLayout(self)
        layout.addRow('姓名(&n):', QLineEdit())
        layout.addRow('年龄(&g):', QSpinBox())
        layout.insertRow(2,'性别:', h_layout)
        layout.addRow(QPushButton('提交'))

        # print('控件的个数:',layout.rowCount()) #控件的个数
        # layout.removeRow(2)
        # print('控件的个数:', layout.rowCount())  # 控件的个数
        # layout.setLabelAlignment(Qt.AlignRight) # 设置标签的对齐方式
        layout.setRowWrapPolicy(QFormLayout.DontWrapRows) # 设置换行策略
        print(layout.formAlignment() == Qt.AlignLeft | Qt.AlignTop) # 获取表单的对齐方式
        layout.setFormAlignment(Qt.AlignLeft | Qt.AlignBottom) # 设置表单的对齐方式
        layout.setHorizontalSpacing(10) # 设置水平间距
        layout.setVerticalSpacing(10) # 设置垂直间距
        print(dir(QFormLayout.TakeRowResult)) # 查看类的所有属性和方法

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())