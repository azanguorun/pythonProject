from PyQt5.Qt import *
import sys
from resource.login_ui import Ui_Form

# QTDesigner
class LoginPane(QWidget, Ui_Form):
    #定义新的信号
    show_register_pane_signal=pyqtSignal()
    check_login_signal=pyqtSignal(str,str)

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置样式表
        self.setupUi(self)

        movie=QMovie(':/login/images/login_top_bg.gif')
        movie.setScaledSize(QSize(500,200))
        self.login_top_bg_label.setMovie(movie)
        movie.start()

    def show_register_pane(self):
        # print('弹出注册窗口')
        #两个界面不直接关联，通过信号关联
        self.show_register_pane_signal.emit() #发射信号

    def open_qq_link(self):
        print('打开QQ链接')
        link='https://www.bilibili.com/'
        QDesktopServices.openUrl(QUrl(link))

    def enable_login_btn(self):
        account=self.account_cb.currentText() #获取当前账号
        pwd=self.pwd_le.text() #获取当前密码
        print('检查是否可以登录',account,pwd)
        if len(account) >0 and len(pwd)>0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def  check_login(self):
        #在界面内容将数据丢出去，要在上面定义新的信号 check_login_signal  检查登录信息  传入账号 密码 丢出去
        self.check_login_signal.emit(self.account_cb.currentText(),self.pwd_le.text())

    def auto_login(self,checked):
        print('自动登录',checked)
        if checked:
            self.remember_pwd_cb.setChecked(True) #自动登录时记住密码


    def remember_pwd(self,checked):
        print('记住密码',checked)
        if not checked:
            self.auto_login_cb.setChecked(False) #自动登录时记住密码

    def show_error_animation(self):
        #展示错误动画  控件可以左右抖动
        animation=QPropertyAnimation(self)
        animation.setTargetObject(self.login_bottom)
        animation.setPropertyName(b'pos')
        animation.setKeyValueAt(0,self.login_bottom.pos())
        animation.setKeyValueAt(0.2,self.login_bottom.pos()+QPoint(15,0))  # 15 0
        animation.setKeyValueAt(0.5,self.login_bottom.pos())
        animation.setKeyValueAt(0.7,self.login_bottom.pos()+QPoint(-15,0))
        animation.setKeyValueAt(1,self.login_bottom.pos())
        animation.setDuration(200)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped) # 动画结束后删除





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())