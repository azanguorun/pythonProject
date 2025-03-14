from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500) #设置窗口大小
        self.setWindowTitle("QPlainTextEdit的学习")
        self.setup_ui()


    def setup_ui(self):
        pte=QPlainTextEdit(self) # 纯文本编辑框
        self.pte=pte
        pte.resize(300,300) #设置窗口大小
        pte.move(100,100)  #设置窗口位置

        btn=QPushButton(self)
        btn.setText("测试按钮")
        btn.pressed.connect(self.btn_test)
        line_num_parent=QWidget(self)
        line_num_parent.move(70,100) #设置窗口位置
        line_num_parent.resize(30,300) #设置窗口 大小
        line_num_parent.setStyleSheet("background-color:cyan;")

        self.line_label=QLabel(line_num_parent)
        self.line_label.move(0,2)
        #1-100
        line_nums='\n'.join([str(i) for i in range(100)])
        self.line_label.setText(line_nums)

        self.占位提示文本()
        self.格式()
        self.自动换行()
        self.文本操作()
        self.pte.setCenterOnScroll(True) #滚动保证光标可见


    def btn_test(self):
        # self.块的操作()
        self.信号操作()

    def 信号操作(self):
        self.pte.updateRequest.connect(lambda rect,dy: self.line_label.move(self.line_label.x(),self.line_label.y()+dy))
        # self.pte.cursorPositionChanged.connect(lambda :print('光标位置改变信号'))
        # self.pte.modificationChanged.connect(lambda v:print('修改改变信号',v))
        # self.pte.selectionChanged.connect(lambda :print('选中改变信号',self.pte.textCursor().selectedText()))
        # self.pte.blockCountChanged.connect(lambda v:print('块的数量改变信号',v))
        #
        # doc=self.pte.document()
        # doc.setModified(False) #设置修改状态

    def 光标操作(self):
        tc=self.pte.cursorforPosition(QPoint(100,60)) #获取光标
        tc.insertText("123456") #插入文本
        self.pte.setCursorWidth(20) #设置光标宽度
        self.pte.moveCursor(QTextCursor.End,QTextCursor.KeepAnchor) #移动光标
        self.pte.setFocus()

    def 滚动保证光标可见(self):
        self.pte.centerCursor() #居中光标
        self.pte.ensureCursorVisible() #滚动保证光标可见
        self.pte.setFocus()

    def 放大缩小(self):
        self.pte.zoomIn(10) #放大
        # self.pte.zoomOut(2) #缩小

    def 块的操作(self):
        print(self.pte.blockCount()) #获取块的数量
        self.pte.setMaximumBlockCount(3) #设置最大块的数量


    def 文本操作(self):
        self.pte.setPlainText('开始')
        self.pte.appendPlainText("追加文本") #追加文本
        self.pte.appendHtml("<a href=http://www.baidu.com'>百度</a>")
        self.pte.insertPlainText("插入文本") #插入文本
        print(self.pte.toPlainText()) #获取纯文本内容

    def tab键(self):
        self.pte.setTabChangesFocus(True) #设置tab键切换焦点
        print(self.pte.tabChangesFocus()) #获取tab键切换焦点

    def 覆盖模式(self):
        self.pte.setOverwriteMode(True) #设置覆盖模式
        print(self.pte.overwriteMode()) #获取覆盖模式

    def 自动换行(self):
        print(self.pte.lineWrapMode())  #获取自动换行模式
        self.pte.setLineWrapMode(QPlainTextEdit.WidgetWidth) #设置自动换行

    def 格式(self):
        tcf=QTextCharFormat()
        tcf.setFontPointSize(20) #设置字体大小
        tcf.setFontFamily("宋体") #设置字体
        tcf.setFontItalic(True) #设置斜体
        tcf.setFontWeight(QFont.Bold) #设置加粗
        tcf.setFontUnderline(True) #设置下划线
        tcf.setFontOverline(True) #设置上划线
        tcf.setFontStrikeOut(True) #设置删除线
        tcf.setUnderlineColor(QColor(150,50,50)) #设置下划线颜色
        self.pte.setCurrentCharFormat(tcf) #设置当前字符格式

    def 只读(self):
        self.pte.setReadOnly(True) #设置只读
        print(self.pte.isReadOnly()) #判断是否只读

    def 占位提示文本(self):
        self.pte.setPlaceholderText("请输入账号") #设置占位文本
        print(self.pte.placeholderText()) #获取占位文本



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())