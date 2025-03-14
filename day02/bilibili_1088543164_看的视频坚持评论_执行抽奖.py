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
from threading import Thread
from time import sleep


endday=int(time.time())
# tt = datetime.datetime.now().strftime('%m-%d')



###################################################
# csrf='fd1905e6b3b26ba3a2d54af25c5d2337'
# SESSDATA='d106b464%2C1738315585%2C0a103%2A82CjC2Y2Zma0OS4exUoz1TjlIMSOwKLBDu6TSUwMCzQ1ivrvm4zO1cilj1NJPPvBs7HYMSVk5SR0VSUVZ4WU9MMDV1dnFzZEVxMnkzS3JJeFpvRjU0RmlXREtfM3Y1UE9pci1ENUdTWnNkTlcyNjVKbDQyZF95T2t5WnYxQTVJSW8yQjJ6Z0xzOGZnIIEC'
# cookies = {
#     'SESSDATA': SESSDATA,
#     'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
# }
# uuid='1'
# host_mid='1088543164'
# up='看的视频坚持评论'

##################################################
# csrf='d608baeb1072c2630f7e76bb8510464c'
# SESSDATA='6996eb28%2C1738116379%2C94a84%2A82CjAn1PjTiaYRpZGDRiLH5Gig68IyXTvTLjeRXe-pTn1gEvhdnwe4IcsXSvDSk4uRW4MSVkVPRnoyOEtsaHdvbktKUU1LVkQxOFFIdE5aRGMwR1lEeUVEUHNfVjkyUXRVYXFyMjktTWdEcEFqY196d0VJWk91Tlo5MVZtNDFFTzdsbDNheTlva0pBIIEC'
#
#
# uuid='2'
# host_mid='505037436'
# up='安run'




headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
}

# 读取上次操作时间 输出日期
def readActionTime(uuid,host_mid,up):
    with open('I:/b站/'+uuid+'_'+host_mid+'_'+up+'_b站执行日期.csv', mode='r', encoding='utf-8') as f:
        last_line = f.readlines()[-1]
        last_time = last_line.split('结束时间戳:')[1]
        ltime = int(time.time() - 24 * 60 * 60 * 3)
        if int(last_time) <= ltime:
            return ltime
        else:
            return last_time

#判断是否关注
def get_if_sender(sender_uid,uuid,host_mid,up):
    with open(f'I:/b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', mode='r', newline='', encoding='utf-8') as file:
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
            # print('没关注')
    #1 没关注   0 关注
    return nre_row

#最终整理文件
def sort_csv(uuid,host_mid,up):

    with open(f'I:/b站/0_b站抽奖池.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    nre_rows = []
    for row in rows:
        #397287828 灰烬战线 游戏
        if '397287828' not in row[3] or '状态' not in row[0]:
            nre_rows.append(row)

    with open(f'I:/b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(nre_rows)




    data = pd.read_csv(f'I:/b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv')
    sort_data = data.sort_values('抽奖时间戳', ascending=True)
    sort_data.to_csv(f'I:/b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', index=False)

    frame = pd.read_csv('I:/b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', engine='python', encoding='utf-8')
    #状态,链接,活动id,upid,抽奖时间戳,抽奖时间,一等奖,二等奖,三等奖

    data = frame.drop_duplicates(subset=['活动id'], keep='last', inplace=False)
    data.to_csv('I:/b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', index=0, encoding='utf-8')  # index=0, 去除索引
    print('文件去重复完成')


    #写入执行日期
    cs = 0

    last_time = readActionTime(uuid,host_mid,up)  # 获取1_1088543164_看的视频坚持评论_b站执行日期文件日期
    ts = int(time.time())
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(last_time)))
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endday))

    with open('I:/b站/'+uuid+'_'+host_mid+'_'+up+'_b站执行日期.csv', mode='a', encoding='utf-8', newline='') as f:
        f.write(
            f'执行时间:{start}--{end} 个数:{cs} 耗时:{round(((ts - endday) % 3600) / 60)}分{(ts - endday) % 60:.1f}秒 结束时间戳:{endday}')
        f.write('\n')

    print(f'执行时间:{start}--{end} 个数:{cs} 耗时:{round(((ts - endday) % 3600) / 60)}分{(ts - endday) % 60:.1f}秒 结束时间戳:{endday}')

#进行转发
def goto_dynamic(mblog_id,host_mid,csrf,SESSDATA):
    ltext = ['6', '报道', '保佑', '彳亍', '中个小的吧',
             '抽吧', '又来了', '来了来了', '芜湖来了来了', '永不缺席', '想要', '好家伙', '注入分母',
             '许愿许愿', '卷起来', '看我', '锦鲤附体', '么么哒', '这啥时候出的？',
             '可不可以中一次', '今日参与', '拉低', '老粉的话，会中的吧', '搏一搏！', '中啊', '对吧',
             '好人一生10086胎', '爱拼才会赢。从未停止 从未有过。', '来了', '中', '重在参与', '凑热闹', '希望是我',
             '虎虎虎', '来了来了',
             '转发，好运总会降临', '想当幸运儿呀', '根据墨菲定律，我越觉得中不了，就越可能中！', '日常迷信', '好运来！', '我是锦鲤', '每个月都来，从没中过',
             '还不轮到我吗', '哭了', '从不缺席', '多多参与，肯定会中奖的。', '凉快一下。', '能中就行',
             '三大原则：1从不放弃2从不放弃3从不放弃', '从不放弃', '好家伙，天天陪跑',
             '万一中了呢', ]
    # content=str(random.choice(ltext).encode('utf-8'))
    content = '123'
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

    print('执行转发',mblog_id,response.text)
    time.sleep(12)

    if '操作太频繁了，请稍后重试' in response.json()['message']:
        time.sleep(60)
        goto_dynamic(mblog_id,host_mid,csrf,SESSDATA)

