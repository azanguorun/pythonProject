from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("文本编辑框案例")

window.move(100, 100)

le=QLineEdit(window)
le.resize(100,100)
le.move(100,100)
le.setContentsMargins(10,0,0,0) #设置内容边距
le.setStyleSheet("background-color:cyan;")
le.setTextMargins(10,0,0,0) #设置文本边距

le.setAlignment(Qt.AlignCenter) #设置文本对齐方式


btn=QPushButton(window)
btn.setText("按钮")
btn.move(100,200)

def cursor_move():
    le.cursorBackward(False,4) #光标向后移动
    # le.cursorForward(True,2) #光标向前移动
    # le.cursorWordBackward(True) #光标单词向后移动
    # le.cursorWordForward(False) #光标单词向前移动
    # le.home(False) #光标移动到行首23456
    # le.end(True) #光标移动到行尾
    # le.setCursorPosition(0) #设置光标位置
    # print(le.cursorPosition()) #获取光标位置
    # print(le.cursorPositionAt(QPoint(100,100))) #获取指定位置的光标位置
    # print(le.displayText()) #获取显示的文本
    # print(le.dragEnabled()) #获取拖拽是否可用
    le.cursorBackward(False,4) #光标向后移动
    le.copy()   #复制
    le.cut() #剪切
    le.paste() #粘贴
    le.undo() #撤销
    le.redo() #重做
    le.selectAll() #全选
    le.deselect() #取消选择

    le.backspace() #退格键
    le.del_() #删除键
    le.insert("abc") #插入文本
    le.setText("123456") #设置文本
    # le.clear()  #清空文本

    le.select(0,3) #选择文本
    print(le.hasSelectedText()) #是否有选择的文本
    print(le.selectedText()) #获取选择的文本
    print(le.selectionStart()) #获取选择的开始位置
    print(le.selectionEnd()) #获取选择的结束位置
    print(le.selectionLength()) #获取选择的长度
    print(le.maxLength()) #获取最大长度
    le.setMaxLength(6) #设置最大长度
    print(le.minimumWidth()) #获取最小宽度
    le.setFocus() #设置焦点


btn.clicked.connect(cursor_move)


le.textEdited.connect(lambda val:print("文本编辑信号" ,val))
le.textChanged.connect(lambda val:print("文本改变信号" ,val))
le.cursorPositionChanged.connect(lambda val:print("光标位置改变信号" ,val))

window.show()
sys.exit(app.exec_())