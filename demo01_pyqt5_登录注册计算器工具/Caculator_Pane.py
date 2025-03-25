from PyQt5.Qt import *
import sys
from resource.caculator_ui import Ui_Form

# QTDesigner
class CaculatorPane(QWidget, Ui_Form):
    #定义新的信号

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置样式表
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaculatorPane()
    window.show()
    sys.exit(app.exec_())