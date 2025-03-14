from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget交互案例")
        self.resize(500, 500)
        self.move(100, 100)
        self.setup_ui()

    def setup_ui(self):
        #添加子控件
        label=QLabel(self)
        label.setText("标签")
        label.move(100,100)
        label.hide() #隐藏控件


        le=QLineEdit(self)
        # le.setText("输入框")
        le.move(100,150)

        def text_cao(text):
            print('文本发生改变',text)
            btn.setEnabled(len(text)>0)
        le.textChanged.connect(text_cao) #文本发生改变
        # le.setFocus() #设置焦点
        le.setFocusPolicy(Qt.TabFocus)  # 设置焦点策略 TabFocus 点击Tab切换焦点


        btn=QPushButton(self)
        btn.setText("按钮")
        btn.move(100,200)
        btn.setEnabled(False) #设置控件是否可用

        def check():
            print('状态发生改变')
            content=le.text()
            if content=='123':
                label.setText("登录成功")
            else:
                label.setText("登录失败")
            label.show()
            label.adjustSize()

        btn.pressed.connect(check) #状态发生改变


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())