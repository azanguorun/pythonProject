# coding:utf-8
"""
Project    : python_spiders
Time       ：2023/9/1 21:53v cccc
File       : 3_QPlainTextEdit纯文本编辑.py
content:
result:··
"""
import csv,json,math,time
from tqdm import tqdm
import requests
from threading import Thread
import threading

stat = '1'
print(stat)
t=int(time.time())
today = time.strftime("%y-%m-%d", time.localtime(int(t))) #今日日期

csrf='37f317ce7c817ba8507a3110b087b974'
SESSDATA='85151f10%2C1755909450%2C5e8ff%2A22CjDvAFGmLSY0YfKE9w5ILLg0pL3weTxFPWKiCi9Cj4G3rF6TL0mcVaNL1GoBA7XsSmoSVkxxcEVYdlFLOUYyc2tIaDRtYW9xa1E1VTVUSG1BNVh6dDZ1WDVZMnF4SnBKbTZtaFNCeV81RmlPYVgtbXg5MTVsQ3hDcDNqMU5EalYwMkVmTVlPSGtnIIEC'
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
    with open(f'./b站/'+fl+'.json', mode='r', encoding='utf-8-sig') as f:
        data_json = json.load(f)
        # 0:有价值 1:吃屎 2:静默 3:历史
        # stat=str(input('输出 0:有价值 1:吃屎 2:静默'))
        if stat=='3':
            last_time=data_json['ts3']#
        elif stat=='1' :
            last_time=data_json['ts1']
        elif stat=='2':  #
            last_time=data_json['ts2']
        # print(data_json)
        data=data_json['data']
        data=data[::-1]
        print(data)
        print(last_time)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(last_time))))
        global ss
        ss = 1
        for da in tqdm(range(len(data))):
            if da>=0:
                user_name=data[da]['name']
                user_id=data[da]['value']
                tt=data[da]['tt']
                state=data[da]['state']#0:有价值 1:吃屎 2:静默
                if state==stat:
                    offset = ''
                    # print(user_name)
                    ups = [
                        {
                            'uuid': '1',
                            'host_mid': '1088543164',
                            'up': '安run',
                            'phone': '18089480289',
                            'pass': 'az201210262300',
                            'csrf': '8140fe3fda6429a2b2e42e1c90a06b7c',
                            'SESSDATA': 'd2dd8dab%2C1754295362%2Cfb0aa%2A22CjCsli7ynSdB2G_bjAjL8kRQba3UXQRxm9ba2JrMtbeOxNMEG6QG31Pci0p7LThTKSwSVlByd0ZSdWZXWFFwOENKX3V5a1hIdWRxMHJVajRKVjh6N0JUalJzN3RYTHkwNjNnT1ByaUVJLWtoMU5fbWRoM2xmb3p3MXF5UUczdWxaWm5hRFNoY2R3IIEC',
                        }, {
                            'uuid': '2',
                            'host_mid': '505037436',
                            'up': '看的视频坚持评论',
                            'phone': '18394803575',
                            'pass': 'az201210262300',
                            'csrf': csrf,
                            'SESSDATA': SESSDATA,
                        }, {
                            'uuid': '3',
                            'host_mid': '1415819751',
                            'up': 'azanguorun',
                            'phone': '13689484968',
                            'pass': 'az201210262300',
                            'csrf': csrf,
                            'SESSDATA': SESSDATA
                        }
                    ]
                    ups1 = ups[0]
                    ups2 = ups[1]
                    # ups3 = ups[2]
                    if da%2==0:
                        up=ups[0]
                        pub_tt = Filedynamic('安run', up, last_time, user_id, user_name, tt, offset)
                    else:
                        up=ups[1]
                        pub_tt = Filedynamic('看的视频坚持评论', up, last_time, user_id, user_name, tt, offset)
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
                    #     pub_tt=thread1.get_result(0)
                    #     data[da]['tt']=pub_tt
                    #     ss = 1
                    data[da]['tt']=pub_tt
            else:
                print('过')
    get_json_data(stat,last_time,data,fl)

    tt=math.ceil((int(time.time())-t)/60)
    print('耗时为: '+str(tt)+'分钟')

