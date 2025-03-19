'''
\venv\Lib\site-packages\qt5_applications\Qt\bin

设置tool外部工具  添加外部工具designer.exe 可以在pycharm中打开ui文件


pyqt5 -tool 自带 pyuic5  pyrcc5

>_ pyuic5 1_login_登录界面.ui -o 3_login_登录界面.py

'''
import os
# os.system('pyuic5.exe 1_login_登录界面.ui -o 3_login_登录界面.py')


# os.system('pyuic5.exe 1_login_登录界面.ui -o 4_login_登录界面.py -x') #生成可执行文件
os.system('pyuic5.exe 5_login_ui.ui -o login_ui.py -x') #生成可执行文件
# os.system('pyrcc5.exe test_source.qrc -o test_source_rc.py') #生成可执行文件


