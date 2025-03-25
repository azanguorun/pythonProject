# coding:utf-8
"""
Project    : python_spiders
Time       ：2024/7/5 16:35
File       : 3_QCommandLinkButton指向按钮.py
content:
result:
"""


import math,re
import random

import pandas as pd
import csv
import json
import time
from tqdm import tqdm
import requests
from threading import Thread


endday=int(time.time())

# 读取上次操作时间 输出日期
def readAction_0_Time():
    with open('../day02/b站/0_b站执行日期.csv', mode='r', encoding='utf-8') as f:
        last_line = f.readlines()[-1]
        last_time = last_line.split('结束时间戳:')[1]
        ltime = int(time.time() - 24 * 60 * 60 * 3)
        if int(last_time) <= ltime:
            return ltime
        else:
            return last_time

#判断地址是否已经存在
def get_if_csv(mblog_url):
    mblog_ids=str(mblog_url).split('/')[-1]
    with open(f'../day02/b站/0_b站抽奖池.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if mblog_ids  in row:
               return False
            else:
               return True

#验证地址数据
def get_lottery_id(mblog_url):
    mblog_id=mblog_url.split('/')[-1]
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "^cookie": "buvid3=EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc; b_nut=1694446923; i-wanna-go-back=-1; b_ut=7; _uuid=4CAD10A17-7E6B-EF97-CDBE-F310B8161AC7423403infoc; rpdid=^|(RY~)luk~m0J'uYmRRR~^|Ru; header_theme_version=CLOSE; DedeUserID=1088543164; DedeUserID__ckMd5=c3356377a0b6b007; hit-new-style-dyn=1; hit-dyn-v2=1; is-2022-channel=1; buvid4=C84ECE92-8A32-B86C-DE09-29BCA0D25F7740018-022031318-VWnNN8EbnlfakM8T6u0aEA^%^3D^%^3D; buvid_fp_plain=undefined; LIVE_BUVID=AUTO7616949985261915; enable_web_push=DISABLE; CURRENT_BLACKGAP=0; FEED_LIVE_VERSION=V_HEADER_LIVE_NEW_POP; PVID=1; CURRENT_FNVAL=4048; fingerprint=eb3974f202e6e9768f58fa68b0b3381b; CURRENT_QUALITY=80; buvid_fp=eb3974f202e6e9768f58fa68b0b3381b; SESSDATA=4bd2c3b4^%^2C1735739929^%^2Cf34a5^%^2A72CjCs44eQjROOi6_YIE5uQFO8sWAYbvGJzLkb5lJAeLpjTreTCusG2tcoIcXk_ydVpSISVlpFQlZaeHV3OVJSVnJKNkR3R0VCOUtPSDBXa1dsclFONXhTZXpIQzBLNnNvUTQ2Qm1Na21lNFBPYkNmUDNwYjl3Und4T2htWTBiQVpKcmRzMkRlOVN3IIEC; bili_jct=3d04d2d0d32fd333ec0cfdd5d17bee33; sid=81xdykjc; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjA0NDczNjMsImlhdCI6MTcyMDE4ODEwMywicGx0IjotMX0.MNmT_MHLeLOzxY8HrZsB4hG-xo4u8XWramv0h-rPxYw; bili_ticket_expires=1720447303; home_feed_column=5; browser_resolution=1536-703; b_lsid=5FFD7D6B_19091858CEA; bp_t_offset_1088543164=951741001624453120^",
        "origin": "https://www.bilibili.com",
        "priority": "u=1, i",
        "referer": "https://www.bilibili.com/",
        "^sec-ch-ua": "^\\^Not/A)Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^126^^, ^\\^Google",
        "sec-ch-ua-mobile": "?0",
        "^sec-ch-ua-platform": "^\\^Windows^^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    url = "https://api.vc.bilibili.com/lottery_svr/v1/lottery_svr/lottery_notice?business_id="+str(mblog_id)+"&business_type=1"
    response = requests.get(url, headers=headers)
    resp_json = response.json()
    resp_data = resp_json['data']
    try:
        lottery_time = resp_data['lottery_time']

        today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(lottery_time))  # 今日日期

        # 获取一等奖描述和发送者 UID
        first_prize_cmt = resp_data.get('first_prize_cmt')
        sender_uid = resp_data.get('sender_uid')

        # 获取二等奖描述，若不存在则设为 "无"
        second_prize_cmt = resp_data.get('second_prize_cmt', "无")

        # 获取三等奖描述，若不存在则设为 "无"
        third_prize_cmt = resp_data.get('third_prize_cmt', "无")

        # 检查抽奖时间是否在当前时间之后
        if lottery_time >=int(time.time()):
            #执行日期
            data=[0,mblog_url,mblog_id,sender_uid,lottery_time,today,first_prize_cmt, second_prize_cmt, third_prize_cmt]
            print(data)
            csv_files = [f'./b站/0_b站抽奖池.csv', f'./b站/0_b站历史抽奖池.csv']
            for csv_file in csv_files:
                try:
                    with open(csv_file, mode='a', encoding='utf-8', newline='') as f:
                        csv_write = csv.writer(f)
                        csv_write.writerow(data)
                except FileNotFoundError:
                    print(f"文件 {csv_file} 未写入。")
    except:
        print('非官方,预约,转发 地址{}  地址{}'.format(mblog_url,url))

