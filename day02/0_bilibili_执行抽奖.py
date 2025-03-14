# coding:utf-8
"""
Project    : python_spiders
Time       ：2024/7/5 16:35
File       : 3_QCommandLinkButton指向按钮.py
content:
result:
"""
import math,re
import datetime
import random

import pandas as pd
import csv
import json
import time
from tqdm import tqdm
import requests




endday=int(time.time())
# tt = datetime.datetime.now().strftime('%m-%d')

SESSDATA='d106b464%2C1738315585%2C0a103%2A82CjC2Y2Zma0OS4exUoz1TjlIMSOwKLBDu6TSUwMCzQ1ivrvm4zO1cilj1NJPPvBs7HYMSVk5SR0VSUVZ4WU9MMDV1dnFzZEVxMnkzS3JJeFpvRjU0RmlXREtfM3Y1UE9pci1ENUdTWnNkTlcyNjVKbDQyZF95T2t5WnYxQTVJSW8yQjJ6Z0xzOGZnIIEC'
cookies = {
    'SESSDATA': SESSDATA,
    'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
}

host_mid='505037436'
up='安run'
#安run


# 读取上次操作时间 输出日期
def readActionTime():
    with open('I:/b站/0_b站执行日期.csv', mode='r', encoding='utf-8') as f:
        last_line = f.readlines()[-1]
        last_time = last_line.split('结束时间戳:')[1]
        ltime = int(time.time() - 24 * 60 * 60 * 3)
        if int(last_time) <= ltime:
            return ltime
        else:
            return last_time

#获取锦鲤数据
def get_article_id():
    '''
       226257459 _大锦鲤_
       3493086911007529    不锈钢炒锅
       5536630     西伯利亞倉鼠
    '''
    mids = ['226257459','3493086911007529','5536630']
    last_time=readActionTime()              #获取上次执行结束时间
    mblog_urls = []
    for mid in mids:
        time.sleep(2)
        # up主页
        article_url = f'https://api.bilibili.com/x/space/article?mid={mid}&pn=1&ps=12'
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        }
        resp = requests.get(article_url, headers=headers)
        print(resp.json())
        article_datas = resp.json()['data']['articles']
        for article_data in tqdm(article_datas):
            #获取专栏id
            article_id=article_data['id']
            publish_time = article_data['publish_time']
            # 如果
            if int(last_time) < publish_time:
                cv_url = f'https://www.bilibili.com/read/cv{article_id}/?spm_id_from=333.999.0.0'
                html_data = requests.get(cv_url, headers=headers).text
                data=re.findall('https://t.bilibili.com/([0-9]{18})', str(html_data))
                opus_data=re.findall('https://www.bilibili.com/opus/([0-9]{18})', str(html_data))

                if opus_data != None :
                    opus_url=['https://www.bilibili.com/opus/' + item for item in opus_data]
                else:
                    opus_url=[]
                if data != None:
                    data_url=['https://t.bilibili.com/' + item for item in data]
                else:
                    data_url=[]
                mblog_urls=mblog_urls+opus_url+data_url
    #获取活动id
    mblog_urls=list(set(mblog_urls))
    print(mblog_urls)
    print(len(mblog_urls))

    # mkdirfiletwo(mblog_urls,publish_time)

    for mblog_url in tqdm(mblog_urls):
        time.sleep(0.5)
        if 1==get_if_csv(mblog_url):
            get_lottery_id(mblog_url)

