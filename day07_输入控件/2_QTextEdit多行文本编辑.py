from PyQt5.Qt import *
import sys
class MyTextEdit(QTextEdit):
    def mousePressEvent(self,evt):
        link_str=self.anchorAt(evt.pos()) #获取超链接
        if len(link_str)>0:
            print(evt.pos(),link_str,QUrl(link_str))
            QDesktopServices.openUrl(QUrl(link_str))

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def text_changed(self):
        print("文本改变了")
        print(self.te.toPlainText()) #获取纯文本内容
        print(self.te.toHtml()) #获取html文本内容

    def setup_ui(self):
        te = MyTextEdit(self)
        self.te = te
        te.move(50,50)
        te.resize(300,300)
        te.setStyleSheet("background-color:cyan;")
        # self.占位文本的提示()

        te.setHtml("<h1>123456</h1>") #设置html文本内容
        # self.te.insertPlainText("123456") #插入纯文本内容
        te.insertHtml("<h2>123456</h2>") #插入html文本内容

        te.append("<h3>123456</h3>") #追加文本内容
        # print(self.te.toHtml()) #获取html文本内容
        te.textChanged.connect(self.text_changed) #文本改变信号
        # te.selectionChanged.connect(self.cursor_changed) #光标改变信号
        # te.cursorPositionChanged.connect(self.cursor_position_changed) #光标位置改变信号
        # te.copyAvailable.connect(self.copy_available) #复制可用信号
        # te.selectionChanged.connect(self.selection_changed) #选中改变信号
        # te.anchorClicked.connect(self.anchor_clicked) #锚点点击信号

        btn=QPushButton(self)
        btn.setText("测试按钮")

        btn.pressed.connect(self.btn_test) #清空文本内容
        # te.textCursor().insertTable(2,2) #插入表格
        te.insertHtml("<a href=http://www.baidu.com'>百度</a>") #插入html文本内容



    def btn_test(self):
        print(self.te.document())
        print(self.te.textCursor())
        # self.te.setText("")
        # self.光标内容的插入()
        # self.格式设置与合并()
        # self.文本选中与清空()
        # self.文本选中内容的获取()
        self.超链接()

    def 超链接(self):
        self.te.setOpenExternalLinks(True) #设置是否打开外部链接
        self.te.setOpenLinks(True) #设置是否打开链接

    def tab功能测试(self):
        self.te.setTabChangesFocus(True) #设置tab键切换焦点
        self.te.setTabStopDistance(100) #设置tab键的距离
        self.te.setTabStopWidth(50) #设置tab键的宽度

    def 只读模式(self):
        self.te.setReadOnly(True) #设置只读模式
        self.te.insertPlainText("123456") #插入纯文本内容

    def 常用编辑功能(self):
        self.te.undo() #撤销
        self.te.redo() #重做
        self.te.cut() #剪切
        self.te.copy() #复制
        self.te.paste() #粘贴
        self.te.selectAll() #全选
        self.te.deselect() #取消选中
        self.te.clear() #清空文本内容
        print(self.te.find("1"))    #查找文本内容

    def 滚动到锚点(self):
        self.te.scrollToAnchor("btn") #滚动到锚点

    def 字符设置(self):
        tcf=QTextCharFormat()
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(20)
        tcf.setFontWeight(QFont.Bold) #设置字体加粗
        tcf.setFontCapitalization(QFont.AllUppercase) #设置字体大写
        tcf.setForeground(QBrush(QColor(200,0,0))) #设置字体颜色
        tcf.setBackground(QBrush(QColor(0,200,0))) #设置字体背景颜色
        tcf.setFontUnderline(True) #设置字体下划线
        tcf.setFontOverline(True) #设置字体上划线
        self.te.setCurrentCharFormat(tcf) #设置当前字符格式

    def 颜色设置(self):
        self.te.setTextBackgroundColor(QColor(200,0,0)) #设置文本背景颜色
        self.te.setTextColor(QColor(0,200,0)) #设置文本颜色

    def 字体设置(self):
        self.te.setFontFamily("幼圆")
        self.te.setFontPointSize(20)
        self.te.setFontWeight(QFont.Bold) #设置字体加粗
        self.te.setFontItalic(True) #设置字体斜体
        # self.te.setFontUnderline(True) #设置字体下划线
        # self.te.setFontOverline(True) #设置字体上划线
        # self.te.setFontStrikeOut(True) #设置字体删除线

    def 对齐方式(self):
        self.te.setAlignment(Qt.AlignCenter) #获取文本对齐方式

    def 光标设置(self):
        print(self.te.cursorRect(self.te.textCursor())) #获取光标所在的矩形区域
        if self.te.overwriteMode(): #判断是否是覆盖模式
            self.te.setOverwriteMode(False) #设置不覆盖模式
            self.te.setCursorWidth(10) #设置光标宽度
        else:
            self.te.setOverwriteMode(True) #设置覆盖模式
            self.te.setCursorWidth(10) #设置光标宽度

    def 覆盖模式(self):
        self.te.setOverwriteMode(True) #设置覆盖模式

    def 软换行(self):
        # self.te.setLineWrapMode(QTextEdit.NoWrap) #设置不换行
        self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)  #设置固定像素宽度换行
        self.te.setLineWrapColumnOrWidth(100) #设置固定像素宽度换行的宽度

    def 位置相关(self):
        tc = self.te.textCursor() #获取光标对象
        print(tc.atBlockStart()) #判断光标是否在块的开头
        print(tc.atBlockEnd())
        print(tc.atStart()) #判断光标是否在文本的开头
        print(tc.atEnd())
        print(tc.atColumn(0))  #判断光标是否在列的开头
        print(tc.columnNumber())  #获取光标所在的列数
        print(tc.position()) #
        print(tc.blockNumber())
        print(tc.block().text())
        print(tc.positionInBlock())

    def 文本的其他操作(self):
        tc=self.te.textCursor()
        print(tc.selectionStart()) #获取文本的起始位置
        print(tc.selectionEnd()) #获取文本的结束位置
        print(tc.hasSelection()) #判断是否有选中的文本
        tc.clearSelection() #清空文本内容
        tc.deleteChar() #删除一个字符
        tc.deletePreviousChar() #删除前一个字符


        # self.te.setReadOnly(True) #设置只读
        # self.te.setAcceptRichText(False) #设置不接受富文本
        # self.te.setLineWrapMode(QTextEdit.NoWrap) #设置不换行

    def 文本选中内容的获取(self):
        tc = self.te.textCursor() #获取光标对象
        print(tc.selectedText()) #获取选中的文本内容
        print(tc.selectionStart()) #获取选中的文本起始位置
        print(tc.selection().toPlainText())
        print(tc.selectedTableCells())

    def 文本选中与清空(self):
        tc = self.te.textCursor() #获取光标对象
        tc.setPosition(6,QTextCursor.KeepAnchor) #设置光标位置

        tc.movePosition(QTextCursor.StartOfLine,QTextCursor.KeepAnchor,1) #移动光标位置

        self.te.setTextCursor(tc) #设置光标
        self.te.setFocus() #设置焦点

    def 格式设置与合并(self):
        tc = self.te.textCursor()
        print(tc.block().text())
        print(tc.blockNumber())
        print(tc.currentList().count())
        return None

        tc = self.te.textCursor()
        tbf=QTextBlockFormat() #块的格式
        tbf.setAlignment(Qt.AlignCenter) #设置文本对齐方式
        tbf.setTopMargin(50) #设置文本上边距
        tbf.setBottomMargin(50) #设置文本下边距
        tbf.setLeftMargin(50) #设置文本左边距
        tbf.setIndent(3) #设置文本缩进
        tc.setBlockFormat(tbf) #设置块的格式

        return None
        tc=self.te.textCursor()
        tcf=QTextCharFormat() #字符的格式
        tcf.setFontFamily("微软雅黑")
        tcf.setFontPointSize(20)
        tcf.setFontUnderline(True)
        tcf.setFontItalic(True)
        tcf.setFontWeight(QFont.Bold)
        tcf.setFontStrikeOut(True)
        tcf.setFontOverline(True)
        tc.setBlockCharFormat(tcf) #设置字符的格式

    def 光标内容的插入(self):
        tc = self.te.textCursor()
        tff=QTextFrameFormat() #文本框的格式
        tff.setBorder(1)
        tff.setBorderBrush(QBrush(QColor(100,100,100)))
        tff.setRightMargin(50) #设置文本右边距
        tc.insertFrame(tff)
        doc=self.te.document()
        rootFrame=doc.rootFrame()
        rootFrame.setFrameFormat(tff)

        return None
        tc=self.te.textCursor()
        tbf=QTextBlockFormat() #块的格式
        tbf.setAlignment(Qt.AlignCenter) #设置文本对齐方式
        tbf.setTopMargin(50) #设置文本上边距
        tbf.setBottomMargin(50) #设置文本下边距
        tbf.setLeftMargin(50) #设置文本左边距
        tbf.setIndent(3) #设置文本缩进

        tcf=QTextCharFormat() #字符的格式
        tcf.setFontFamily("微软雅黑")
        tcf.setFontPointSize(20)
        tcf.setFontUnderline(True)

        tc.insertBlock(tbf,tcf) #插入一个块
        self.te.setFocus()

        return None
        tc = self.te.textCursor()
        ttf=QTextTableFormat()
        ttf.setAlignment(Qt.AlignCenter) #设置文本对齐方式
        ttf.setCellPadding(10) #设置文本边距
        ttf.setCellSpacing(10) #设置文本间距
        ttf.setBorder(1) #设置边框
        # ttf.setBorderBrush(QBrush(QColor(100,100,100))) #设置边框颜色
        # ttf.setBackground(QBrush(QColor(170,170,100))) #设置背景颜色

        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength, 50),
                                      QTextLength(QTextLength.PercentageLength, 40),
                                      QTextLength(QTextLength.PercentageLength, 10)
                                       )) #设置列宽

        table=tc.insertTable(3,3,ttf)
        # table.appendColumns(2) #追加列
        # table.removeColumns(1) #删除列
        # table.appendRows(2) #追加行
        # table.removeRows(1) #删除行

        return None



        tc=self.te.textCursor()
        tlf=QTextListFormat()
        tlf.setIndent(3) #设置列表缩进
        tlf.setStyle(QTextListFormat.ListDisc) #设置列表风格
        tlf.setNumberPrefix("<<") #设置列表前缀
        tlf.setNumberSuffix(".") #设置列表后缀

        tl=tc.createList(tlf)
        return None


        tc=self.te.textCursor()
        tl=tc.insertList(QTextListFormat.ListDecimal) #插入列表
        # tl=tc.createList(QTextListFormat.ListDisc) #创建列表
        print(tl)
        return None

        tc=self.te.textCursor()
        tdf=QTextDocumentFragment.fromHtml("<h1>123456</h1>")
        return None


        tc=self.te.textCursor()
        tif=QTextImageFormat()
        tif.setName('./1.jpg')
        tif.setWidth(100)
        tif.setHeight(100)
        tc.insertImage(tif,QTextFrameFormat.FloatRight)
        return None

        tcf=QTextCharFormat()
        tcf.setToolTip('光标提示')
        tcf.setFontFamily("微软雅黑")
        tcf.setFontPointSize(20)
        tcf.setFontUnderline(True)
        tcf.setFontItalic(True)

        tc=self.te.textCursor()
        tc.insertText('百度',tcf)

        tc.insertHtml("<a href=http://www.baidu.com'>百度</a>")

    def 占位文本的提示(self):
        self.te.setPlaceholderText("请输入账号")
        print(self.te.placeholderText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())