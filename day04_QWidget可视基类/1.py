# coding:utf-8
"""
Project    : python_text
Time       ：2025/3/1 下午8:31
File       : 1.py
目的: 
内容:
结果:
"""
from PyQt5.Qt import * # 导入PyQt5的所有常用的一些库
import sys # 导入系统库

class AccountTool:
    ACCOUNT_ERROR = 1
    PWD_ERROR = 2
    SUCCESS = 3


    @staticmethod  #静态方法
    def check_login(account,pwd):
        if account !='admin':
            return AccountTool.ACCOUNT_ERROR
        if pwd != '123456':
            return AccountTool.PWD_ERROR
        return AccountTool.SUCCESS


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5的学习')
        self.resize(500,500)
        self.setMinimumSize(500,500)
        self.setup_ui()

    def setup_ui(self):
        self.accounnt_le=QLineEdit(self)
        self.accounnt_le.setPlaceholderText('请输入账号')
        self.pwd_le=QLineEdit(self)
        self.pwd_le.setPlaceholderText('请输入密码')
        self.pwd_le.setEchoMode(QLineEdit.Password)
        self.login_btn=QPushButton('登   录',self)

        self.login_btn.clicked.connect(self.cao)

    def cao(self):
        account=self.accounnt_le.text()
        pwd=self.pwd_le.text()
        state=AccountTool.check_login(account,pwd)
        if state == AccountTool.ACCOUNT_ERROR:
            print('账号错误')
            self.accounnt_le.setText('')
            self.pwd_le.setText('')
            self.accounnt_le.setFocus()
        elif state == AccountTool.PWD_ERROR:
            print('密码错误')
            self.pwd_le.setText('')
            self.pwd_le.setFocus()
        elif state == AccountTool.SUCCESS:
            print('登录成功')
    def resizeEvent(self, evt):
        widget_w = 150
        widget_h = 40
        margin = 60

        self.accounnt_le.resize(widget_w, widget_h)
        self.pwd_le.resize(widget_w, widget_h)
        self.login_btn.resize(widget_w, widget_h)

        x = int((self.width() - widget_w) / 2)

        self.accounnt_le.move(x, self.height() / 4)
        self.pwd_le.move(x, self.accounnt_le.y() + widget_h + margin)
        self.login_btn.move(x, self.pwd_le.y() + widget_h + margin)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())