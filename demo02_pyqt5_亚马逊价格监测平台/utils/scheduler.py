class Scheduler(object):
    def __init__(self):
        self.thread_list=[]

    def start(self):
        #获取表格中所有的数据，每一行创建一个线程去执行检查任务
        #每一个线程 执行&状态实时的显示在表格中 信号+回调
        pass
    def stop(self):
        pass

Scheduler=Scheduler() # 单例模式  创建一个类 实例化对象  别人使用时是同一个对象   Scheduler.stop() 和 Scheduler.start() 时同一个对象