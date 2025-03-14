import threading
asf = list(range(20))



def test (name,a):
    print(name,a)

for a in asf:
    thread1 = threading.Thread(name='t1',target= test,args=('t1',a))
    thread2 = threading.Thread(name='t2',target= test,args=('t2',a))
    thread1.start()   #启动线程1
    thread2.start()   #启动线程2

import threading
import time


def read_data(data_list, start, end):
    for i in range(start, end):
        # 处理数据列表中的数据
        print(f"Thread {threading.current_thread().name} is processing item {data_list[i]}")
        time.sleep(0.1)  # 模拟处理数据的时间


def goto_threading():
    data_list = list(range(20))  # 示例数据列表
    thread_count = 2  # 线程数
    chunk_size = len(data_list) // thread_count  # 计算每个线程处理的数据大小
    print(chunk_size)
    threads = []
    for i in range(thread_count):
        start = i * chunk_size
        end = start + chunk_size if i < thread_count - 1 else len(data_list)
        t = threading.Thread(target=read_data, args=(data_list, start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # 等待所有线程完成


if __name__ == "__main__":
    goto_threading()