import json
import os
import time

jsonPath = './resource/cookie.json'
imgpath = './img/1.png'
ffmpegpath = './resource/ffmpeg.exe'

def json_write(DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat):
    if os.path.exists(jsonPath):
        test_dict = {
            'DedeUserID': DedeUserID,
            'DedeUserID__ckMd5': DedeUserID__ckMd5,
            'SESSDATA': SESSDATA,
            'bili_jct': bili_jct,
            'sid': sid,
            'cookiecat': cookiecat,
            'cookie': cookiecat + "bili_jct=" + bili_jct + "; SESSDATA=" + SESSDATA + "; sid=" + sid + "; DedeUserID=" + DedeUserID + ";  DedeUserID__ckMd5=" + DedeUserID__ckMd5 + "; "
        }

        json_str = json.dumps(test_dict)
        new_dict = json.loads(json_str)
        with open(jsonPath, "w") as f:
            json.dump(new_dict, f)
            print("加载入文件完成...")
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
            print("加载入文件完成...")


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