#获取锦鲤数据
def get_article_id():
    last_time=readAction_0_Time()  #获取上次执行结束时间
    mids=[['_大锦鲤_','226257459'],['不锈钢炒锅','3493086911007529'],['西伯利亞倉鼠','5536630']]
    mblog_urls = []
    for mid in mids:
        time.sleep(2)
        # up主页
        article_url = f'https://api.bilibili.com/x/space/article?mid={mid[1]}&pn=1&ps=12'
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        }
        resp = requests.get(article_url, headers=headers)
        article_datas = resp.json()['data']['articles']
        for article_data in article_datas:
            #获取专栏id
            article_id=article_data['id']
            publish_time = article_data['publish_time']
            # 如果  上次执行时间 2025/2/16  < 专栏时间  2025/2/13
            if int(last_time) < publish_time:
                cv_url = f'https://www.bilibili.com/read/cv{article_id}/?spm_id_from=333.999.0.0'
                html_data = requests.get(cv_url, headers=headers).text
                data=re.findall('https://t.bilibili.com/([0-9]{19})', str(html_data))
                opus_data=re.findall('https://www.bilibili.com/opus/([0-9]{19})', str(html_data))

                if opus_data != None :
                    opus_url=['https://www.bilibili.com/opus/' + item for item in opus_data]
                else:
                    opus_url=[]
                if data != None:
                    data_url=['https://t.bilibili.com/' + item for item in data]
                else:
                    data_url=[]
                mblog_urls=mblog_urls+opus_url+data_url
            else:
                print('锦鲤:{} 无抽奖内容 专栏时间:{}'.format(mid[0],time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(publish_time))))
                break
    mblog_urls=list(set(mblog_urls))
    print('抽奖数量：{},地址：{}'.format(len(mblog_urls),mblog_urls))

    for mblog_url in mblog_urls:
        if get_if_csv(mblog_url):
            get_lottery_id(mblog_url)

#获取机器人数据
def get_upper_offset():
    host_mids = ['1218591431', '74105384', '12058031', '3546685089254178', '396902231',
                 '3461577258830253','1233410593','3493277005253367'
                 ,'181046678','158120381','174356526','281690207','44472232']
    cs=0
    for i in tqdm(range(12)):
        offset=''
        get_upper_id(cs,i,host_mids[i],offset)
    print('机器人抽奖',cs)

