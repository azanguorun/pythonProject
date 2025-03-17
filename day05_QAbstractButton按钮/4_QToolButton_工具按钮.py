from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("QWidget案例")

window.move(100, 100)

#工具栏
tb=QToolButton(window)
tb.setIcon(QIcon("1.jpg"))
tb.setToolTip("工具按钮")
tb.setText('工具')
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
tb.setAutoRaise(True)

menu=QMenu(tb)
sub_menu=QMenu(menu)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon("1.jpg"))
sub_action1=QAction("子菜单行为1",sub_menu)
sub_action1.setData([1,2,3])
sub_action2=QAction("子菜单行为2",sub_menu)
sub_action2.setData([4,5,6])

sub_action1.triggered.connect(lambda:print("子菜单行为被点击了1"))
sub_action2.triggered.connect(lambda:print("子菜单行为被点击了2"))

menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(sub_action1)
menu.addAction(sub_action2)
tb.setMenu(menu)
tb.setPopupMode(QToolButton.InstantPopup)
tb.pressed.connect(lambda:print("工具按钮被点击了"))


def do_action(action):
    print("do_action被调用了",action.data())

tb.triggered.connect(do_action)

tb2=QToolButton(window)
tb2.move(100,0)
tb2.setArrowType(Qt.UpArrow)
tb2.setAutoRaise(True)  #自动提升

window.show()
sys.exit(app.exec_())