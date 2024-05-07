import json

import requests
import time
import jsonTest
import os
import socket
import uuid

platform = 'PC'
backup_stream = '0'
#area_v2 = '88'
origin = 'https://link.bilibili.com'
referer = 'https://link.bilibili.com/p/center/index?spm_id_from=333.1007.0.0'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
title = 'CF00后妹妹，在线上分'

cookiecat = ''



def sendMessage(rMsg):
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookietcat, cookie = jsonTest.json_read()
    url = 'https://api.live.bilibili.com/msg/send'
    data = {
        'bubble': '0',
        'msg': rMsg,
        'color': '16777215',
        'room_type': '0',
        'jumpfrom': '86001',
        'mode': '1',
        'fontsize': '25',
        'rnd': '1691342751',
        'roomid': getRoomID(),
        'csrf': bili_jct,
        'csrf_token': bili_jct,
    }

    headers = {
        'cookie': cookie,
        'origin': 'https://live.bilibili.com',
        'referer': 'https://live.bilibili.com/30274276?broadcast_type=0&is_room_feed=1&spm_id_from=333.999.live_users_card.0.click&live_from=86001',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        'Connection': 'close',
    }
    response = requests.post(url=url, data=data, headers=headers)
    # print(response.status_code)


def getrtmpurl():
    getrtmpurlpvid = 'PVID=2'
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
    csrf = bili_jct
    csrf_token = csrf
    url = 'https://api.live.bilibili.com/xlive/app-blink/v1/live/FetchWebUpStreamAddr'
    data = {
        'platform': platform,
        'backup_stream': backup_stream,
        'csrf': csrf,
        'csrf_token': csrf_token,
    }

    headers = {
        'Cookie': cookie + getrtmpurlpvid,
        'origin': origin,
        'referer': referer,
        'user-agent': user_agent,
    }
    response = requests.post(url=url, data=data, headers=headers)
    url = response.json()['data']['addr']['code']


def setStartArea(area_v2):
    areapvid = 'PVID=4'
    room_id = getRoomID()

    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
    csrf = bili_jct
    csrf_token = csrf
    print("================================  选择直播区域  =====================================")
    getAreaurl = 'https://api.live.bilibili.com/xlive/app-blink/v1/index/getNewRoomSwitch?platform=pc&area_parent_id=2&area_id=88'
    getAreadata = {
        'room_id': room_id,
        'platform': platform,
        'area_v2': str(area_v2),
        'backup_stream': backup_stream,
        'csrf': csrf,
        'csrf_token': csrf_token,
    }
    getAreaheaders = {
        'Cookie': cookie + areapvid,
        'origin': origin,
        'referer': referer,
        'user-agent': user_agent,
    }
    res = requests.get(url=getAreaurl, data=getAreadata, headers=getAreaheaders)

def getStart(area_v2):
    startpvid = 'PVID=3'
    room_id = getRoomID()

    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
    csrf = bili_jct
    csrf_token = csrf
    print("================================  开始直播  =====================================")

    url = 'https://api.live.bilibili.com/room/v1/Room/startLive'
    data = {
        'room_id': room_id,
        'platform': platform,
        'area_v2': str(area_v2),
        'backup_stream': backup_stream,
        'csrf': csrf,
        'csrf_token': csrf_token,
    }
    headers = {
        'Cookie': cookie + startpvid,
        'origin': origin,
        'referer': referer,
        'user-agent': user_agent,
    }
    res = requests.post(url=url, data=data, headers=headers)

def getreflashrtmp():
    refreshpvid = 'PVID=8'
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
    csrf = bili_jct
    csrf_token = csrf
    print("================================  刷新地址  =====================================")
    url = 'https://api.live.bilibili.com/xlive/app-blink/v1/live/FetchWebUpStreamAddr'
    data = {
        'platform': platform,
        'backup_stream': backup_stream,
        'reset_key': 'true',
        'csrf': csrf,
        'csrf_token': csrf_token,
    }
    headers = {
        'Cookie': cookie + refreshpvid,
        'origin': origin,
        'referer': referer,
        'user-agent': user_agent,
    }
    responsereflashrtmp = requests.post(url=url, data=data, headers=headers)
    reflashurl = responsereflashrtmp.json()['data']['addr']['code']
    return reflashurl