#获取机器人数据
def get_upper_id(cs,i,host_mid,offset):
    last_time = readAction_0_Time()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset="+str(offset)+"&host_mid="+str(host_mid)
    cookies = {
        'SESSDATA': 'd2dd8dab%2C1754295362%2Cfb0aa%2A22CjCsli7ynSdB2G_bjAjL8kRQba3UXQRxm9ba2JrMtbeOxNMEG6QG31Pci0p7LThTKSwSVlByd0ZSdWZXWFFwOENKX3V5a1hIdWRxMHJVajRKVjh6N0JUalJzN3RYTHkwNjNnT1ByaUVJLWtoMU5fbWRoM2xmb3p3MXF5UUczdWxaWm5hRFNoY2R3IIEC',
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    resp = requests.get(url, headers=headers,cookies=cookies)
    try:
        resp_json = resp.json()
        resp_data = resp_json['data']
        offset = resp_data['offset']  # 下一次动态请求的offset参数
        items = resp_data['items']
        for item in items:
            if 'orig' in item:
                id_str = item['orig']['id_str']  # 动态id
                pub_ts = item['modules']['module_author']['pub_ts']  # 动态pub_ts
                sender_uid = item['orig']['modules']['module_author']['mid']

                item_type = item['type']  # 动态类型 DYNAMIC_TYPE_DRAW 文本 DYNAMIC_TYPE_FORWARD 转发  DYNAMIC_TYPE_AV 视频
                if item_type in ('DYNAMIC_TYPE_DRAW', 'DYNAMIC_TYPE_FORWARD'):
                    #抽奖文本中有日期
                    desc = item['orig']['modules']['module_dynamic']['desc']
                    if desc is not None:
                        text = desc.get('text', '').replace('\r', '').replace('\n', '')  # Published content
                    else:
                        text = ''
                    text = re.findall(r"(\d{1,2}月\d{1,2}日)",text)
                    if len(text)>0:
                        try:
                            text=text[-1]
                            today = '2025-' + text + ' 00:00:00'
                            today = today.replace('月', '-').replace('日', '')
                            dt = time.strptime(today, '%Y-%m-%d %H:%M:%S')
                            lottery_time = int(time.mktime(dt))
                            if lottery_time >= int(time.time()):
                                mblog_url = 'http://www.bilibili.com/opus/' + id_str
                                if 1 == get_if_csv(mblog_url):
                                    data = [0, mblog_url, id_str, sender_uid, lottery_time, today, '无', '无', '无']
                                    cs += 1
                                    print('{} {} {}'.format(i, host_mid, data))
                                    csv_files = [f'./b站/0_b站抽奖池.csv', f'./b站/0_b站历史抽奖池.csv']
                                    for csv_file in csv_files:
                                        try:
                                            with open(csv_file, mode='a', encoding='utf-8', newline='') as f:
                                                csv_write = csv.writer(f)
                                                csv_write.writerow(data)
                                        except FileNotFoundError:
                                            print(f"文件 {csv_file} 未写入。")
                        except ValueError:
                            print('日期格式错误',text)

                    else:
                        if pub_ts >= int(time.time()):
                            #文本中没有日期  去重
                            mblog_url='https://t.bilibili.com/'+id_str
                            today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(pub_ts))  # 今日日期
                            data = [0, mblog_url, id_str, sender_uid, pub_ts, today, '无', '无', '无']
                            cs+=1
                            print('{} {} {}'.format(i, host_mid, data))
                            csv_files = [f'./b站/0_b站抽奖池.csv', f'./b站/0_b站历史抽奖池.csv']
                            for csv_file in csv_files:
                                try:
                                    with open(csv_file, mode='a', encoding='utf-8', newline='') as f:
                                        csv_write = csv.writer(f)
                                        csv_write.writerow(data)
                                except FileNotFoundError:
                                    print(f"文件 {csv_file} 未写入。")


        pub_ts = resp_data['items'][-1]['modules']['module_author']['pub_ts']
        #机器人最后的时间大于  执行时间
        if int(last_time) <= pub_ts:
            time.sleep(3)
            print('进行下一页',host_mid,pub_ts,offset)
            get_upper_id(cs,i,host_mid, offset)
    except json.JSONDecodeError:
        # 处理无法将响应内容解析为 JSON 格式的异常
        print("获取数据失败: 无法解析响应为 JSON 格式")

