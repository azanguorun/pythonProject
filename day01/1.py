# coding:utf-8
"""
Project    : python_spiders
Time       ：2023/9/1 21:53
File       : 3_QPlainTextEdit纯文本编辑.py
content:
result:··
"""
#获取粉丝数
import csv,json,math,time
from tqdm import tqdm
import requests
from threading import Thread
import threading

# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas


endday=int(time.time())
today = time.strftime("%y-%m-%d", time.localtime(int(endday))) #今日日期

# csrf='fd1905e6b3b26ba3a2d54af25c5d2337'
# SESSDATA='d106b464%2C1738315585%2C0a103%2A82CjC2Y2Zma0OS4exUoz1TjlIMSOwKLBDu6TSUwMCzQ1ivrvm4zO1cilj1NJPPvBs7HYMSVk5SR0VSUVZ4WU9MMDV1dnFzZEVxMnkzS3JJeFpvRjU0RmlXREtfM3Y1UE9pci1ENUdTWnNkTlcyNjVKbDQyZF95T2t5WnYxQTVJSW8yQjJ6Z0xzOGZnIIEC'
#
#
# cookies = {投诉
#     'SESSDATA': SESSDATA,
#     'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
# }

fl='关注2'
class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        time.sleep(2)
        self.result = self.func(*self.args)

    def get_result(self):
        threading.Thread.join(self)  # 等待线程执行完毕
        try:
            return self.result
        except Exception:
            return None

def readFocusFile():
    with open(f'b站/'+fl+'.json', mode='r', encoding='utf-8') as f:
        data_json = json.load(f)
        last_time=data_json['ts']
        data=data_json['data']
        print(last_time)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(last_time))))
        global ss
        ss = 1
        for da in tqdm(range(len(data))):
            user_name=data[da]['name']
            user_id=data[da]['value']
            tt=data[da]['tt']
            offset = ''
            # print(user_name)
            ups = [
                {
                    'uuid': '1',
                    'host_mid': '1088543164',
                    'up': '安run',
                    'phone': '18089480289',
                    'pass': 'az201210262300',
                    'csrf': 'fd1905e6b3b26ba3a2d54af25c5d2337',
                    'SESSDATA': 'd106b464%2C1738315585%2C0a103%2A82CjC2Y2Zma0OS4exUoz1TjlIMSOwKLBDu6TSUwMCzQ1ivrvm4zO1cilj1NJPPvBs7HYMSVk5SR0VSUVZ4WU9MMDV1dnFzZEVxMnkzS3JJeFpvRjU0RmlXREtfM3Y1UE9pci1ENUdTWnNkTlcyNjVKbDQyZF95T2t5WnYxQTVJSW8yQjJ6Z0xzOGZnIIEC',
                }, {
                    'uuid': '2',
                    'host_mid': '505037436',
                    'up': '看的视频坚持评论',
                    'phone': '18394803575',
                    'pass': 'az201210262300',
                    'csrf': 'd608baeb1072c2630f7e76bb8510464c',
                    'SESSDATA': '6996eb28%2C1738116379%2C94a84%2A82CjAn1PjTiaYRpZGDRiLH5Gig68IyXTvTLjeRXe-pTn1gEvhdnwe4IcsXSvDSk4uRW4MSVkVPRnoyOEtsaHdvbktKUU1LVkQxOFFIdE5aRGMwR1lEeUVEUHNfVjkyUXRVYXFyMjktTWdEcEFqY196d0VJWk91Tlo5MVZtNDFFTzdsbDNheTlva0pBIIEC',
                }, {
                    'uuid': '3',
                    'host_mid': '1415819751',
                    'up': 'azanguorun',
                    'phone': '13689484968',
                    'pass': 'az201210262300',
                    'csrf': 'c65b1a7f651b27d34f95b143e609c1ad',
                    'SESSDATA': 'ef8070b8%2C1740792854%2Cfa010%2A91CjCsEk5rBB9ru2ak8dEgVsP3BCSBO0eomgpoP7XtKrsTuwwULtjwstY9f6rZ73nd3e8SVjFqclBDdWlDUXAxd1dFaW9zNGUtYm9DX3hnV0NicDN4UEZBNEJtMnhpV1paNExEOFhtQ0NpRml3WTFOenFBM0xweWxVaXoyVkN4US16UlBmV0p3UDZnIIEC'
                }
            ]
            # ups1 = ups[0]
            # ups2 = ups[1]
            # ups3 = ups[2]
            # if ss == 1:
            #     thread1 = MyThread(Filedynamic,
            #                      args=("thread_1", ups1, last_time, user_id, user_name, offset))  # 线程1：执行任务打印4个a
            #     thread1.start()  # 线程1开始
            #     thread1.join()  # 等待线程1结束
            #     pub_tt=thread1.get_result()
            #     data[da]['tt'] = pub_tt
            #     ss = 2
            # elif ss == 2:
            #     thread2 = MyThread(Filedynamic,
            #                      args=("thread_2", ups2, last_time, user_id, user_name, offset))  # 线程2：执行任务打印2个b
            #     thread2.start()  # 线程2开始 3_1415819751_azanguorun_b站执行日期.csv
            #     thread2.join()  # 等待线程2结束
            #     thread2.get_result()
            #     pub_tt=thread1.get_result()
            #     data[da]['tt']=pub_tt
            #     ss = 1
            pub_tt=Filedynamic('threadName', last_time, user_id, user_name,tt, offset)
            data[da]['tt']=pub_tt
    get_json_data(last_time,data,fl)

    tt=math.ceil((int(time.time())-endday)/60)
    print('耗时为: '+str(tt)+'分钟')


