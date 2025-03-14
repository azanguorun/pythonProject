from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()

    def setup_ui(self):
        # fd=QFontDialog(self) #字体对话框
        font=QFont()
        # font.setFamily("宋体")
        # font.setPointSize(36)
        fd=QFontDialog(font,self)
        fd.setCurrentFont(font) #设置当前字体
        # fd.setOption(QFontDialog.NoButtons,on=True) #设置不使用原生对话框
        fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts) #设置不使用原生对话框
        btn=QPushButton(self)

        btn.setText("按钮")
        btn.move(100,100)
        fd.show()

        lable=QLabel(self)
        lable.setText("设置值改变信号")
        lable.move(100,200)

        def font_sel():
            result=QFontDialog.getFont(self)
            if result[1]:
                lable.setFont(result[0])
                lable.adjustSize() #自动调整大小

        btn.clicked.connect(font_sel) #打开文件对话框


        def cfc(font):
            lable.setFont(font)
            lable.adjustSize() #自动调整大小
        fd.currentFontChanged.connect(cfc) #设置值改变信号

        # def font_test():
        #     print('字体已经被选择',fd.selectedFont().family())
        # btn.clicked.connect(lambda :fd.open(font_test)) #打开文件对话框
        # if fd.exec():
        #     print('字体已经被选择',fd.selectedFont().family())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())