#最终整理文件
def sort_0_csv():
    data = pd.read_csv(f'../day02/b站/0_b站抽奖池.csv')
    sort_data = data.sort_values('抽奖时间戳', ascending=True)
    sort_data.to_csv(f'./b站/0_b站抽奖池.csv', index=False)

    frame = pd.read_csv('../day02/b站/0_b站抽奖池.csv', engine='python', encoding='utf-8')
    #状态,链接,活动id,upid,抽奖时间戳,抽奖时间,一等奖,二等奖,三等奖
    data = frame.drop_duplicates(subset=['活动id', '抽奖时间戳'], keep='last', inplace=False)
    data.to_csv('./b站/0_b站抽奖池.csv', index=0, encoding='utf-8')  # index=0, 去除索引
    # 定义要过滤的 upid 列表
    exclude_upid = ['397287828', '397287821', '397287822']

    data = pd.read_csv('../day02/b站/0_b站抽奖池.csv', encoding='utf-8')
    # 过滤掉包含指定 upid 的行
    data = data[~data['upid'].astype(str).str.contains('|'.join(exclude_upid))]
    # 将过滤后的数据写回 CSV 文件
    data.to_csv('./b站/0_b站抽奖池.csv', index=False, encoding='utf-8')
    print('文件去重完成,文件过滤完成')

    cs=pd.read_csv(f'../day02/b站/0_b站抽奖池.csv').shape[0]
    last_time = readAction_0_Time()  # 获取1_1088543164_看的视频坚持评论_b站执行日期文件日期
    ts = int(time.time())
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(last_time)))
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endday))
    sc='执行时间:'+start+'--'+end+' 个数:'+str(cs)+' 耗时:'+str(round(((ts-endday)%3600)/60))+'分'+str((ts-endday)%60)+'秒 结束时间戳:'+str(endday)
    print(sc)
    with open('../day02/b站/0_b站执行日期.csv', mode='a', encoding='utf-8', newline='') as f:
        f.write(sc)
        f.write('\n')

#抽奖
def goto_lottery():
    ups=[
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
            'csrf': '1630c8ba5640316c7bb93c2b20b9b1e5',
            'SESSDATA': 'a176cbde%2C1755313594%2C7f463%2A22CjDAcJaZQmCaduIGZGqsfadbyd6mc1OuMWnuh9L4XNiVNUTYtn9ulC0D6sNB6B10el8SVmVSY3VWYnYxOE8xQl9kT25hSVFTZENmaWktVjViX1YxbWNUYzFCUW8xMUJmZ01QTm5qSERBMjBWUTRyNzBzcVl3NEh1bGFzNzc2LTVpUmZXSkNscW1BIIEC',
        }, {
        'uuid': '3',
        'host_mid': '1415819751',
        'up': 'azanguorun',
        'phone': '13689484968',
        'pass': 'az201210262300',
        'csrf':'c65b1a7f651b27d34f95b143e609c1ad',
        'SESSDATA':'ef8070b8%2C1740792854%2Cfa010%2A91CjCsEk5rBB9ru2ak8dEgVsP3BCSBO0eomgpoP7XtKrsTuwwULtjwstY9f6rZ73nd3e8SVjFqclBDdWlDUXAxd1dFaW9zNGUtYm9DX3hnV0NicDN4UEZBNEJtMnhpV1paNExEOFhtQ0NpRml3WTFOenFBM0xweWxVaXoyVkN4US16UlBmV0p3UDZnIIEC'
        }
    ]
    ups1=ups[0]
    thread1 = Thread(target=task, args=("安run", ups1))  # 线程1：执行任务打印4个a
    thread1.start()  # 线程1开始
    thread1.join()  # 等待线程1结束

    # ups2=ups[1]
    # thread2 = Thread(target=task, args=("看的视频坚持评论", ups2))  # 线程2：执行任务打印2个b
    # thread2.start()  # 线程2开始 3_1415819751_azanguorun_b站执行日期.csv
    # thread2.join()  # 等待线程2结束

# 自定义的函数，可以替换成其他任何函数
def task(threadName, up):
    csrf = up['csrf']
    SESSDATA = up['SESSDATA']
    uuid = up['uuid']
    host_mid = up['host_mid']
    up = up['up']
    offset = ''

    #整理文件
    sort_csv(uuid,host_mid,up)

    #进行抽奖
    goto_lotto(threadName,uuid,host_mid,up,SESSDATA,csrf)

    #删除动态
    goto_my(threadName,offset,up,host_mid,SESSDATA)

    #获取艾特
    goto_at(threadName,offset, host_mid, SESSDATA,csrf)

