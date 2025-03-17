from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("Q的学习")
        self.setup_ui()
    def setup_ui(self):
        # QMessageBox.about(self, '标题', '内容')
        QMessageBox.aboutQt(self)

        md=QMessageBox(QMessageBox.Warning,'消息提示','<h2>文件内容被修改</h2>',QMessageBox.Ok | QMessageBox.Discard,self)
        md.setWindowModality(Qt.NonModal)
        md.setIconPixmap(QPixmap('1.jpg').scaled(50,50))
        md.setInformativeText('<h4>是否保存修改</h4>')
        md.setCheckBox(QCheckBox('下次不再提示',md))
        md.setDetailedText('详细信息暂无')

        btn=QPushButton('保存',md)
        md.addButton(btn,QMessageBox.NoRole)
        # md.addButton('不',QMessageBox.NoRole)
        md.setEscapeButton(btn)

        def test(btn):
            role=md.buttonRole(btn)
            if role==QMessageBox.NoRole:
                print('保存')


        md.buttonClicked.connect(test)
        md.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())