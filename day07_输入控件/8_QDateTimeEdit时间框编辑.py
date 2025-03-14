from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("QFrame的学习")
        self.setup_ui()

    def setup_ui(self):
        # dte=QDateTimeEdit(self)
        dte=QDateTimeEdit(QDateTime.currentDateTime(),self)
        dte=QDateTimeEdit(QTime.currentTime(),self)
        dte.move(100,100)
        dte.resize(200,30)
        dte.setDateTime(QDateTime.currentDateTime()) #设置当前日期时间
        dte.setDisplayFormat("yyyy-MM-dd HH:mm:ss") #设置显示格式

        print(dte.sectionCount()) #获取日期时间的部分数量

        btn=QPushButton(self)
        btn.move(100,150)
        btn.setText("测试按钮")
        # btn.clicked.connect(lambda :print(dte.currentSectionIndex())) #获取当前选中的部分的索引

        def test():
            dte.setCurrentSectionIndex(3) #设置当前选中的部分的索引
            dte.setFocus() #设置焦点

            dte.setCurrentSection(QDateTimeEdit.DaySection) #设置当前选中的部分

            dte.setMaximumDateTime(QDateTime(2020,12,12,12)) #设置最大日期时间
            dte.setMaximumDateTime(QDateTime.currentDateTime().addYears(-3)) #设置最大日期时间

            dte.setCalendarPopup(True) #设置日历弹出
            dte.setDateRange(QDate(2020,1,1),QDate(2020,12,31)) #设置日期范围
            dte.setTimeRange(QTime(0,0),QTime(23,59,59)) #设置时间范围

        btn.clicked.connect(test) #获取当前选中的部分的索引

        print(dte.sectionCount())
        dte.setCalendarPopup(True) #设置日历弹出
        dte.dateTimeChanged.connect(lambda val:print("日期时间改变了",val)) #日期时间改变了
        dte.dateChanged.connect(lambda val:print("日期改变了",val)) #日期改变了
        dte.timeChanged.connect(lambda val:print("时间改变了",val)) #时间改变了q


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())