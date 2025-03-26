'''
文件入口
pyinstaller  打包工具    把python代码打包成exe文件
pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple
pyinstaller -v
pyinstaller -F -w main.py      打包成一个exe文件   -w 去掉控制台窗口  生成的文件在dist文件夹下

'''
from PyQt5.Qt import *
import sys
from Register_Pane import RegisterPane
from Login_Pane import LoginPane
from Caculator_Pane import CaculatorPane

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_pane = LoginPane()
    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()
    caculator_pane = CaculatorPane() # 计算器面板

    def exit_register_pane():
        print('显示登录面板')
        animation=QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QPoint(0,0))
        animation.setEndValue(QPoint(login_pane.width(),0))
        animation.setDuration(200)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_register_pane():
        print('显示注册面板')
        animation=QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QPoint(0,login_pane.height()))
        animation.setEndValue(QPoint(0,0))
        animation.setDuration(200)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def check_login(account,pwd):
        if account == '123456' and pwd == '123':
            print('登录成功')
            #变量写在函数内部，是一个局部变量，函数执行完毕，变量就会被销毁 所以不会暂时
            # caculator_pane = CaculatorPane()
            caculator_pane.show()
            login_pane.hide() # 隐藏登录面板
        else:
            print('登录失败')
            login_pane.show_error_animation()



    register_pane.exit_signal.connect(exit_register_pane) # 退出信号
    register_pane.register_account_pwd_signal.connect(lambda account,pwd:print(account,pwd)) # 注册信号

    login_pane.show_register_pane_signal.connect(show_register_pane) # 显示注册面板
    login_pane.check_login_signal.connect(check_login) # 登录信号 要验证
    login_pane.show()

    sys.exit(app.exec_())