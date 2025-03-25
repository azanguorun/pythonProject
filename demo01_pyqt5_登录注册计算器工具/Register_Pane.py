from PyQt5.Qt import *
import sys
from resource.register_ui import Ui_Form

# QTDesigner
class RegisterPane(QWidget, Ui_Form):
    exit_signal = pyqtSignal() # 退出信号
    register_account_pwd_signal = pyqtSignal(str, str) # 注册信号

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置样式表
        self.setupUi(self)
        self.animation_targets=[self.exit_menue_btn,self.reset_menue_btn,self.about_menue_btn]
        self.animation_targets_pos=[target.pos() for target in self.animation_targets]

    def show_hide_menue(self,checked):
        print('显示隐藏菜单')
        animation_group = QSequentialAnimationGroup(self) # 动画组
        for index,target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b'pos')
            # if not checked:
            animation.setStartValue(self.main_menue_btn.pos())
            animation.setEndValue(self.animation_targets_pos[index])
            # else:
            #     animation.setEndValue(self.main_menue_btn.pos())
            #     animation.setStartValue(self.animation_targets_pos[index])
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.InOutBounce)
            animation_group.addAnimation(animation)

        # if not checked:
        #     animation_group.setDirection(QAbstractAnimation.Forward) # 向前
        # else:
        #     animation_group.setDirection(QAbstractAnimation.Backward) # 向后
        animation_group.setDirection(checked) #  通过枚举值 获取前进 后退
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def about_lk(self):
        # print('关于')
        QMessageBox.about(self,'bilibili','https://www.bilibili.com/')

    def reset(self):
        # print('重置')
        self.account_le.clear()
        self.password_le.clear()
        self.confirm_pwd_le.clear()

    def exit_pane(self):
        # print('退出')
        self.exit_signal.emit()

    def check_reqister(self):
        # print('注册')
        self.register_account_pwd_signal.emit(self.account_le.text(), self.password_le.text())

    def enable_register_btn(self):
        print('检查是否可以注册')
        account_txt=self.account_le.text()
        password_txt=self.password_le.text()
        cp_txt=self.confirm_pwd_le.text()
        if len(account_txt)>=0 and len(password_txt)>=0 and len(cp_txt)>=0 and password_txt==cp_txt:
            self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegisterPane()
    window.exit_signal.connect(lambda: print('退出'))
    window.register_account_pwd_signal.connect(lambda account, pwd: print(account, pwd))
    window.show()

    sys.exit(app.exec_())