from PyQt5.Qt import *
import sys
from resource.register_ui import Ui_Form

# QTDesigner
class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置样式表
        self.setupUi(self)

    def show_hide_menue(self):
        print('显示隐藏菜单')

    def about_lk(self):
        print('关于')

    def reset(self):
        print('重置')

    def exit_pane(self):
        print('退出')

    def check_reqister(self):
        print('注册')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())