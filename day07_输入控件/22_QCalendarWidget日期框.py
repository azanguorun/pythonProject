from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()
    def setup_ui(self):
        cw=QCalendarWidget(self)
        cw.move(100,100)
        cw.resize(200,200)
        cw.setFirstDayOfWeek(Qt.Sunday) #设置每周的第一天

        cw.setMinimumDate(QDate(2020,1,1)) #设置最小日期
        cw.setMaximumDate(QDate(2020,12,31)) #设置最大日期
        cw.setDateRange(QDate(2020,1,1),QDate(2020,12,31)) #设置日期范围

        # cw.setDateEditEnabled(False) #设置日期编辑框不可用

        btn=QPushButton(self)
        btn.setText('测试按钮')
        btn.move(100,350)
        btn.clicked.connect(lambda :print(cw.monthShown())) #获取选中的日期
        btn.clicked.connect(lambda :print(cw.yearShown())) #获取选中的日期
        btn.clicked.connect(lambda :print(cw.selectedDates())) #获取选中的日期列表

        btn.clicked.connect(cw.showNextMonth) #显示下一个月
        btn.clicked.connect(cw.showPreviousMonth) #显示上一个月
        btn.clicked.connect(cw.showNextYear) #显示下一年
        btn.clicked.connect(cw.showPreviousYear) #显示上一年
        btn.clicked.connect(cw.showSelectedDate) #显示选中的日期

        tcf=QTextCharFormat()
        tcf.setFontFamily('宋体')
        tcf.setFontPointSize(20)
        tcf.setFontUnderline(True)

        cw.setHeaderTextFormat(tcf) #设置表头格式
        cw.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames) #设置水平表头格式

        cw.activated.connect(lambda val:print(val)) #日期被选中信号
        cw.currentPageChanged.connect(lambda year,month:print(year,month)) #当前页改变信号
        cw.selectionChanged.connect(lambda :print(cw.selectedDate())) #选中日期改变信号
        cw.clicked.connect(lambda val:print(val)) #日期被点击信号



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())