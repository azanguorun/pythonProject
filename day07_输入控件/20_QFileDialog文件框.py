from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def setup_ui(self):
        # QFileDialog.getOpenFileName(self,"选择文件","../","All(*);;Images(*.png *.xpm *.jpg)")
        # result=QFileDialog.getExistingDirectoryUrl(self,"选择文件夹",QUrl("../"))
        # print(result)

        def test():
            fd=QFileDialog(self, '文件', '../', 'All(*);;Images(*.png *.xpm *.jpg)')
            fd.fileSelected.connect(lambda val:print(val))  #文件选择信号
            fd.setAcceptMode(QFileDialog.AcceptSave)  #设置只显示保存按钮
            fd.setDefaultSuffix('txt')

            fd.setFileMode(QFileDialog.Directory)  #设置只显示文件夹
            fd.setNameFilters(['图片','视频','音频']) #设置文件过滤器
            fd.open()


        btn=QPushButton(self)
        btn.setText('测试按钮')
        btn.clicked.connect(test)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())