from PyQt5.Qt import *
import sys

class Window(QWidget):
    def contextMenuEvent(self, evt):
        print("鼠标右键被点击了")
        # 设置菜单
        menu = QMenu(self)
        # 子菜单，最近打开

        open_recent_menu = QMenu(menu)
        open_recent_menu.setTitle("最近打开")

        # 行为动作
        new_action = QAction(QIcon("1.jpg"), "新建", menu)
        new_action.triggered.connect(lambda: print("新建被点击了"))

        open_action = QAction(QIcon("1.jpg"), "打开", menu)
        open_action.triggered.connect(lambda: print("打开被点击了"))
        open_action.setShortcut("Ctrl+O")  # 设置快捷键
        open_action.setStatusTip("打开最近的文件")  # 设置状态栏提示信息
        open_action.triggered.connect(lambda: print("打开被点击了"))

        exit_action = QAction(QIcon("1.jpg"), "退出", menu)
        exit_action.triggered.connect(lambda: print("退出被点击了"))
        exit_action.setShortcut("Ctrl+Q")  # 设置快捷键
        exit_action.setStatusTip("退出应用程序")  # 设置状态栏提示信息
        exit_action.triggered.connect(lambda: print("退出被点击了"))

        file_action = QAction("文件(&F)", menu)

        menu.addAction(new_action)
        menu.addAction(open_action)
        open_recent_menu.addAction(file_action)
        menu.addMenu(open_recent_menu)
        menu.addSeparator()  # 添加分割线
        menu.addAction(exit_action)

        menu.exec_(evt.globalPos()) #显示菜单


app = QApplication(sys.argv)
window = Window()
window.resize(500, 500)
window.setWindowTitle("QWidget案例")
window.move(100, 100)


btn=QPushButton(QIcon("1.jpg"),'按钮',window)


#设置菜单
menu=QMenu(window)
#子菜单，最近打开

open_recent_menu=QMenu(menu)
open_recent_menu.setTitle("最近打开")



#行为动作
new_action=QAction(QIcon("1.jpg"),"新建",menu)
new_action.triggered.connect(lambda :print("新建被点击了"))


open_action=QAction(QIcon("1.jpg"),"打开",menu)
open_action.triggered.connect(lambda :print("打开被点击了"))
open_action.setShortcut("Ctrl+O") #设置快捷键
open_action.setStatusTip("打开最近的文件") #设置状态栏提示信息
open_action.triggered.connect(lambda :print("打开被点击了"))

exit_action=QAction(QIcon("1.jpg"),"退出",menu)
exit_action.triggered.connect(lambda :print("退出被点击了"))
exit_action.setShortcut("Ctrl+Q") #设置快捷键
exit_action.setStatusTip("退出应用程序") #设置状态栏提示信息
exit_action.triggered.connect(lambda :print("退出被点击了"))

file_action=QAction("文件(&F)",menu)



menu.addAction(new_action)
menu.addAction(open_action)
open_recent_menu.addAction(file_action)
menu.addMenu(open_recent_menu)
menu.addSeparator() #添加分割线
menu.addAction(exit_action)


btn.setMenu(menu)

btn.setFlat(True) #设置扁平化
print(btn.isFlat()) #获取是否扁平


btn2=QPushButton("按钮2",window)
btn2.move(0,50)
btn2.setAutoDefault(True) #设置自动默认
btn2.setDefault(True) #设置默认

def show_menu(point):
    print("菜单被展示了",point)
    # 设置菜单
    menu = QMenu(window)
    # 子菜单，最近打开

    open_recent_menu = QMenu(menu)
    open_recent_menu.setTitle("最近打开")

    # 行为动作
    new_action = QAction(QIcon("1.jpg"), "新建", menu)
    new_action.triggered.connect(lambda: print("新建被点击了"))

    open_action = QAction(QIcon("1.jpg"), "打开", menu)
    open_action.triggered.connect(lambda: print("打开被点击了"))
    open_action.setShortcut("Ctrl+O")  # 设置快捷键
    open_action.setStatusTip("打开最近的文件")  # 设置状态栏提示信息
    open_action.triggered.connect(lambda: print("打开被点击了"))

    exit_action = QAction(QIcon("1.jpg"), "退出", menu)
    exit_action.triggered.connect(lambda: print("退出被点击了"))
    exit_action.setShortcut("Ctrl+Q")  # 设置快捷键
    exit_action.setStatusTip("退出应用程序")  # 设置状态栏提示信息
    exit_action.triggered.connect(lambda: print("退出被点击了"))

    file_action = QAction("文件(&F)", menu)

    menu.addAction(new_action)
    menu.addAction(open_action)
    open_recent_menu.addAction(file_action)
    menu.addMenu(open_recent_menu)
    menu.addSeparator()  # 添加分割线
    menu.addAction(exit_action)
    dest_point=window.mapToGlobal(point) #将窗口坐标转换为全局坐标
    menu.exec_(dest_point)  # 显示菜单

window.setContextMenuPolicy(Qt.CustomContextMenu) #设置上下文菜单策略
window.customContextMenuRequested.connect(show_menu) #鼠标右键被点击


window.show()
sys.exit(app.exec_())