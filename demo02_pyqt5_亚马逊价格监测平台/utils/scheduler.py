class Scheduler(object):
    def __init__(self):
        self.thread_list=[] # 线程列表
        self.window=None
        self.terminate=False # 终止信号

    def start(self,BASE_DIR,window,fn_start,fn_stop,fn_counter,fn_error_counter):
        self.window=window
        self.terminate=False
        #获取表格中所有的数据，每一行创建一个线程去执行检查任务
        # window.table_widget.clearContents() # 清空表格内容
        for row in range(window.table_widget.rowCount()):
            asin=window.table_widget.item(row,0).text().strip()
            status=window.table_widget.item(row,6).text().strip()

            #写入日志文件
            import os
            log_folder=os.path.join(BASE_DIR,'log') #日志文件夹
            if not os.path.exists(log_folder):
                os.mkdir(log_folder)
            log_path=os.path.join(log_folder,'{}.log'.format(asin))



            #状态是待执行才创建线程
            if status!='待执行':
                continue
            #每一个线程 执行&状态实时的显示在表格中 信号+回调
            #创建线程类  根据型号 行号
            from .threads import TaskThread
            thread=TaskThread(self,log_path,row,asin,window)
            # #设置回调函数
            thread.start_sighal.connect(fn_start)
            thread.counter_sighal.connect(fn_counter)
            thread.error_counter_sighal.connect(fn_error_counter)
            thread.stop_sighal.connect(fn_stop)
            thread.start()
            self.thread_list.append(thread)

    def stop(self):
        self.terminate=True
        #创建一个线程  去监控线程列表 实时更新
        # self.update_status_message('检测停止')
        # self.window.update_status_message('检测停止')
        from .threads import StopThread
        thread=StopThread(self,self.window)
        thread.update_sighal.connect(self.window.update_status_message)
        thread.start()



    def destroy_thread(self,thread):
        '''线程销毁'''
        self.thread_list.remove(thread)

Scheduler=Scheduler() # 单例模式  创建一个类 实例化对象  别人使用时是同一个对象   Scheduler.stop() 和 Scheduler.start() 时同一个对象