def stoprtmp():
    room_id = getRoomID()
    stoppvid = 'PVID=14'
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
    csrf = bili_jct
    csrf_token = csrf
    print("================================  停止直播  =====================================")
    url = 'https://api.live.bilibili.com/room/v1/Room/stopLive'
    data = {
        'platform': platform,
        'room_id': room_id,
        'csrf': csrf,
        'csrf_token': csrf_token,
    }
    headers = {
        'Cookie': cookie + stoppvid,
        'origin': origin,
        'referer': referer,
        'user-agent': user_agent,
    }
    responsereflashrtmp = requests.post(url=url, data=data, headers=headers)
    LiveStatus = responsereflashrtmp.json()['data']['status']
    return LiveStatus


def resettitle(text):
    room_id = getRoomID()
    roompvid = 'PVID=6'
    title = text
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
    csrf = bili_jct
    csrf_token = csrf

    print("================================  修改标题  =====================================")
    getroomtiyleurl = 'https://api.live.bilibili.com/room/v1/Room/update'
    getroomdata = {
        'platform': platform,
        'room_id': room_id,
        'title': title,
        'csrf_token': csrf_token,
        'csrf': csrf,
    }
    getroomheaders = {
        'Cookie': cookie + roompvid,
        'origin': origin,
        'referer': referer,
        'user-agent': user_agent,
    }
    responsegetroom = requests.post(url=getroomtiyleurl, data=getroomdata, headers=getroomheaders)

    if responsegetroom.json()['msg'] == '房间不存在':
        print("请开通并认证直播间，再尝试！！！！！！！！！！！！！！！")
        res = '房间不存在'
    elif str(responsegetroom.json()['msg'] == '0'):
        res = "房间存在"
    else:
        res = "未知问题"
    return res


def getBilibiliLiveStatusFromURL():
    statuspvid = 'PVID=2'
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
    csrf = bili_jct
    statusurl = 'https://api.live.bilibili.com/xlive/app-blink/v1/room/GetInfo?platform=pc'
    statusheader = {
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie': cookie + statuspvid,
        'Origin': 'https://link.bilibili.com',
        'Referer': 'https://link.bilibili.com/p/center/index?spm_id_from=333.337.0.0',
        'Sec-Ch-Ua': "'Chromium';v='122', 'Not(A:Brand';v='24','Microsoft Edge';v='122'",
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "'Windows'",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',

    }
    statusdata = {
        'platform': "pc",
    }
    responsegetroom = requests.get(url=statusurl, data=statusdata, headers=statusheader)
    title = responsegetroom.json()['data']['title']
    uname = responsegetroom.json()['data']['uname']
    if responsegetroom.json()['data']['live_status'] == 1:
        live_status = 'OnLive'
    else:
        live_status = 'OffLive'
    return live_status, title,uname


def getBilibiliLoginStatus():
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat1, cookie = jsonTest.json_read()
    cookie = cookiecat1 + 'DedeUserID=' + DedeUserID + ";" + 'DedeUserID__ckMd5=' + DedeUserID__ckMd5 + ";" + 'SESSDATA=' + SESSDATA + ";" + 'bili_jct=' + bili_jct + ";" + 'sid=' + sid + ";"
    room_id = getRoomID()
    roompvid = 'PVID=6'
    title = "十年磨一剑"
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat1, cookie = jsonTest.json_read()
    csrf = bili_jct
    csrf_token = csrf
    getroomtiyleurl = 'https://api.live.bilibili.com/room/v1/Room/update'
    getroomdata = {
        'platform': platform,
        'room_id': room_id,
        'title': title,
        'csrf_token': csrf_token,
        'csrf': csrf,
    }
    getroomheaders = {
        'Cookie': cookie + roompvid,
        'origin': origin,
        'referer': referer,
        'user-agent': user_agent,
    }
    responsegetroom = requests.post(url=getroomtiyleurl, data=getroomdata, headers=getroomheaders)
    text = ['账号未登录', '房间不存在']
    if responsegetroom.json()['msg'] == "user no login":
        text[0] = "账号未登录"
    else:
        text[0] = "账号已登录"
    if responsegetroom.json()['msg'] == "房间不存在":
        text[1] = "房间不存在"
    else:
        text[1] = "房间存在"

    return text