def goto_relation(mblog_id,sender_uid,csrf,SESSDATA):
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

    print('执行关注',sender_uid,response.text)

#进行取消关注
def goto_relationx(threadName,mblog_id,sender_uid,csrf,SESSDATA):
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

    print('执行取消关注',threadName,sender_uid,response.text)

#获取本人动态
def goto_my(threadName,offset,host_mid,SESSDATA,csrf):

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
                   goto_remove(id_str,host_mid,SESSDATA,csrf)
            except:
                print(threadName,item)

        last_ts = resp.json()['data']['items'][-1]['modules']['module_author']['pub_ts']
        last_time = resp.json()['data']['items'][-1]['modules']['module_author']['pub_time']

        print(last_ts, last_time)
        #最后的日期大于当前日期-3天，则进行爬取
        if last_ts >= endday - 10 * 24 * 60 * 60:
            print('最后的日期大于当前日期-3天',last_ts,endday,offset)
            goto_my(threadName,offset,host_mid,SESSDATA,csrf)
    except:
        print(resp.json(),'异常')

#进行删除
def goto_remove(id_str,host_mid,SESSDATA,csrf):
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

    response.json()['message']
    # print(response.text)

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
    with open(f'I:/b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', mode='r', newline='', encoding='utf-8') as file:
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
                    goto_relation(mblog_id,sender_uid,csrf,SESSDATA)

                # print('执行转发',mblog_id)
                goto_dynamic(mblog_id,host_mid,csrf,SESSDATA)

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
                    goto_relationx(threadName,mblog_id,sender_uid,csrf,SESSDATA)

                # print('执行删除')
                # goto_remove(mblog_id)


            # 没抽过期的删除
            elif mblog_statls == '0' and lottery_time < endday:
                print('没抽过期的删除')
            else:
                nre_rows.append(row)
        else:
            nre_rows.append(row)


    with open(f'I:/b站/'+uuid+'_'+host_mid+'_'+up+'_b站抽奖池.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(nre_rows)

    last_time = readActionTime(uuid,host_mid,up)  # 获取2_'+host_mid+'_看的视频坚持评论_b站执行日期文件日期
    ts = int(time.time())
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(endday)))
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ts)))

    print(f'执行时间:{start}--{end} 个数:{cs} 耗时:{round(((ts - endday) % 3600) / 60)}分{(ts - endday) % 60:.1f}秒 结束时间戳:{endday}')

#获取艾特
def goto_at(SESSDATA):
    url = "https://api.bilibili.com/x/msgfeed/at?build=0&mobi_app=web"
    cookies = {
        'SESSDATA': SESSDATA,
        'buvid3': 'EBBBBECC-3D73-D64B-5866-6470BFD7F6B023832infoc'
    }
    response = requests.get(url, headers=headers, cookies=cookies)

    print(response.text)
    print(response)
    try:
        items = response.json()['data']['items']
        for item in items:
            nickname = item['user']['nickname']
            source_content = item['item']['source_content']
            print(nickname, source_content)

            data=[nickname,source_content]
            with open(f'I:/b站/0_b站结果.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_write = csv.writer(f)
                csv_write.writerow(data)
    except:
        print(response.text)
# 自定义的函数，可以替换成其他任何函数
def task(threadName, up):
        csrf = up['csrf']
        SESSDATA = up['SESSDATA']
        uuid = up['uuid']
        host_mid = up['host_mid']
        up = up['up']
        offset = ''

        print(threadName,uuid,host_mid,up,SESSDATA,csrf)

        #整理文件
        sort_csv(uuid,host_mid,up)

        #进行抽奖
        goto_lotto(threadName,uuid,host_mid,up,SESSDATA,csrf)

        #删除动态
        goto_my(threadName,offset, host_mid, SESSDATA, csrf)

        #获取艾特
        goto_at(SESSDATA)
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
    ups2=ups[1]
    thread1 = Thread(target=task, args=("安run", ups1))  # 线程1：执行任务打印4个a
    thread2 = Thread(target=task, args=("看的视频坚持评论", ups2))  # 线程2：执行任务打印2个b
    # ups3=ups[2]
    # thread3 = Thread(target=task, args=("thread_3", ups3))  # 线程2：执行任务打印2个b

    thread1.start()  # 线程1开始
    thread2.start()  # 线程2开始 3_1415819751_azanguorun_b站执行日期.csv
    # thread3.start()
    thread1.join()  # 等待线程1结束
    thread2.join()  # 等待线程2结束
    # thread3.join()  # 等待线程2结束



# goto_lottery()