def get_if_csv(mblog_url):
    mblog_id=str(mblog_url).split('/')[-1]
    with open(f'I:/b站/0_b站抽奖池.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    nre_row = 1
    for row in rows:
        # 397287828 灰烬战线 游戏
        # print(row)
        if mblog_id  in row:
           # print(mblog_id)
           nre_row=0
        else:
           pass
    return nre_row

#验证锦鲤数据
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
    url = "https://api.vc.bilibili.com/lottery_svr/v1/lottery_svr/lottery_notice"
    params = {
        "business_id": str(mblog_id),
        "business_type": "1",
        # "csrf": "3d04d2d0d32fd333ec0cfdd5d17bee33",
        "web_location": "333.1330"
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        lottery_time = response.json()['data']['lottery_time']
        today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(lottery_time))  # 今日日期

        first_prize_cmt = response.json()['data']['first_prize_cmt']
        '''
        闪卡
        '''
        sender_uid = response.json()['data']['sender_uid']
        try:
            second_prize_cmt = response.json()['data']['second_prize_cmt']
        except:
            second_prize_cmt = "无"
        try:
            third_prize_cmt = response.json()['data']['third_prize_cmt']
        except:
            third_prize_cmt = "无"
        if lottery_time >=int(time.time()):
            #执行日期
            data=[0,mblog_url,mblog_id,sender_uid,lottery_time,today,first_prize_cmt, second_prize_cmt, third_prize_cmt]
            with open(f'I:/b站/0_b站抽奖池.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_write = csv.writer(f)
                csv_write.writerow(data)
            with open(f'I:/b站/0_b站历史抽奖池.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_write = csv.writer(f)
                csv_write.writerow(data)
            # print(mblog_url,mblog_id,lottery_time,today,first_prize_cmt, second_prize_cmt, third_prize_cmt)
    except:
        # print('非官方,预约,转发')
        pass

#获取机器人数据
def get_upper_offset():
    host_mids = ['1218591431', '74105384', '12058031', '3546685089254178', '396902231', '3461577258830253','1233410593','3493277005253367'
                 ,'181046678','158120381','174356526','281690207','44472232']
    # host_mids = ['3546685089254178', '3461577258830253']
    # host_mids=['3546685089254178']
    for host_mid in host_mids:
        # print(host_mid)
        offset=''
        get_upper_id(host_mid,offset)

#获取机器人数据
def get_upper_id(host_mid,offset):
    last_time = readActionTime()
    cs=0
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset="+str(offset)+"&host_mid="+str(host_mid)
    resp = requests.get(url, headers=headers,cookies=cookies)
    #
    try:
        offset = resp.json()['data']['offset']  # 下一次动态请求的offset参数

        items = resp.json()['data']['items']

        for item in tqdm(items):
            if 'orig' in item:
                # print(item)
            # try:
                id_str = item['orig']['id_str']  # 动态id
                orig_ts = item['orig']['modules']['module_author']['pub_ts']  # 发布时间

                type = item['type']  # 动态类型


                pub_ts = item['modules']['module_author']['pub_ts']  # 发布时间
                pub_time = item['modules']['module_author']['pub_time']  # 发布时间
                # print(id_str)
                #执行时间<抽奖日期<当前时间
                # if int(last_time) <= orig_ts and orig_ts < endday:


                '''
                DYNAMIC_TYPE_DRAW           文本
                DYNAMIC_TYPE_FORWARD        转发
                DYNAMIC_TYPE_AV             发布视频
                '''
                if type == 'DYNAMIC_TYPE_DRAW' or type == 'DYNAMIC_TYPE_FORWARD':

                    mblog_id = item['orig']['id_str']
                    try:
                        text = item['orig']['modules']['module_dynamic']['desc']['text'].replace('\r', '').replace('\n', '')  # 发布内容
                    except:
                        text = ''
                    rsl = re.findall(r"(\d{1,2}月\d{1,2}日)",text)
                    if len(rsl)>0:
                        today = '2024-'+rsl[-1]+' 00:00:00'

                        today=today.replace('月','-').replace('日','')
                        try:
                            dt = time.strptime(today, '%Y-%m-%d %H:%M:%S')
                            lottery_time = int(time.mktime(dt))

                            if lottery_time >=int(time.time()):
                                sender_uid = item['orig']['modules']['module_author']['mid']
                                mblog_url = 'http://www.bilibili.com/opus/' + id_str

                            #     print(mblog_url,mblog_id,sender_uid,lottery_time,today)
                                if 1 == get_if_csv(mblog_url):
                                    data = [0,mblog_url,mblog_id,sender_uid,lottery_time,today,'无', '无', '无']
                                    print(data)
                                    cs += 1
                                    with open(f'I:/b站/0_b站抽奖池.csv', mode='a', encoding='utf-8', newline='') as f:
                                        csv_write = csv.writer(f)
                                        csv_write.writerow(data)
                                    with open(f'I:/b站/0_b站历史抽奖池.csv', mode='a', encoding='utf-8', newline='') as f:
                                        csv_write = csv.writer(f)
                                        csv_write.writerow(data)
                        except:
                            print(today)
                    else:
                        # pass
                        try:
                            mblog_url='https://t.bilibili.com/'+id_str
                            if 1 == get_if_csv(mblog_url):
                                get_lottery_id(mblog_url)
                        except:
                            print('id_str错误')
                        # print(id_str)

            # print('找到'+str(cs)+'条数据')
            # else:
            #     print(item)
            # except:
            #     pass
            #     print(item)

        pub_ts = resp.json()['data']['items'][-1]['modules']['module_author']['pub_ts']
        #机器人最后的时间大于  执行时间
        if int(last_time) <= pub_ts:
            time.sleep(3)
            print('进行下一页',host_mid,pub_ts,offset)
            get_upper_id(host_mid, offset)
    except:
        print(resp.json())
#最终整理文件
def sort_csv():        #f'I:/'
    data = pd.read_csv(f'I:/b站/0_b站抽奖池.csv')
    sort_data = data.sort_values('抽奖时间戳', ascending=True)
    sort_data.to_csv(f'I:/b站/0_b站抽奖池.csv', index=False)

    frame = pd.read_csv('I:/b站/0_b站抽奖池.csv', engine='python', encoding='utf-8')
    #状态,链接,活动id,upid,抽奖时间戳,抽奖时间,一等奖,二等奖,三等奖

    data = frame.drop_duplicates(subset=['活动id', '抽奖时间戳'], keep='last', inplace=False)
    data.to_csv('I:/b站/0_b站抽奖池.csv', index=0, encoding='utf-8')  # index=0, 去除索引
    print('文件去重复完成')


    with open(f'I:/b站/0_b站抽奖池.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    nre_rows = []
    for row in rows:
        #397287828 灰烬战线 游戏
        if '397287828' not in row[3]:
            nre_rows.append(row)

    with open(f'I:/b站/0_b站抽奖池.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(nre_rows)




    #写入执行日期
    cs = 0

    last_time = readActionTime()  # 获取1_1088543164_看的视频坚持评论_b站执行日期文件日期
    ts = int(time.time())
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(last_time)))
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endday))

    with open('I:/b站/0_b站执行日期.csv', mode='a', encoding='utf-8', newline='') as f:
        f.write(
            f'执行时间:{start}--{end} 个数:{cs} 耗时:{round(((ts - endday) % 3600) / 60)}分{(ts - endday) % 60:.1f}秒 结束时间戳:{endday}')
        f.write('\n')

    print(f'执行时间:{start}--{end} 个数:{cs} 耗时:{round(((ts - endday) % 3600) / 60)}分{(ts - endday) % 60:.1f}秒 结束时间戳:{endday}')

#获取抽奖数据
def get_data():
    with open(f'I:/b站/0_b站抽奖池.csv', 'w', newline='', encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['状态','链接','活动id','upid','抽奖时间戳','抽奖时间','一等奖','二等奖','三等奖'])

    #获取锦鲤池
    get_article_id()

    #获取机器人池
    get_upper_offset()

    #文件整理
    sort_csv()

def main():
    #获取数据
    # host_mid = '505037436'
    # up='安run'
    #
    # host_mid = '1088543164'
    # up='看的视频坚持评论'

    get_data()
    print('完成')
    import bilibili_1088543164_看的视频坚持评论_执行抽奖

    bilibili_1088543164_看的视频坚持评论_执行抽奖.goto_lottery()


main()


