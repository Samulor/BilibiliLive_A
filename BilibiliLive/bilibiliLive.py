import shlex
import subprocess
import jsonTest
import BilibiRequest
import time

FailedOrSuccess = False


def RunTest(filepath, FailedOrSuccess, ii,reflashurl="123456789"):
    if BilibiRequest.getBilibiliLiveStatusFromURL()[0] == 'OnLive':
        reflashurl = BilibiRequest.getreflashrtmp()
        url = "rtmp://live-push.bilivideo.com/live-bvc/" + reflashurl
        shell_cmd = (
                jsonTest.ffmpegpath + " -re -stream_loop -1 -i " + filepath + " -acodec aac -ar 32000 -vcodec copy -f flv " + url)
        cmd = shlex.split(shell_cmd)
        # p = subprocess.Popen(cmd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # 下面这么写能在打包的时候隐藏ffmpeg黑窗
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1,
                             creationflags=0x08000000)
        while p.poll() is None:
            line = p.stdout.readline()
            line = line.strip()
            if line:
                string = str(line, 'utf-8')
                print(string)
                if string.count("error") != 0 or string.count("Conversion failed!") != 0 or string.count(
                        "Network is unreachable") != 0 or string.count("Error number") != 0:
                    DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, cookiecat, cookie = jsonTest.json_read()
                    #if BilibiRequest.getBilibiliLoginStatus()[0] == '账号已登录':
                    if FailedOrSuccess == True:
                        FailedOrSuccess = False
                        RunTest(filepath, FailedOrSuccess, ii, reflashurl)
                    else:
                        print("视频失败，正在重新尝试，休整十秒。。。")
                        time.sleep(10)
                        RunTest(filepath, FailedOrSuccess, ii, reflashurl)
                        ii = ii + 1
                    if ii >= 10:
                        print("已经尝试超过十次，请检查网络或者更改视频")
                        break

    else:
        FailedOrSuccess = False
        pass
    time.sleep(10)
    return FailedOrSuccess,ii


def Run(filepath):
    RunTest(filepath, False,0)



