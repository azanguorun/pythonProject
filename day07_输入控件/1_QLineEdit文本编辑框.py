from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("文本编辑框案例")

window.move(100, 100)

ql=QLineEdit("请输入账号",window) #占位文本
btn=QPushButton(window)
btn.setText("按钮")
btn.move(0,30)
btn.pressed.connect(lambda :ql.insert("abc"))


ql1=QLineEdit(window)
ql1.move(0,100)
ql2=QLineEdit(window)
ql2.move(0,150)
ql2.setEchoMode(QLineEdit.Password) #枚举值 密码模式
ql2.setInputMask(">A-9") #输入掩码
ql2.setInputMask("9999-9999999")

btn1=QPushButton(window)
btn1.setText("复制")
btn1.move(0,200)

def copy():
    ql2.setText(ql1.text())
    print(ql2.text())

btn1.pressed.connect(copy)

ql3=QLineEdit(window)
ql3.resize(100,30)
ql3.move(300,100)
ql3.setContentsMargins(10,0,0,0) #设置内容边距
ql3.setStyleSheet("background-color:cyan;")
ql3.setTextMargins(10,0,0,0) #设置文本边距

ql3.setAlignment(Qt.AlignCenter) #设置文本对齐方式


btn=QPushButton(window)
btn.setText("按钮")
btn.move(310,130)

def cursor_move():
    ql3.cursorBackward(False,4) #光标向后移动
    # ql3.cursorForward(True,2) #光标向前移动
    # ql3.cursorWordBackward(True) #光标单词向后移动
    # ql3.cursorWordForward(False) #光标单词向前移动
    # ql3.home(False) #光标移动到行首23456
    # ql3.end(True) #光标移动到行尾
    # ql3.setCursorPosition(0) #设置光标位置
    # print(ql3.cursorPosition()) #获取光标位置
    # print(ql3.cursorPositionAt(QPoint(100,100))) #获取指定位置的光标位置
    # print(ql3.displayText()) #获取显示的文本
    # print(ql3.dragEnabled()) #获取拖拽是否可用
    ql3.cursorBackward(False,4) #光标向后移动
    ql3.copy()   #复制
    ql3.cut() #剪切
    ql3.paste() #粘贴
    ql3.undo() #撤销
    ql3.redo() #重做
    ql3.selectAll() #全选
    ql3.deselect() #取消选择

    ql3.backspace() #退格键
    ql3.del_() #删除键
    ql3.insert("abc") #插入文本
    ql3.setText("123456") #设置文本
    # ql3.clear()  #清空文本

    ql3.select(0,3) #选择文本
    print(ql3.hasSelectedText()) #是否有选择的文本
    print(ql3.selectedText()) #获取选择的文本
    print(ql3.selectionStart()) #获取选择的开始位置
    print(ql3.selectionEnd()) #获取选择的结束位置
    print(ql3.selectionLength()) #获取选择的长度
    print(ql3.maxLength()) #获取最大长度
    ql3.setMaxLength(6) #设置最大长度
    print(ql3.minimumWidth()) #获取最小宽度
    ql3.setFocus() #设置焦点


btn.clicked.connect(cursor_move)


ql3.textEdited.connect(lambda val:print("文本编辑信号" ,val))
ql3.textChanged.connect(lambda val:print("文本改变信号" ,val))
ql3.cursorPositionChanged.connect(lambda val:print("光标位置改变信号" ,val))


window.show()
sys.exit(app.exec_())