#获取抽奖数据
def get_data():
    with open(f'../day02/b站/0_b站抽奖池.csv', 'w', newline='', encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['状态','链接','活动id','upid','抽奖时间戳','抽奖时间','一等奖','二等奖','三等奖'])

    #获取锦鲤池
    get_article_id()

    #获取机器人池
    get_upper_offset()

    # 文件整理
    sort_0_csv()

# 读取上次操作时间 输出日期
def readActionTime(uuid,host_mid,up):
    with open('./b站/'+uuid+'_'+host_mid+'_'+up+'_b站执行日期.csv', mode='r', encoding='utf-8') as f:
        last_line = f.readlines()[-1]
        last_time = last_line.split('结束时间戳:')[1]
        ltime = int(time.time() - 24 * 60 * 60 * 3)
        if int(last_time) <= ltime:
            return ltime
        else:
            return last_time

#判断是否关注
def get_if_sender(sender_uid,uuid,host_mid,up):
    with open(f'./b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    nre_row = 1
    for row in rows:
        if sender_uid in row[3] and '1' in row[0] and int(row[4]) >= endday - 3 * 24 * 60 * 60 :
            nre_row = 0
            print('已关注: ',sender_uid)
            return nre_row
        else:
            pass
    #1 没关注   0 关注
    return nre_row

#最终整理文件
def sort_csv(uuid,host_mid,up):
    # 读取原始抽奖池文件
    file_path = f'../day02/b站/0_b站抽奖池.csv'
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        nre_rows = list(reader)

    # 写入新的抽奖池文件
    new_file_path = f'./b站/{uuid}_{host_mid}_{up}_b站抽奖池.csv'
    with open(new_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(nre_rows)


    data = pd.read_csv(f'./b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv')
    sort_data = data.sort_values('抽奖时间戳', ascending=True)
    sort_data.to_csv(f'./b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', index=False)

    frame = pd.read_csv(f'./b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', engine='python', encoding='utf-8')

    data = frame.drop_duplicates(subset=['活动id'], keep='last', inplace=False)
    data.to_csv(f'./b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', index=0, encoding='utf-8')  # index=0, 去除索引
    print('文件去重复完成')


    #写入执行日期
    cs = 0

    last_time = readActionTime(uuid,host_mid,up)  # 获取1_1088543164_看的视频坚持评论_b站执行日期文件日期
    ts = int(time.time())
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(last_time)))
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endday))

    with open(f'./b站/'+uuid+'_'+host_mid+'_'+up+'_b站执行日期.csv', mode='a', encoding='utf-8', newline='') as f:
        f.write(
            f'执行时间:{start}--{end} 个数:{cs} 耗时:{round(((ts - endday) % 3600) / 60)}分{(ts - endday) % 60:.1f}秒 结束时间戳:{endday}')
        f.write('\n')

    print(f'执行时间:{start}--{end} 个数:{cs} 耗时:{round(((ts - endday) % 3600) / 60)}分{(ts - endday) % 60:.1f}秒 结束时间戳:{endday}')