#采集视频
def Filedynamic(threadName,last_time,user_id, user_name,tt,offset):
    SESSDATA =  '6996eb28%2C1738116379%2C94a84%2A82CjAn1PjTiaYRpZGDRiLH5Gig68IyXTvTLjeRXe-pTn1gEvhdnwe4IcsXSvDSk4uRW4MSVkVPRnoyOEtsaHdvbktKUU1LVkQxOFFIdE5aRGMwR1lEeUVEUHNfVjkyUXRVYXFyMjktTWdEcEFqY196d0VJWk91Tlo5MVZtNDFFTzdsbDNheTlva0pBIIEC'
    url=f'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset={offset}&host_mid={user_id}&timezone_offset=-480&features=itemOpusStyle'
    headers = {
        "authority": "api.bilibili.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    resp=requests.get(url,headers=headers,cookies=cookies)

    time.sleep(1.5)
    pub_tt = tt

    try:
        if '-352' != resp.json()['message']:
            offset = resp.json()['data']['offset']  # 下一次动态请求的offset参数
            items = resp.json()['data']['items']  # 下一次动态请求的offset参数
            pub_ts = 0
            for item in items:
                pub_ts = item['modules']['module_author']['pub_ts']  # 发布时间

                name = item['modules']['module_author']['name']  # 发布时间

                mblog_type = item['type']
                id_str = item['id_str']
                # print(mblog_type)
                if mblog_type == 'DYNAMIC_TYPE_AV' and int(last_time) <= pub_ts:
                    title = item['modules']['module_dynamic']['major']['archive']['title']  # 发布时间

                    aid = item['modules']['module_dynamic']['major']['archive']['aid']
                    bvid = item['modules']['module_dynamic']['major']['archive']['bvid']
                    text = item['modules']['module_dynamic']['major']['archive']['badge']['text']
                    # if text == '投稿视频':
                    pub_tt = time.strftime("%Y-%m-%d %H:%M", time.localtime(int(pub_ts)))
                    if text == '投稿视频':
                        mblog_url = 'https://t.bilibili.com/' + id_str  # 动态的链接
                    # exit()
                        MyDynamic(threadName,aid, name,pub_tt,mblog_url, title)
                        data = [mblog_url, name, title]
                        writefile(data)

                    break
            if int(last_time) <= pub_ts and offset != '':
                last_tt=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(last_time)))
                print(threadName,'读取下一页',last_time,pub_ts,last_tt,pub_tt)
                Filedynamic(threadName,last_time, user_id, user_name,tt, offset)
        else:
            print(threadName,'重新读取',user_name,resp.json())
            time.sleep(30)
            Filedynamic(threadName,last_time, user_id, user_name,tt, offset)
    except:
        time.sleep(30)
        print(url)
        print(user_name)
        print(resp.json())
    # print(user_id, user_name, pub_tt)
    return pub_tt
#添加稍后观看
def MyDynamic(threadName,aid, name,pub_tt,mblog_url, title):
    # time.sleep(4)
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    csrf='fd1905e6b3b26ba3a2d54af25c5d2337'
    SESSDATA='d106b464%2C1738315585%2C0a103%2A82CjC2Y2Zma0OS4exUoz1TjlIMSOwKLBDu6TSUwMCzQ1ivrvm4zO1cilj1NJPPvBs7HYMSVk5SR0VSUVZ4WU9MMDV1dnFzZEVxMnkzS3JJeFpvRjU0RmlXREtfM3Y1UE9pci1ENUdTWnNkTlcyNjVKbDQyZF95T2t5WnYxQTVJSW8yQjJ6Z0xzOGZnIIEC'


    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    url = "https://api.bilibili.com/x/v2/history/toview/add"

    data = {
        "aid": str(aid),
        "jsonp": "jsonp",
        "csrf": csrf
    }

    response = requests.post(url, headers=headers,cookies=cookies, data=data)
    data = [threadName,aid, name,mblog_url, title]
    print(data)
    if '-352'==response.json()['message']:
        time.sleep(30)
        print('再次请求点击')
        MyDynamic(threadName,aid, name,pub_tt, mblog_url, title)
    # print(response.text)
    # print(response)

def writefile(data):
    # 打开文件，以追加模式写入，文件路径为'b站/b站视频.csv'，编码方式为'utf-8'，换行符为空
    with open('b站/b站视频.csv', mode='a', encoding='utf-8', newline='') as f:
        # 创建一个csv写入器对象
        csv_write = csv.writer(f)
        # 将数据写入csv文件的当前行
        csv_write.writerow(data)

def get_json_data(last_time,data,fl):
    with open(f'b站/'+fl+'.json', 'r', encoding='utf-8') as f:  # 使用只读模型，并定义名称为f
        params = json.load(f)  # 加载json文件

        # print(params)
    params["ts"] = endday
    params["old_ts"] = int(last_time)
    params["data"] = data

    with open(f'b站/'+fl+'.json', 'w', encoding='utf-8') as r:
        # 将dict写入名称为r的文件中
        json.dump(params, r,ensure_ascii=False)
        # r.write(str(params))

if __name__ == '__main__':
    # 视频稍后观看
    readFocusFile()