def getRoomID():
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
    url = "https://api.live.bilibili.com/xlive/web-ucenter/user/live_info"
    header = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': cookie,
        'origin': 'https://link.bilibili.com',
        'referer': 'https://link.bilibili.com/p/center/index?spm_id_from=333.1007.0.0',
        'sec-ch-ua': "'Not A;Brand';v='99', 'Chromium';v='99'",
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "'Windows'",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    }

    responsegetroom = requests.get(url=url, headers=header)
    if responsegetroom.json()['message'] == "账号未登录":
        return "11111111"
    elif responsegetroom.json()['message'] == "网络请求错误" or responsegetroom.json()['message'] == "请求错误":
        return "22222222"
    else:
        return responsegetroom.json()['data']['room_id']

def getPCInfo():
    hostName, loginName = socket.gethostname(), os.getlogin()
    ip = socket.gethostbyname(socket.gethostname())
    node = uuid.getnode()
    macHex = uuid.UUID(int=node).hex[-12:]
    mac = []
    for i in range(len(macHex))[::2]:
        mac.append(macHex[i:i + 2])
    mac = ':'.join(mac)

    return ip, mac, hostName, loginName

def getBilibiliUserInfoLogin():
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
    url = "https://api.bilibili.com/x/web-interface/nav"
    header = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie': cookie,
        'Origin': 'https://space.bilibili.com',
        'Referer': 'https://space.bilibili.com/492921501?spm_id_from=333.1007.0.0',
        'Sec-Ch-Ua': "'Microsoft Edge';v='123', 'Not:A-Brand';v='8', 'Chromium';v='123'",
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "'Windows'",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'user_agent',
    }

    responsegetroom = requests.get(url=url, headers=header)
    try:
        uname = responsegetroom.json()['data']['uname']
        Login = responsegetroom.json()['data']['isLogin']
    except:
        Login = False
        uname = 'Samulor_Xie'
    return Login,uname

def getLiveAreaList():
    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
    url = "https://api.live.bilibili.com/room/v1/Area/getList?show_pinyin=1"
    header = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie': '',
        'Origin': 'https://space.bilibili.com',
        'Referer': 'https://space.bilibili.com/492921501?spm_id_from=333.1007.0.0',
        'Sec-Ch-Ua': "'Microsoft Edge';v='123', 'Not:A-Brand';v='8', 'Chromium';v='123'",
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "'Windows'",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'user_agent',
    }

    responsegetroom = requests.get(url=url, headers=header)
    listLP = responsegetroom.json()['data']

    json_dict_2 = json.dumps(listLP, indent=2, sort_keys=True, ensure_ascii=False)
    dict_from_str_2 = json.loads(json_dict_2)
    dict = {}
    for i in range(len(dict_from_str_2)):
        dict[i] = dict_from_str_2[i]

    Pdict = {}
    Clist = []

    for i in dict:
        for j in dict[i]:
            Pid = dict[i]['id']
            Pname = dict[i]['name']
            Pdict[Pname] = [Pid]
            for z in dict[i]['list']:
                Cid = z['id']
                Cname = z['name']
                Clist.append([Pid, Cname, Cid])

    return Pdict, Clist

def getCidFromCPname(Pname, Cname="穿越火线", Pdict=1, Clist=2):
    Pdict, Clist = getLiveAreaList()
    Cdata = []
    Cid = 88
    for list in Clist:
        if list[0] == Pdict.get(Pname)[0]:
            Cdata.append(list[1])
            if Cname == list[1]:
                Cid = list[2]
    return Cdata, Cid

