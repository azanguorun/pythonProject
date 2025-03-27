import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QDesktopWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtWidgets import *
import os
import json

BASE_DIR=os.path.dirname(os.path.realpath(sys.argv[0]))  # 获取当前文件的路径

STATUS_MAPPING = {
    0: '初始化中',
    1: '待执行',
    2: '正在执行',
    3: '完成并提醒',
    10: '异常并停止',
    11: '初始化失败',
} #状态映射


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFrame的学习")
        self.resize(1220, 300)

        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        #方向布局
        layout=QVBoxLayout()
        #创建布局
        layout.addLayout(self.init_header())
        layout.addLayout(self.init_form())
        layout.addLayout(self.init_table())
        layout.addLayout(self.init_footer())
        #给窗口设置元素的排列方式
        self.setLayout(layout)

    def init_header(self):
        # 1. 创建顶部菜单布局
        header_layout = QHBoxLayout()
        btn_start = QPushButton('开始')
        btn_start.clicked.connect(self.event_start_click)
        btn_stop = QPushButton('停止')
        btn_stop.clicked.connect(self.event_stop_click)

        btn_help = QPushButton('帮助') #QMessageBox.warning
        btn_help.clicked.connect(self.event_help_click)

        header_layout.addWidget(btn_start)
        header_layout.addWidget(btn_stop)
        header_layout.addStretch()  # 加弹簧分割
        header_layout.addWidget(btn_help)
        return header_layout

    def init_form(self):
        # 2. 创建上面标题布局
        form_layout = QHBoxLayout()
        self.txt_asin = QLineEdit()
        self.txt_asin.setPlaceholderText('请输入商品ID和价格')
        self.txt_asin.setText('B089233DF=100')
        btn_add = QPushButton('添加')
        # 设置按钮为默认按钮，按下 Enter 键时触发点击事件
        self.txt_asin.returnPressed.connect(btn_add.click)

        form_layout.addWidget(self.txt_asin)
        btn_add.clicked.connect(self.event_add_click) # 绑定事件
        form_layout.addWidget(btn_add)
        return form_layout

    def init_table(self):
        # 3. 创建中间内容布局
        table_layout = QHBoxLayout()
        self.table_widget=table_widget = QTableWidget(0, 8)
        table_header = [
            {"field": "asinssss", "text": "ASIN", "width": 120},
            {"field": "title", "text": "标题", "width": 150},
            {"field": "url", "text": "url", "width": 400},
            {"field": "price", "text": "价格", "width": 100},
            {"field": "success", "text": "成功次数", "width": 100},
            {"field": "error", "text": "失败次数", "width": 100},
            {"field": "status", "text": "状态", "width": 100},
            {"field": "frequency", "text": "频率(n/s)", "width": 100},
        ]
        for index, info in enumerate(table_header):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(index, item)
            table_widget.setColumnWidth(index, info['width'])

        file_path = os.path.join(BASE_DIR,'db', 'amazon.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        data_list=json.loads(data)
        current_row_count=table_widget.rowCount()
        for row_list in data_list:
            print(row_list)
            table_widget.insertRow(current_row_count) #插入一行
            for i,ele in enumerate(row_list):
                row_list[ele]=STATUS_MAPPING.get(row_list[ele]) if i==6 else row_list[ele]
                cell=QTableWidgetItem(str(row_list[ele])) #创建单元格
                if i in [0,4,5,6]:
                    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置 0,4,5,6 单元格不可编辑   要在创建单元格后设置
                table_widget.setItem(current_row_count,i,cell)
            current_row_count+=1


        #点击右击菜单 自动触发
        table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        table_widget.customContextMenuRequested.connect(self.table_right_menu)

        table_layout.addWidget(table_widget)
        return table_layout

    def init_footer(self):
        # 4. 创建底部菜单布局
        footer_layout = QHBoxLayout()

        lable_status = QLabel('未检测', self)
        self.lable_status = lable_status
        footer_layout.addWidget(lable_status)
        footer_layout.addStretch()

        btn_reinit = QPushButton('重新初始化')
        btn_reinit.clicked.connect(self.event_reset_click)
        footer_layout.addWidget(btn_reinit)


        btn_recheck = QPushButton('重新检测')
        footer_layout.addWidget(btn_recheck)

        btn_reset_count = QPushButton('重置次数')
        btn_reset_count.clicked.connect(self.event_reset_count_click)
        footer_layout.addWidget(btn_reset_count)

        btn_delete = QPushButton('删除')
        btn_delete.clicked.connect(self.event_delete_click)
        footer_layout.addWidget(btn_delete)

        btn_alert = QPushButton('邮箱SMTP报警配置')
        btn_alert.clicked.connect(self.event_alert_click)
        footer_layout.addWidget(btn_alert)

        btn_proxy = QPushButton('代理配置')
        btn_proxy.clicked.connect(self.event_proxy_click)
        footer_layout.addWidget(btn_proxy)

        return footer_layout

    def event_add_click(self):
        print('添加按钮被点击了')
        #1,获取输入框的内容
        test=self.txt_asin.text()
        test=test.strip()
        if not test:
            QMessageBox.warning(self,'警告','请输入商品ID')
            return
        asin,price=test.split('=')
        price=float(price)
        #2.加入到表格中
        new_row_list=[asin,'','',price,0,0,0,5]

        current_row_count=self.table_widget.rowCount() #获取当前行数
        self.table_widget.insertRow(current_row_count) #插入一行
        for i, ele in enumerate(new_row_list):
            ele = STATUS_MAPPING.get(ele) if i == 6 else ele
            cell = QTableWidgetItem(str(ele))  # 创建单元格
            if i in [0, 4, 5, 6]:
                cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置 0,4,5,6 单元格不可编辑   要在创建单元格后设置
            self.table_widget.setItem(current_row_count, i, cell)

        #3.通过爬虫获取标题
        # 注意：不能在主线程中执行耗时操作  创建子线程 爬取到数据后 再更新到表格中
        # 注意：传入参数 参数要在self 的前面
        from utils.threads import NewTaskThread
        news_thread=NewTaskThread(current_row_count,asin,self)

        news_thread.success.connect(self.init_task_success_callback)
        news_thread.error.connect(self.init_task_error_callback)
        news_thread.start() #启动线程

    def init_task_success_callback(self,index,asin,title,url):
        print('爬取成功',index,asin,title,url)
        #1.更新表格中的标题
        cell_title=QTableWidgetItem(title)
        self.table_widget.setItem(index,1,cell_title)
        #2.更新表格中的url
        cell_url=QTableWidgetItem(url)
        self.table_widget.setItem(index,2,cell_url)
        #3.更新表格中的状态
        cell_status=QTableWidgetItem(STATUS_MAPPING.get(1))
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置 0,4,5,6 单元格不可编辑   要在创建单元格后设置
        self.table_widget.setItem(index,6,cell_status)

        self.txt_asin.clear() #清空输入框

    def init_task_error_callback(self,index,asin,title,url):
        #1.更新表格中的标题
        cell_title=QTableWidgetItem(title)
        self.table_widget.setItem(index,1,cell_title)
        #2.更新表格中的url
        cell_url=QTableWidgetItem(url)
        self.table_widget.setItem(index,2,cell_url)
        #3.更新表格中的状态
        print('爬取失败',index,asin,title,url)
        cell_status=QTableWidgetItem(STATUS_MAPPING.get(11))
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置 0,4,5,6 单元格不可编辑   要在创建单元格后设置
        self.table_widget.setItem(index,6,cell_status)

    def event_reset_click(self):
        '''重新初始化'''
        row_list=self.table_widget.selectionModel().selectedRows()
        if not row_list:
            QMessageBox.warning(self,'警告','请选择要重置的行')
            return

        for row in row_list:
            index=row.row()
            print(index)
            asin=self.table_widget.item(index,0).text()
            #1.更新表格中的状态
            cell_status = QTableWidgetItem(STATUS_MAPPING.get(0))
            cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置 0,4,5,6 单元格不可编辑   要在创建单元格后设置
            self.table_widget.setItem(index, 6, cell_status)

            #2.创建线程初始化
            from utils.threads import NewTaskThread
            news_thread = NewTaskThread(index, asin, self)

            news_thread.success.connect(self.init_task_success_callback)
            news_thread.error.connect(self.init_task_error_callback)
            news_thread.start()  # 启动线程

    def event_reset_count_click(self):
        '''重置次数'''
        row_list=self.table_widget.selectionModel().selectedRows()
        if not row_list:
            QMessageBox.warning(self,'警告','请选择要重置的行')
            return

        for row in row_list:
            index=row.row()
            print(index)

            #1.更新表格中的状态
            cell_status = QTableWidgetItem('0')
            cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置 0,4,5,6 单元格不可编辑   要在创建单元格后设置
            self.table_widget.setItem(index, 4, cell_status)
            cell_status = QTableWidgetItem('0')
            cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置 0,4,5,6 单元格不可编辑   要在创建单元格后设置
            self.table_widget.setItem(index, 5, cell_status)

    def event_delete_click(self):
        '''删除'''
        row_list=self.table_widget.selectionModel().selectedRows()
        if not row_list:
            QMessageBox.warning(self,'警告','请选择要重置的行')
            return

        row_list.reverse() #倒序
        for row in row_list:
            self.table_widget.removeRow(row.row())

    def event_alert_click(self):
        '''邮箱SMTP报警配置'''
        #创建弹窗
        from utils.dialog import AlertDialog
        dialog=AlertDialog()
        dialog.setWindowModified(Qt.ApplicationModal) #设置为模态窗口
        dialog.exec_()

    def event_proxy_click(self):
        '''代理配置'''
        #创建弹窗
        from utils.dialog import ProxyDialog
        dialog=ProxyDialog()
        dialog.setWindowModified(Qt.ApplicationModal) #设置为模态窗口
        dialog.exec_()

    def table_right_menu(self,pos):
        '''显示右击菜单'''
        select_row_list=self.table_widget.selectedItems()
        if len(select_row_list)!=1:
            return


        #1.创建菜单
        menu=QMenu()
        item_copy=menu.addAction('复制')
        item_log=menu.addAction('查看日志')
        item_log_clear=menu.addAction('清空日志')
        #2.菜单显示的位置
        action=menu.exec_(self.table_widget.mapToGlobal(pos)) #显示菜单  要在当前窗口中显示

        if action==item_copy:
            print('复制') #B089233DF
            clipboard=QApplication.clipboard()
            clipboard.setText(select_row_list[0].text())
        elif action==item_log:
            print('查看日志')
            from utils.dialog import LogDialog

            dialog=LogDialog(select_row_list[0].text())
            dialog.setWindowModality(Qt.ApplicationModal) #设置为模态窗口
            dialog.exec_()

        elif action==item_log_clear:
            print('清空日志')
            asin=self.table_widget.item(select_row_list[0].row(),0).text().strip()

            file_path = os.path.join('log', '{}.log'.format(asin))
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                QMessageBox.warning(self,'警告','日志文件不存在')

    def event_start_click(self):
        '''开始'''
        from utils.scheduler import Scheduler
        self.update_status_message('检测开始','color:green;')
        Scheduler.start()

    def event_stop_click(self):
        '''停止  执行中的线程逐一停止'''
        from utils.scheduler import Scheduler
        self.update_status_message('检测停止','color:red;')
        Scheduler.stop()


    def update_status_message(self,message,color):
        '''更新状态信息'''
        self.lable_status.setText(message)
        self.lable_status.setStyleSheet(color)
        self.lable_status.repaint()


    def event_help_click(self):
        '''帮助'''
        print('帮助')
        QMessageBox.about(self,'帮助','帮助')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())