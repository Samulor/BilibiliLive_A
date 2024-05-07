import asyncio
import datetime
import http.cookies
import os
import random
import time
from typing import *

import aiohttp
import requests

import BilibiRequest
import blivedm as blivedm
import blivedm.models.web as web_models
import json

import SparkApiGetReturn
from jsonTest import jsonPath


# 直播间ID的取值看直播间URL


# 这里填一个已登录账号的cookie的SESSDATA字段的值。不填也可以连接，但是收到弹幕的用户名会打码，UID会变成0




def sendMessage(rMsg,bili_jct,cookie):
    url = 'https://api.live.bilibili.com/msg/send'
    data = {
        'bubble': '0',
        'msg': rMsg,
        'color': '16777215',
        'room_type' : '0',
        'jumpfrom' : '86001',
        'mode': '1',
        'fontsize': '25',
        'rnd': '1691342751',
        'roomid': room_id,
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
    #print(response.status_code)
    if response.status_code != 200:
        time.sleep(3)
        response = requests.post(url=url, data=data, headers=headers)

def json_read():
    if os.path.exists(jsonPath):
        with open(jsonPath, 'r') as load_f:
            load_dict = json.load(load_f)
        DedeUserID = load_dict['DedeUserID']
        DedeUserID__ckMd5 = load_dict['DedeUserID__ckMd5']
        SESSDATA = load_dict['SESSDATA']
        bili_jct = load_dict['bili_jct']
        sid = load_dict['sid']
        cookiecat = load_dict['cookiecat']
        cookie = load_dict['cookie']
        return DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie
    else:
        test_dict = {
            'DedeUserID': '123213444',
            'DedeUserID__ckMd5': 'vsdghg23f4534',
            'SESSDATA': 'b5876799%2C1728991105%2C35cfefwfdcfvawefqwfwfdwDPPqpCrMGY2TyxG88owcKFyaRcoZUuHgjXhYrZC47W0BhxplJPFXdwwSVlpGa0g5ZWlSTU5zbDZYM3BmLTBoUjBXeHk2TlExV3hlR0dFQWMxcTRKWnhTWHBXNm9pWTNRbjIxZzJDaDJ5aXY0RWltUmhKbnprV2lXYnhhZ3dzSnVRIIEC',
            'bili_jct': '482a51vrevcvswefgwegwgfvc68d5cd41',
            'sid': 'sdgsergw3523',
            'cookiecat': '',
            'cookie': 'bili_jct=482a51vrevcvswefgwegwgfvc68d5cd41; SESSDATA=b5876792C35cfefwfdcfvawefqwfwfdwDPPqpCrMGY2TyxG88owcKFyaRcoZUuHgjXhYrZC47W0BhxplJPFXoUjBXeHk2TlExV3hlR0dFQWMxcTRKWnhTWHBXNm9pWTNRbjIxZzJDaDJ5aXY0RWltUmhKbnprV2lXYnhhZ3dzSnVRIIECgjXhYrZC47W0BhxplJPFXdwwSVlpGa0g5ZWlSTU5zbDZYM3BmLTBoUjBXeHk2TlExV3hlR0dFQWMxcTRKWnhTWHBXNm9pWTNRbjIxZzJDaDJ5aXY0RWltUmhKbnprV2lXYnhhZ3dzSnVRIIEC; sid=mi0sdasfqc2; DedeUserID=353246252345;  DedeUserID__ckMd5=fbfdgergt3434f43;'
        }

        json_str = json.dumps(test_dict)
        new_dict = json.loads(json_str)
        with open(jsonPath, "w") as f:
            json.dump(new_dict, f)
        time.sleep(1)
        DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = json_read()
        return DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie


async def main():
    init_session()
    try:
        await run_single_client()
        await run_multi_clients()
    finally:
        await session.close()



def init_session():
    cookies = http.cookies.SimpleCookie()

    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookietcat, cookie11 = json_read()
    cookies['SESSDATA'] = SESSDATA

    cookies['SESSDATA']['domain'] = 'bilibili.com'

    global session
    session = aiohttp.ClientSession()
    session.cookie_jar.update_cookies(cookies)


async def run_single_client():
    """
    演示监听一个直播间
    """
    room_id = random.choice(TEST_ROOM_IDS)
    client = blivedm.BLiveClient(room_id, session=session)#线程
    handler = MyHandler() #线程
    client.set_handler(handler)

    client.start()
    try:
        # 演示5秒后停止
        await asyncio.sleep(5)
        client.stop()

        await client.join()
    finally:
        await client.stop_and_close()


async def run_multi_clients():
    """
    演示同时监听多个直播间
    """

    clients = [blivedm.BLiveClient(room_id, session=session) for room_id in TEST_ROOM_IDS]
    handler = MyHandler()
    for client in clients:
        client.set_handler(handler)
        client.start()

    try:
        await asyncio.gather(*(
            client.join() for client in clients
        ))
    finally:
        await asyncio.gather(*(
            client.stop_and_close() for client in clients
        ))


class MyHandler(blivedm.BaseHandler):
    # # 演示如何添加自定义回调
    # _CMD_CALLBACK_DICT = blivedm.BaseHandler._CMD_CALLBACK_DICT.copy()
    #
    # # 入场消息回调
    # def __interact_word_callback(self, client: blivedm.BLiveClient, command: dict):
    #     print(f"[{client.room_id}] INTERACT_WORD: self_type={type(self).__name__}, room_id={client.room_id},"
    #           f" uname={command['data']['uname']}")
    # _CMD_CALLBACK_DICT['INTERACT_WORD'] = __interact_word_callback  # noqa

    def _on_heartbeat(self, client: blivedm.BLiveClient, message: web_models.HeartbeatMessage):
        #print(f'[{client.room_id}] 心跳')
        pass

    def _on_danmaku(self, client: blivedm.BLiveClient, message: web_models.DanmakuMessage):
        print(f'[{client.room_id}] {message.uname}：{message.msg}')
        DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookietcat, cookie11 = json_read()
        if message.uname != UpName and message.msg != "":
                Msg = SparkApiGetReturn.Msg_Xinghuo_Retrun(message.msg)
                time2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                with open('./resource/BilibiliBarrage.log', 'a') as f:
                    lines = [message.uname,":   ", message.msg,"。"]
                    f.writelines(lines)
                    f.write("\r\n")

                    lines = [ "回复：",UpName+": ",str(Msg),time2]
                    f.writelines(lines)
                    f.write("\r\n")
                    f.write("\r\n")
                    f.write("\r\n")


                sendMessage(Msg,bili_jct=bili_jct,cookie=cookie11)
        if message.uname == UpName and message.msg == "[比心]":
            client.stop()

    def _on_gift(self, client: blivedm.BLiveClient, message: web_models.GiftMessage):

        print(f'[{client.room_id}] {message.uname} 赠送{message.gift_name}x{message.num}'
              f' （{message.coin_type}瓜子x{message.total_coin}）')
        DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookietcat, cookie11 = json_read()
        Msg = "感谢"+message.uname+"大哥赠送的"+message.coin_type+"[比心][比心]"
        time2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('./resource/BilibiliBarrage.log', 'a') as f:
            f.write("\r\n")
            f.write("==============================================")
            lines = [message.uname, ":   ", Msg, "。"]
            f.writelines(lines)
            f.write("\r\n")
            f.write("==============================================")
        sendMessage(Msg, bili_jct=bili_jct, cookie=cookie11)

    def _on_buy_guard(self, client: blivedm.BLiveClient, message: web_models.GuardBuyMessage):
        print(f'[{client.room_id}] {message.username} 购买{message.gift_name}')

    def _on_super_chat(self, client: blivedm.BLiveClient, message: web_models.SuperChatMessage):
        print(f'[{client.room_id}] 醒目留言 ¥{message.price} {message.uname}：{message.message}')


def BarrageDetectRun():
    print("正在监听直播间~~~~~~~~~~~~")
    global room_id
    global live_status
    global titie
    global UpName
    global SESSDATA
    global TEST_ROOM_IDS
    TEST_ROOM_IDS = [
        '1'
    ]
    SESSDATA = ''
    room_id = BilibiRequest.getRoomID()
    # 直播间ID的取值看直播间URL
    TEST_ROOM_IDS = [
        room_id
    ]
    try:
        live_status, title, UpName = BilibiRequest.getBilibiliLiveStatusFromURL()
    except:
        pass
    asyncio.run(main())

