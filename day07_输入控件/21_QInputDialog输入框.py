from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QInputDialog的学习")
        self.setup_ui()
    def setup_ui(self):
        result=QInputDialog.getInt(self,'整数输入框','请输入数字',88,1,100,1)
        result=QInputDialog.getDouble(self,'小数输入框','请输入数字',88.88,1,100,1)
        result=QInputDialog.getText(self,'文本输入框','请输入内容')
        result=QInputDialog.getItem(self,'条目选择框','请选择一个选项',['选项1','选项2','选项3'])
        result=QInputDialog.getMultiLineText(self,'多行文本输入框','请输入内容','default')
        # result=QInputDialog.getColor(self,'颜色选择框','请选择一个颜色')
        print(result)

        input_d=QInputDialog(self,Qt.FramelessWindowHint)
        input_d.setOption(QInputDialog.UseListViewForComboBoxItems)
        input_d.setComboBoxItems(['选项1','选项2','选项3'])   #设置条目
        input_d.setLabelText('请输入内容')
        input_d.setOkButtonText('确定')
        input_d.setCancelButtonText('取消')
        input_d.setInputMode(QInputDialog.DoubleInput) #设置输入模式
        input_d.setDoubleRange(1,100)
        input_d.setDoubleStep(1)
        input_d.setDoubleDecimals(1)

        input_d.intValueSelected.connect(lambda val:print('整数信号',val))  #整数信号
        input_d.doubleValueSelected.connect(lambda val:print('小数信号',val))  #小数信号
        input_d.textValueSelected.connect(lambda val:print('文本信号',val))  #文本信号
        input_d.textValueChanged.connect(lambda val:print('文本改变信号',val))  #文本改变信号
        input_d.currentIndexChanged.connect(lambda val:print('当前索引改变信号',val))  #当前索引改变信号
        input_d.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())