from PyQt5.Qt import *
import sys
class MyAbstractSpinBox(QAbstractSpinBox):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.lineEdit().setText("0")

    def stepEnabled(self):
        current_num=int(self.text())
        if current_num==0:
            return QAbstractSpinBox.StepUpEnabled
        elif current_num==9:
            return QAbstractSpinBox.StepDownEnabled
        elif current_num<0 or current_num>9:
            return QAbstractSpinBox.StepNone
        else:
            return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, p_int): #步长
        current_num=int(self.text())+p_int
        self.lineEdit().setText(str(current_num))
        # self.lineEdit().setAlignment(Qt.AlignRight)\

    def validate(self, p_str, p_int): #校验
        num=int(p_str)
        if num<18:
            return (QValidator.Intermediate,p_str,p_int) #中间状态
        elif num<=180:
            return (QValidator.Acceptable,p_str,p_int) #可接受
        else:
            return (QValidator.Invalid,p_str,p_int)#不可接受

    def fixup(self, p_str):
        print(p_str)
        return "18"

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()

    def setup_ui(self):
        asb=MyAbstractSpinBox(self) #抽象的数字框
        self.asb=asb
        asb.resize(100,30)
        asb.move(100,100)
        asb.setAccelerated(True) #加速

        self.asb.editingFinished.connect(lambda :print("结束编辑"))

        test_btn=QPushButton(self)
        test_btn.move(100,150)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)

    def btn_test(self):
        print("按钮被点击了")
        print(self.asb.text())
        print(self.asb.lineEdit().setText("100"))

        cl=QCompleter(['123','145','167'],self.asb) #自动补全
        self.asb.lineEdit().setCompleter(cl)
        self.asb.lineEdit().setAlignment(Qt.AlignRight) #设置对齐方式

        self.asb.setButtonSymbols(QAbstractSpinBox.PlusMinus) #设置按钮的符号

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())