#进行转发
def goto_dynamic(mblog_id,up,host_mid,csrf,SESSDATA):
    ltext = ['6', '1111', '保佑', '彳亍', '中个小的吧',
             '抽吧', '又来了', '来了来了', '芜湖来了来了', '永不缺席', '想要', '好家伙', '注入分母',
             '许愿许愿', '卷起来', '看我', '锦鲤附体', '么么哒', '这啥时候出的？',
             '可不可以中一次', '今日参与', '拉低', '老粉的话，会中的吧', '搏一搏！', '中啊', '对吧',
             '好人一生10086胎', '爱拼才会赢。从未停止 从未有过。', '来了', '中', '重在参与', '凑热闹', '希望是我',
             '虎虎虎', '来了来了',
             '转发，好运总会降临', '想当幸运儿呀', '根据墨菲定律，我越觉得中不了，就越可能中！', '日常迷信', '好运来！', '我是锦鲤', '每个月都来，从没中过',
             '还不轮到我吗', '哭了', '从不缺席', '多多参与，肯定会中奖的。', '凉快一下。', '能中就行',
             '三大原则：1从不放弃2从不放弃3从不放弃', '从不放弃', '好家伙，天天陪跑',
             '万一中了呢', ]
    content=str(random.choice(['1','123','666','6','ok']).encode('utf-8'))
    headers = {
        "content-type": "application/json",
        "referer": "https://t.bilibili.com/"+mblog_id,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    url = "https://api.bilibili.com/x/dynamic/feed/create/dyn"
    params = {
        "platform": "web",
        "csrf": csrf,
    }
    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    data = '{"dyn_req":{"content":{"contents":[{"raw_text":"'+content+'","type":1,"biz_id":""}]},"scene":4,"attach_card":null,"upload_id":"'+host_mid+'_'+str(int(time.time()))+'_3379","meta":{"app_meta":{"from":"create.dynamic.web","mobi_app":"web"}}},"web_repost_src":{"dyn_id_str":"' + mblog_id + '"}}'
    response = requests.post(url, headers=headers,cookies=cookies, params=params, data=data)

    print('执行转发',up,response.text)
    time.sleep(12)

    if '操作太频繁了，请稍后重试' in response.json()['message']:
        time.sleep(60)
        goto_dynamic(mblog_id,up,host_mid,csrf,SESSDATA)

def goto_relation(mblog_id,up,sender_uid,csrf,SESSDATA):
    time.sleep(10)
    headers = {
        "referer": "https://t.bilibili.com/"+mblog_id,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    url = "https://api.bilibili.com/x/relation/modify"
    data = {
        "act": "1",
        "fid": sender_uid,
        "csrf": csrf
    }
    response = requests.post(url, headers=headers,cookies=cookies, data=data)
    code=response.json()['code']
    if code==0:
        print('执行关注成功',up)
    elif code==22014:
        print('执行关注,无法重复关注',up)
    else:
        time.sleep(60)
        goto_relation(mblog_id,up,sender_uid,csrf,SESSDATA)

#进行取消关注
def goto_relationx(threadName,mblog_id,up,sender_uid,csrf,SESSDATA):
    headers = {
        "referer": "https://t.bilibili.com/"+mblog_id,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    url = "https://api.bilibili.com/x/relation/modify"
    data = {
        "act": "2",
        "fid": sender_uid,
        "spmid": "333.1368",
        "re_src": "0",
        "csrf": csrf
    }
    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    response = requests.post(url, headers=headers,cookies=cookies, data=data)

    print('执行取消关注',threadName,up,response.text)

#获取本人动态
def goto_my(threadName,offset,up,host_mid,SESSDATA):

    headers = {
        "origin": "https://space.bilibili.com",
        "referer": "https://space.bilibili.com/12058031/"+host_mid+"?spm_id_from=333.1368.reaction_usercard.all.click",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset="+offset+"&host_mid=" + str(host_mid)
    resp = requests.get(url, headers=headers,cookies=cookies)
    # print(resp.json())
    try:
        offset = resp.json()['data']['offset']  # 下一次动态请求的offset参数
        items = resp.json()['data']['items']

        for item in items:

            try:
                id_str = item['id_str']  # 动态id
                pub_ts = item['modules']['module_author']['pub_ts']  # 发布时间
                pub_time = item['modules']['module_author']['pub_time']  # 发布时间
                if pub_ts <= endday - 6 * 24 * 60 * 60 :
                   # print('进行删除',id_str, pub_ts,pub_time)
                   time.sleep(3)
                   goto_remove(id_str,up,host_mid,SESSDATA)
            except:
                print(threadName,item)

        last_ts = resp.json()['data']['items'][-1]['modules']['module_author']['pub_ts']
        last_time = resp.json()['data']['items'][-1]['modules']['module_author']['pub_time']

        print(last_ts, last_time)
        #最后的日期大于当前日期-3天，则进行爬取
        if last_ts >= endday - 10 * 24 * 60 * 60:
            print('最后的日期大于当前日期-3天',last_ts,endday,offset)
            goto_my(threadName,offset,up,host_mid,SESSDATA)
    except:
        print(resp.json(),'异常')

#进行删除
def goto_remove(id_str,up,host_mid,SESSDATA,csrf):
    print(id_str)
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "referer": "https://space.bilibili.com/"+host_mid+"/dynamic",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    url = "https://api.bilibili.com/x/dynamic/feed/operate/remove"
    params = {
        "platform": "web",
        "csrf": csrf
    }
    data = '{"dyn_id_str":"' + str(id_str) + '"}'
    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

    # response.json()['message']
    print('删除动态',up,response.text)

#进行点赞
def goto_thumb(mblog_id,SESSDATA,csrf):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    url = "https://api.vc.bilibili.com/dynamic_like/v1/dynamic_like/thumb"
    data = {
        "dynamic_id": str(mblog_id),
        # "up": "1",
        "csrf": csrf
    }
    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    print('执行点赞',mblog_id,response.text)

#进行抽奖
def goto_lotto(threadName,uuid,host_mid,up,SESSDATA,csrf):
    print('开始抽奖')
    with open(f'./b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    nre_rows = []
    cs = 0
    senders=[]
    for row in rows:
        if '状态' not in row :
            mblog_statls = row[0]
            lottery_time = int(row[4])
            sender_uid = row[3]
            if mblog_statls == '1' and lottery_time >= endday - 3 * 24 * 60 * 60:
                senders.append(sender_uid)


    for row in tqdm(rows):
        if '状态' not in row:
            # 0,mblog_url,mblog_id,sender_uid,lottery_time,today,first_prize_cmt, second_prize_cmt, third_prize_cmt
            mblog_statls = row[0]
            mblog_id = row[2]
            sender_uid = row[3]
            lottery_time = int(row[4])
            # 如果状态为0 抽奖日期大于当前日期，同时小于当前日期+3天，则执行
            if mblog_statls == '0' and lottery_time > endday and lottery_time < endday + 3 * 24 * 60 * 60:

                if 1 == get_if_sender(sender_uid,uuid,host_mid,up):
                    # 1 没关注   0 关注
                    # print('执行关注',sender_uid)
                    goto_relation(mblog_id,up,sender_uid,csrf,SESSDATA)

                # print('执行转发',mblog_id)
                goto_dynamic(mblog_id,up,host_mid,csrf,SESSDATA)

                # print('执行点赞',mblog_id)
                goto_thumb(mblog_id,SESSDATA,csrf)

                # 写入状态
                # mblog_statls = 1
                row[0] = '1'
                nre_rows.append(row)
                cs+= 1
            # 已抽完的删除  如果状态为1 抽奖日期小于当前日期-3 则执行
            elif mblog_statls == '1' and lottery_time < endday - 3 * 24 * 60 * 60:
                if sender_uid not in senders:
                    goto_relationx(threadName,mblog_id,up,sender_uid,csrf,SESSDATA)


            # 没抽过期的删除
            elif mblog_statls == '0' and lottery_time < endday:
                print('没抽过期的删除')
            else:
                nre_rows.append(row)
        else:
            nre_rows.append(row)


    with open(f'./b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(nre_rows)

    last_time = readActionTime(uuid,host_mid,up)  # 获取2_'+host_mid+'_看的视频坚持评论_b站执行日期文件日期
    ts = int(time.time())
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(endday)))
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ts)))

    print(f'执行时间:{start}--{end} 个数:{cs} 耗时:{round(((ts - endday) % 3600) / 60)}分{(ts - endday) % 60:.1f}秒 结束时间戳:{endday}')

#获取艾特
def goto_at(threadName,offset, host_mid, SESSDATA, csrf):
    url = "https://api.bilibili.com/x/msgfeed/at?build=0&mobi_app=web"
    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    response = requests.get(url, headers=headers, cookies=cookies)

    try:
        items = response.json()['data']['items']
        for item in items:
            nickname = item['user']['nickname']
            source_content = item['item']['source_content']
            print(nickname, source_content)

            data=[nickname,source_content]
            with open(f'../day02/b站/0_b站结果.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_write = csv.writer(f)
                csv_write.writerow(data)
    except:
        print('获取@失败',response.text)


def main():
    get_data()
    goto_lottery()

main()