#采集视频
def Filedynamic(threadName,up,last_time,user_id, user_name,tt,offset):
    url=f'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset={offset}&host_mid={user_id}&timezone_offset=-480&features=itemOpusStyle'
    headers = {
        "authority": "api.bilibili.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    SESSDATA = up['SESSDATA']
    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    resp=requests.get(url,headers=headers,cookies=cookies)

    time.sleep(1)
    pub_tt = tt

    # try:
    if '-352' != resp.json()['message']:
        if [] ==resp.json()['data']['items']:
            print('内容空',user_id, user_name)
        else:
            # if resp.json()['message']['items']!=[]:
            offset = resp.json()['data']['offset']  # 下一次动态请求的offset参数
            items = resp.json()['data']['items']  # 下一次动态请求的offset参数
            pub_ts = 0
            last_ts = 0
            name=''
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

                    # break


                last_ts = items[-1]['modules']['module_author']['pub_ts']  # 发布时间

            if int(last_time) <= last_ts and offset != '':
                last_tt=time.strftime("%Y-%m-%d %H:%M", time.localtime(int(last_time)))
                print(name,'读取下一页',last_tt,pub_tt)
                Filedynamic(threadName,up,last_time, user_id, user_name,tt, offset)
    else:
        print(threadName,'重新读取',user_name,resp.json(),url)
        time.sleep(60)
        Filedynamic(threadName,up,last_time, user_id, user_name,tt, offset)
    # except:
    #     time.sleep(30)
    #     print(url)
        # print(user_name)
        # print(resp.json())
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
    # csrf='e2b7ac967480c4da95551cc9c8885504'
    # SESSDATA='4f19beca%2C1754269246%2C3a9a7%2A22CjDOPIXirrWMVv1FQ3gfHWW4NxuydoUG3PvPOLrCXHpZNbQoy_qQYdQrsQfgDqW7C6oSVnctZkotX1dzWUZzWmhYbXZITWVhb0NjaVNiUk1LQk4tbkxsd1NKLXFvUm1JbnZucjZ3MTZUbTc2TXZ0bHBqVWhUNVJxRHdqYVFsNG5UTlNCMFo1bDJBIIEC'


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
    data = [response.json(),aid, name,mblog_url, title]
    print(data)
    if '-352'==response.json()['message']:
        time.sleep(30)
        print('再次请求点击')
        MyDynamic(threadName,aid, name,pub_tt, mblog_url, title)
    # print(response.text)
    # print(response)

def writefile(data):
    # 打开文件，以追加模式写入，文件路径为'b站/b站视频.csv'，编码方式为'utf-8'，换行符为空
    with open('./b站/b站视频.csv', mode='a', encoding='utf-8-sig', newline='') as f:
        # 创建一个csv写入器对象
        csv_write = csv.writer(f)
        # 将数据写入csv文件的当前行
        csv_write.writerow(data)

def get_json_data(stat,last_time,data,fl):
    with open(f'./b站/'+fl+'.json', 'r', encoding='utf-8-sig') as f:  # 使用只读模型，并定义名称为f
        params = json.load(f)  # 加载json文件


        if stat=='3':
            params["ts3"] = t
        elif stat=='1':
            params["ts1"] = t
        elif stat=='2':
            params["ts2"] = t

        params["old_ts"] = int(last_time)
        params["data"] = data

    with open(f'./b站/'+fl+'.json', 'w', encoding='utf-8-sig') as r:
        # 将dict写入名称为r的文件中k
        json.dump(params, r,ensure_ascii=False)
        # r.write(str(params))

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
if __name__ == '__main__':
    # 视频稍后观看
    readFocusFile()
