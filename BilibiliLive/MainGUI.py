import json
import os
import time

import httpx
import qrcode
from PyQt5 import QtWidgets
import sys
import qtawesome
from PyQt5.QtCore import pyqtSignal, QEventLoop, QTimer, QThread
from PyQt5.QtGui import QTextCursor, QPixmap
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QFileDialog, QMessageBox, QComboBox, \
    QDialog, QLabel

import jsonTest
import sample
import BilibiRequest
import bilibiliLive
from jsonTest import jsonPath,imgpath
token = ''
scanFlag = False

class MyThreadOne(QThread):
    signalForText = pyqtSignal(str)

    def __init__(self, data=None, parent=None):
        super(MyThreadOne, self).__init__(parent)
        self.data = data


    def write(self, text):
        self.signalForText.emit(str(text))  # 发射信号

    def run(self):
        # 演示代码
        try:
            BilibiRequest.getStart(LiveAera)
            bilibiliLive.RunTest(filepath,True,0)
        except:
            BilibiRequest.getStart("88")
            bilibiliLive.RunTest(filepath, True, 0)

    def flush(self):
        pass

class MyThreadTwo(QThread):
    signalForText = pyqtSignal(str)

    def __init__(self, data=None, parent=None):
        super(MyThreadTwo, self).__init__(parent)
        self.data = data

    def write(self, text):
        self.signalForText.emit(str(text))  # 发射信号

    def run(self):
        # 演示代码

        BilibiRequest.stoprtmp()

    def flush(self):
        pass

class MyThreadThree(QThread):
    signalForText = pyqtSignal(str)

    def __init__(self, data=None, parent=None):
        super(MyThreadThree, self).__init__(parent)
        self.data = data

    def write(self, text):
        self.signalForText.emit(str(text))  # 发射信号

    def run(self):
        # 演示代码
        BilibiRequest.setStartArea(LiveAera)
    def flush(self):
        pass
class MyThreadFour(QThread):
    signalForText = pyqtSignal(str)

    def __init__(self, data=None, parent=None):
        super(MyThreadFour, self).__init__(parent)
        self.data = data

    def write(self, text):
        self.signalForText.emit(str(text))  # 发射信号

    def run(self):
        # 演示代码
        global token
        print("run----token::",token)
        i = 0
        while True:
            with httpx.Client() as client:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
                }
                url = f"https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key={token}&source=main-fe-header"
                data_login = client.get(url=url, headers=headers)  # 请求二维码状态
                data_login = json.loads(data_login.text)
            code = int(data_login['data']['code'])
            if code == 0:
                global scanFlag
                scanFlag = TransferData2(True)
                cookie_2 = dict(client.cookies)
                try:
                    with open(jsonTest.jsonPath, 'w') as f:
                        json.dump(cookie_2, f, ensure_ascii=False)
                except FileNotFoundError:
                    os.mkdir('cookie')
                    with open(jsonTest.jsonPath, 'w') as f:
                        json.dump(cookie_2, f, ensure_ascii=False)
                break
            else:
                scanFlag = False
            time.sleep(3)
            i = i + 1
            if i >= 60:
                print("登录超时，请重新按下登录按钮，获取二维码")
                break
        if i >= 60:
            print("登录超时，请重新按下登录按钮，获取二维码")
        else:
            with open(jsonTest.jsonPath, 'r') as load_f:
                load_dict = json.load(load_f)
            DedeUserID = load_dict['DedeUserID']
            DedeUserID__ckMd5 = load_dict['DedeUserID__ckMd5']
            SESSDATA = load_dict['SESSDATA']
            bili_jct = load_dict['bili_jct']
            sid = load_dict['sid']
            jsonTest.json_write(DedeUserID, DedeUserID__ckMd5, SESSDATA, bili_jct, sid, '')

        print("End")

    def flush(self):
        pass
class MyThreadFive(QThread):
    signalForText = pyqtSignal(str)

    def __init__(self, data=None, parent=None):
        super(MyThreadFive, self).__init__(parent)
        self.data = data

    def write(self, text):
        self.signalForText.emit(str(text))  # 发射信号

    def run(self):
        # 演示代码
        #BilibiliCookieGet.loginBilibili(cookiecat='')
        sample.BarrageDetectRun()
        print("End")

    def flush(self):
        pass

class MyThreadSix(QThread):
    signalForText = pyqtSignal(str)

    def __init__(self, data=None, parent=None):
        super(MyThreadSix, self).__init__(parent)
        self.data = data

    def write(self, text):
        self.signalForText.emit(str(text))  # 发射信号

    def run(self):
        # 演示代码
        #BilibiliCookieGet.loginBilibili(cookiecat='')
        #sample.BarrageDetectRun()
        print("End")

    def flush(self):
        pass

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.th1 = MyThreadOne()
        self.th1.signalForText.connect(self.onUpdateText1)
        self.th2 = MyThreadTwo()
        self.th2.signalForText.connect(self.onUpdateText2)

        sys.stdout = self.th1

    # 槽函数，用于更新文本编辑框的内容
    def onUpdateText1(self, text):
        cursor = self.process_One.textCursor()  # 获取文本编辑框的光标
        cursor.movePosition(QTextCursor.End)  # 移动光标到文本末尾
        cursor.insertText(text)  # 插入文本
        self.process_One.setTextCursor(cursor)  # 设置文本编辑框的光标
        self.process_One.ensureCursorVisible()  # 确保光标可见

    def onUpdateText2(self, text):
        cursor = self.process_One.textCursor()  # 获取文本编辑框的光标
        cursor.movePosition(QTextCursor.End)  # 移动光标到文本末尾
        cursor.insertText(text)  # 插入文本
        self.process_One.setTextCursor(cursor)  # 设置文本编辑框的光标
        self.process_One.ensureCursorVisible()  # 确保光标可见

    def init_ui(self):
        #使用提示
        if not os.path.exists('./img'):
            os.makedirs('./img')
        if not os.path.exists('./resource'):
            os.makedirs('./resource')
        if not os.path.exists("./resource/BilibiliBarrage.log"):
            file = open("./resource/BilibiliBarrage.log", "w")
            file.write("\r\n")
            file.close()

        self.Status = BilibiRequest.getBilibiliLoginStatus()
        serverStatus = 'yes'
        self.RunAhoRight = False
        self.FirstFlage = True
        loginButtonTitle = "登录"
        if self.Status[0] == "账号已登录" and serverStatus == "yes" and self.Status[1] != '房间不存在':
            QMessageBox.information(self, "状态",
                                    "账号已登录,互联网链接正常，服务器状态正常",
                                    QMessageBox.Yes)
            loginButtonTitle = "登出"
            loginButtonIco = qtawesome.icon('fa.sitemap', color='red')
            self.RunAhoRight = True

        elif self.Status[0] == "账号已登录" and serverStatus == "yes" and self.Status[1] == '房间不存在':
            QMessageBox.information(self, "状态",
                                    "账号已登录,互联网链接正常，服务器状态正常,直播间权限未开通，请开通后重试。点击Yes，重新登录B站账号",
                                    QMessageBox.Yes)
            os.remove(jsonPath)

        elif self.Status[0] != "账号已登录" and serverStatus != "yes":
            QMessageBox.information(self, "状态",
                                    "账号未登录,互联网链接异常，服务器状态异常（可能授权过期，可能作者服务器在离线状态，请重试）",
                                    QMessageBox.Yes)
        elif self.Status[0] == "账号已登录" and serverStatus != "yes":
            QMessageBox.information(self, "状态",
                                    "账号已登录,互联网链接正常，服务器状态异常（可能授权过期，可能作者服务器在离线状态，请重试）",
                                    QMessageBox.Yes)
        else:
            QMessageBox.information(self, "状态",
                                    "账号未登录,互联网链接正常，服务器状态正常",
                                    QMessageBox.Yes)
            loginButtonTitle = "登录"
            loginButtonIco = qtawesome.icon('fa.sitemap', color='green')
            self.RunAhoRight = True

        if self.RunAhoRight:
            self.setFixedSize(1220, 750)
            self.setWindowTitle('谢老师最帅~~~谢老师YYDS~~~~')
            # self.setWindowIcon(qtawesome.icon('fa.reddit-alien', color='blue'))

            self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
            self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
            self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

            # 创建和设置搜索框部件
            self.widget = QtWidgets.QWidget()
            self.widget.setObjectName('widget')
            self.layout = QtWidgets.QGridLayout()
            self.widget.setLayout(self.layout)  # 设置部件布局为网格

            self.main_layout.addWidget(self.widget, 0, 2, 12, 10)
            self.setCentralWidget(self.main_widget)  # 设置窗口主部件
            # 创建搜索按钮和搜索框，并设置布局
            self.bar_widget = QtWidgets.QWidget()  # 顶部搜索框部件
            self.bar_layout = QtWidgets.QGridLayout()  # 顶部搜索框网格布局
            self.bar_widget.setLayout(self.bar_layout)
            # 按钮1
            self.buttonOneToStart = QtWidgets.QPushButton(qtawesome.icon('fa.sign-in', color='green'), "一键开播")
            self.buttonOneToStart.clicked.connect(self.genMastClicked_One)
            self.buttonOneToStart.setObjectName('button1')
            self.buttonOneToStart.setFont(qtawesome.font('fa', 16))
            # 按钮2
            self.buttonOneToStop = QtWidgets.QPushButton(qtawesome.icon('fa.sign-out', color='red'), "一键停播")
            self.buttonOneToStop.clicked.connect(self.getThTwoClick)
            self.buttonOneToStop.setObjectName('button2')
            self.buttonOneToStop.setFont(qtawesome.font('fa', 16))
            # 按钮3
            self.button_resettitle = QtWidgets.QPushButton(qtawesome.icon('fa.hand-lizard-o', color='red'), "修改标题")
            self.button_resettitle.clicked.connect(self.getThThreeClickOnResetTitle)
            self.button_resettitle.setObjectName('button3')
            self.button_resettitle.setFont(qtawesome.font('fa', 16))
            # 修改标题键
            self.LineEditForTitle = QLineEdit(self)
            self.LineEditForTitle.setPlaceholderText("输入标题后按上方修改标题按钮")
            self.button_resettitle.setEnabled(False)
            # 检测是否修改了输入框
            self.LineEditForTitle.textChanged.connect(self.checkResetTitle_input)
            # 设置标题获取动态

            # 状态信息
            self.buttonLiveStatus = QtWidgets.QPushButton(qtawesome.icon('fa.chevron-circle-right', color='red'),
                                                          "LiveStatus")
            self.buttonLiveStatus.clicked.connect(self.getThFourClickOnLiveStatus)
            self.buttonLiveStatus.setObjectName('button4')

            self.buttonTitleStatus = QtWidgets.QPushButton(qtawesome.icon('fa.chevron-circle-right', color='red'),
                                                           "TitleStatus")
            self.buttonTitleStatus.clicked.connect(self.getThFiveClickOnTitleStatus)
            self.buttonTitleStatus.setObjectName('button5')

            self.LineLiveStatus = QLineEdit(self)
            self.LineLiveStatus.setReadOnly(True)
            self.LineLiveStatus.setText("请按左边按钮以刷新")
            self.LineLiveStatus.setStyleSheet("background-color: #f0f0f0; border: none;font-weight:bold;")

            self.LineTitleStatus = QLineEdit(self)
            self.LineTitleStatus.setReadOnly(True)
            self.LineTitleStatus.setText("请按左边按钮以刷新")
            self.LineTitleStatus.setStyleSheet("background-color: #f0f0f0; border: none;font-weight:bold;")

            # 布局添加
            self.bar_layout.addWidget(self.buttonOneToStart, 0, 0, 1, 1)
            self.bar_layout.addWidget(self.buttonOneToStop, 1, 0, 1, 1)

            self.bar_layout.addWidget(self.buttonLiveStatus, 0, 2, 1, 1)
            self.bar_layout.addWidget(self.buttonTitleStatus, 1, 2, 1, 1)
            self.bar_layout.addWidget(self.LineLiveStatus, 0, 3, 1, 1)
            self.bar_layout.addWidget(self.LineTitleStatus, 1, 3, 1, 1)

            self.bar_layout.addWidget(self.button_resettitle, 0, 4, 1, 1)
            self.bar_layout.addWidget(self.LineEditForTitle, 1, 4, 1, 1)

            # 部件到主布局
            self.layout.addWidget(self.bar_widget, 0, 0, 1, 9)

            # 登录
            self.buttonLogin = QtWidgets.QPushButton(loginButtonIco, loginButtonTitle)
            self.buttonLogin.clicked.connect(self.onclickLogin)
            self.buttonLogin.setObjectName('button6')

            self.buttonChooseLiveFile = QtWidgets.QPushButton(qtawesome.icon('fa.video-camera', color='red'),
                                                              "选择直播录像")
            self.buttonChooseLiveFile.clicked.connect(self.openFile)
            self.buttonChooseLiveFile.setObjectName('button7')

            self.LineChooseFile = QLineEdit(self)
            self.LineChooseFile.setReadOnly(True)
            self.LineChooseFile.setText("请按左边按钮，以选择文件。。")
            self.LineChooseFile.setStyleSheet("background-color: #f0f0f0; border: none;font-weight:bold;")

            Pdict, Clist = BilibiRequest.getLiveAreaList()
            #################################################
            #大类
            self.catalog1 = QComboBox(self)
            self.catalog1.addItem('默认大类网游')
            Plist = list(Pdict.keys())
            for i in Plist:
                self.catalog1.addItem(i)

            #self.catalog1.setGeometry(10, 40, 100, 30)
            #小类
            self.catalog2 = QComboBox(self)
            self.catalog2.addItem('默认小类CF')
            #self.catalog2.changeEvent(lambda x:x+1)

            self.catalog1.currentIndexChanged.connect(self.changePnameConnect)
            self.catalog2.currentIndexChanged.connect(self.changeCnameConnect)

            # 只有当OpenFile函数鉴定完权限之后才能开启，由登录按钮控制
            self.checkBox_1 = QtWidgets.QCheckBox(self)
            self.checkBox_1.setObjectName("checkBox_1")
            self.checkBox_1.setText("监听回复弹幕")
            self.checkBox_1.clicked.connect(self.onCheckBox1Click)

            self.checkBox_2 = QtWidgets.QCheckBox(self)
            self.checkBox_2.setObjectName("checkBox_2")
            self.checkBox_2.setText("服务器监听请求")
            self.checkBox_2.clicked.connect(self.onCheckBox2Click)
            self.checkBox_2.setEnabled(False)

            self.LineBname = QLineEdit(self)
            self.LineBname.setReadOnly(True)
            self.LineBname.setEnabled(False)
################################################################################

            self.ProcessAndFile_widget = QtWidgets.QWidget()
            self.DisplayAndProcess = QtWidgets.QGridLayout()

            self.ProcessAndFile_widget.setLayout(self.DisplayAndProcess)

            # 设置进程1
            self.process_One = QTextEdit(self, readOnly=True)
            self.process_One.ensureCursorVisible()
            self.process_One.setLineWrapColumnOrWidth(1100)
            self.process_One.setLineWrapMode(QTextEdit.FixedPixelWidth)
            self.process_One.setFixedWidth(1100)
            self.process_One.setFixedHeight(500)
            self.process_One.move(30, 50)
            self.buttonLogin.setEnabled(True)

            if self.Status[0] == "账号已登录":
                self.buttonLiveStatus.setEnabled(True)
                self.buttonTitleStatus.setEnabled(True)
                self.buttonChooseLiveFile.setEnabled(True)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.LineTitleStatus.setText("十年磨一剑")
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                self.checkBox_1.setEnabled(False)
                try:
                    Login, uname = BilibiRequest.getBilibiliUserInfoLogin()
                    self.LineBname.setText(uname)
                except:
                    self.LineBname.setText("请先登录以获取B站名称")




            else:
                self.buttonLiveStatus.setEnabled(False)
                self.buttonTitleStatus.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(False)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.button_resettitle.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                self.checkBox_1.setEnabled(False)
                self.LineBname.setText("请先登录，以获取B站名称")

            # 设置进程2
            # self.process_Two = QTextEdit(self, readOnly=True)
            # self.process_Two.ensureCursorVisible()
            # self.process_Two.setLineWrapColumnOrWidth(800)
            # self.process_Two.setLineWrapMode(QTextEdit.FixedPixelWidth)
            # self.process_Two.setFixedWidth(500)
            # self.process_Two.setFixedHeight(250)
            # self.process_Two.move(30, 50)
            # 添加布局
            self.DisplayAndProcess.addWidget(self.process_One, 0, 1)
            # self.recommend_layout.addWidget(self.process_Two, 0, 2)
            # 添加总布局
            self.layout.addWidget(self.buttonLogin, 1, 0, 1, 1)
            self.layout.addWidget(self.buttonChooseLiveFile, 1, 1, 1, 2)
            self.layout.addWidget(self.LineChooseFile, 1, 3, 1, 6)
            ###########################################################################
            self.layout.addWidget(self.catalog1, 2, 0, 1, 1)
            self.layout.addWidget(self.catalog2, 2, 1, 1, 1)
            self.layout.addWidget(self.checkBox_1,2, 2, 1, 2)
            self.layout.addWidget(self.checkBox_2,2, 4, 1, 2)
            self.layout.addWidget(self.LineBname,2,6,1,3)

            self.layout.addWidget(self.ProcessAndFile_widget, 3, 0, 2, 9)
            scanFlag = False
            # 使用QSS和部件属性美化窗口部件
            self.widget.setStyleSheet('''
                QWidget#widget{
                    color:#232C51;
                    background:white;
                    border-top:1px solid darkGray;
                    border-bottom:1px solid darkGray;
                    border-right:1px solid darkGray;
                }
                QLabel#lable{
                    border:none;
                    font-size:16px;
                    font-weight:700;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                }
                QPushButton#button:hover{border-left:4px solid red;font-weight:700;}
            ''')
        else:
            self.closeEvent(self)
            pass


    def onCheckBox1Click(self):

        try:
            if self.checkBox_1.isChecked():
                self.t5 = MyThreadFive()
                self.t5.start()
                print("监听开始！！！！")
                self.checkBox_1.setEnabled(False)
            else:
                print("监听停止！！！！")
        except Exception as g:
            raise g


    def onCheckBox2Click(self):
        self.t6 = MyThreadSix()
        try:
            if self.checkBox_2.isChecked():
                    self.t6 = MyThreadSix()
                    self.t6.start()
            else:
                self.t6.pause()
                print("休整100秒")

        except Exception as f:
            raise f


    def changePnameConnect(self):

        Pname = self.catalog1.currentText()
        self.catalog2.setEnabled(True)
        self.catalog1.setEnabled(False)
        Cdata, Cid = BilibiRequest.getCidFromCPname(Pname)
        for i in Cdata:
            self.catalog2.addItem(i)

    def changeCnameConnect(self):
        try:
            if self.catalog1.isEnabled() == False and self.catalog2.isEnabled():
                Cname = self.catalog2.currentText()
                Pname = self.catalog1.currentText()
                Cdata, Cid = BilibiRequest.getCidFromCPname(Pname,Cname)
                print("选择的大类是：",Pname)
                print("选择的小类是：",Cname)
                area_v2 = str(Cid)
            else:
                area_v2 = '88'

            global LiveAera
            LiveAera = TransferData(area_v2)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)
            self.t3 = MyThreadThree()
            self.t3.start()
        except:
            print("错误，未知？？")
            self.buttonLiveStatus.setEnabled(False)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonChooseLiveFile.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)

    def openFile(self):
        try:
            OneclickStatus = BilibiRequest.getBilibiliLoginStatus()
            print("OnclickStatus[0]:",OneclickStatus[0])
            print("OnclickStatus[1]:",OneclickStatus[1])


            if OneclickStatus[1] == '房间存在' and OneclickStatus[0] == '账号已登录':
                status = BilibiRequest.getBilibiliUserInfoLogin()

                chooseLivesource = QMessageBox.question(self, '选择直播对象', '选择媒体文件--Yes;桌面直播--No',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
                if chooseLivesource == QMessageBox.Yes:

                    options = QFileDialog.Options()
                    options |= QFileDialog.DontUseNativeDialog
                    fileName, _ = QFileDialog.getOpenFileName(self, "选择文件", "",
                                                              "All Files (*.mp4);;All Files (*.avi)",
                                                              options=options)
                    if fileName:
                        global filepath
                        filepath = fileName
                        print(f"选择的文件：{fileName}")
                        self.LineChooseFile.setText(fileName)
                        if (str(fileName).find("mp4") != -1) and (str(fileName).find("avi") != -1):
                            self.buttonOneToStart.setEnabled(False)
                            print("目前只支持.mp4格式或者.avi格式！！！")
                        else:
                            self.button_resettitle.setEnabled(True)
                            self.buttonOneToStart.setEnabled(True)
                            self.buttonLiveStatus.setEnabled(True)
                            self.buttonTitleStatus.setEnabled(True)
                            self.catalog1.setEnabled(True)
                            self.catalog2.setEnabled(False)
                            self.checkBox_1.setEnabled(True)
                        self.LineBname.setText(status[1])



                else:
                    print("目前暂不支持桌面直播")
                    nodeinfo = QMessageBox.warning(self, '提示', '目前不支持桌面直播',
                                                            QMessageBox.Yes,
                                                            QMessageBox.Yes)
                    self.LineBname.setText(status[1])
                    pass


            elif OneclickStatus[1] == "房间不存在" and OneclickStatus[0] == "账号已登录":
                print("请开通直播间权限之后，再重试！！！！！！！！！！")
                print("请开通直播间权限之后，再重试！！！！！！！！！！")
                print("请开通直播间权限之后，再重试！！！！！！！！！！")
                self.buttonLiveStatus.setEnabled(False)
                self.buttonTitleStatus.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(False)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.button_resettitle.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                self.LineBname.setText("开通直播权限后再重试")

            elif OneclickStatus[0] == "账号已登录" and OneclickStatus[1] == "房间不存在":
                print("账号已过期，请重新登录！！！！！！")
                print("账号已过期，请重新登录！！！！！！")
                print("账号已过期，请重新登录！！！！！！")
                self.buttonLogin.setText("登录")
                self.buttonLogin.setIcon(qtawesome.icon('fa.sitemap', color='green'))
                self.buttonLiveStatus.setEnabled(False)
                self.buttonTitleStatus.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(False)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.button_resettitle.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                self.LineBname.setText("账号已过期，重新登录")

            else:
                print("未知错误！！！！！！！！！！！！！！")
                self.buttonLogin.setText("登录")
                self.buttonLogin.setIcon(qtawesome.icon('fa.sitemap', color='green'))
                self.buttonLiveStatus.setEnabled(False)
                self.buttonTitleStatus.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(False)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.button_resettitle.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                self.LineBname.setText("未知错误!")

        except:
            print("未知错误，请检查网络！！！！")
            self.buttonLiveStatus.setEnabled(False)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonChooseLiveFile.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)

    def checkResetTitle_input(self):
        if (self.LineEditForTitle.text() and self.buttonTitleStatus.isEnabled() ):
            self.button_resettitle.setEnabled(True)
        elif (self.LineEditForTitle.text() and self.buttonTitleStatus.isEnabled() == False):
            print("开通直播间权限或登录账号之后才能修改标题")
            self.button_resettitle.setEnabled(False)
        else:
            pass

    def BilibiliLiveTh(self):
        try:
            self.t1 = MyThreadOne()
            self.t1.start()
        except Exception as a:
            print("未知错误，请检查网络！！！！")
            self.buttonLiveStatus.setEnabled(False)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonChooseLiveFile.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)
            raise a

    def ThTwo(self):
        try:
            self.t2 = MyThreadTwo()
            self.t2.start()
        except Exception as b:
            raise b

    def loginTh(self):
        try:

            self.t4 = MyThreadFour()
            self.t4.start()


        except Exception as e:
            raise e

    def onclickLogin(self):
        """Runs the main function."""
        print('Running...')
        try:
            serverStatus = 'yes'

            status = BilibiRequest.getBilibiliUserInfoLogin()

            print(status)
            if serverStatus == "yes" and status[0] == False:
                a = QMessageBox.information(self, "关于对话框",
                                          "确定登录吗？",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
                if a == QMessageBox.Yes:
                    self.fault_show_function()
                    print("token",token)
                    self.loginTh()
                    self.LineBname.setText("点击选择直播视频以获取状态")
                    try:
                        BilibiRequest.sendMessage("[比心]")
                    except:
                        print("直播间可能未开通")
                else:
                    pass

            elif serverStatus == "yes" and status[0] == True:
                a = QMessageBox.information(self, "关于对话框",
                                          "确认登出吗",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
                if a == QMessageBox.Yes:
                    if BilibiRequest.getBilibiliUserInfoLogin()[0]:
                        BilibiRequest.stoprtmp()
                    self.checkBox_1.setChecked(False)
                    self.checkBox_1.setEnabled(False)
                    BilibiRequest.sendMessage("[比心]")
                    self.LineBname.setText("请先登录，以获取B站名称")

                    os.remove(jsonPath)
                    self.buttonLogin.setText("登录")
                    self.buttonLogin.setIcon(qtawesome.icon('fa.sitemap', color='green'))
                    self.buttonLiveStatus.setEnabled(False)
                    self.buttonTitleStatus.setEnabled(False)
                    self.buttonChooseLiveFile.setEnabled(False)
                    self.buttonOneToStop.setEnabled(False)
                    self.buttonOneToStart.setEnabled(False)
                    self.button_resettitle.setEnabled(False)
                    self.catalog1.setEnabled(False)
                    self.catalog2.setEnabled(False)
                    print("登出完成")
                elif a == QMessageBox.No:
                    pass

            elif serverStatus == 'no':
                reply = QMessageBox.about(self, "关于对话框", "授权已过期，请联系开发者")
                self.buttonLiveStatus.setEnabled(False)
                self.buttonTitleStatus.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(False)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.button_resettitle.setEnabled(False)
                self.buttonLogin.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                self.LineBname.setText("授权已过期，请联系开发者")
                print("reply::=====", reply)
            else:
                self.buttonLiveStatus.setEnabled(False)
                self.buttonTitleStatus.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(False)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.button_resettitle.setEnabled(False)
                self.buttonLogin.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                self.LineBname.setText("网络错误或者开发者服务器已关闭")

                reply = QMessageBox.about(self, "关于对话框", "网络错误或者开发者服务器已关闭")
                print("reply::=====", reply)
        except:
            self.buttonLiveStatus.setEnabled(False)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonChooseLiveFile.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.buttonLogin.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)
            self.LineBname.setText("网络错误或者开发者服务器已关闭")

            reply = QMessageBox.about(self, "关于对话框", "网络错误或者开发者服务器已关闭")
            print("reply::=====", reply)

        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()

    def fault_show_function(self):
        """返回qrcode链接以及token"""
        with httpx.Client() as client:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
            }
            url = 'https://passport.bilibili.com/x/passport-login/web/qrcode/generate?source=main-fe-header'
            data = client.get(url=url, headers=headers)
        total_data = data.json()
        qrcode_url = total_data['data']['url']
        qrcode_key = total_data['data']['qrcode_key']
        data = {}
        data['url'] = qrcode_url
        data['qrcode_key'] = qrcode_key

        global token
        global scanFlag

        token = data['qrcode_key']
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data['url'])
        qr.make(fit=True)
        # qr.print_ascii(out=None, tty=False, invert=False)
        img = qr.make_image(fill_color="black")
        img.save(jsonTest.imgpath)

        dialog_fault = QDialog()
        pic = QPixmap(imgpath)
        label_pic = QLabel("show", dialog_fault)
        label_pic.setPixmap(pic)
        label_pic.setGeometry(10,10,800,800)

        dialog_fault.exec_()
        os.remove(imgpath)
        if self.FirstFlage == True:
            scanFlag = True
            self.FirstFlage = False
        else:
            pass
        if scanFlag == False:
            print("扫码失败")
            self.buttonLogin.setText("登录")
            self.buttonLogin.setIcon(qtawesome.icon('fa.sitemap', color='green'))
            self.buttonChooseLiveFile.setEnabled(False)
            self.buttonLiveStatus.setEnabled(False)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)
            self.checkBox_1.setChecked(False)
            self.checkBox_1.setEnabled(False)
        else:
            scanFlag = False
            self.buttonLogin.setText("登出")
            self.buttonLogin.setIcon(qtawesome.icon('fa.sitemap', color='red'))
            self.buttonChooseLiveFile.setEnabled(True)
            self.buttonLiveStatus.setEnabled(True)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)
            self.checkBox_1.setChecked(False)
            self.checkBox_1.setEnabled(False)
            print("扫码成功")
        print("scanFlag=",scanFlag)
        scanFlag = False

    def genMastClicked_One(self):
        """Runs the main function."""
        print('Running...')
        try:
            serverStatus = 'yes'
            if serverStatus == "yes":
                QMessageBox.about(self, "关于对话框", "开播之后想停播，请先按一键停播，否则会一直挂后台")
                if os.path.exists('./resource/ffmpeg.exe'):
                    self.BilibiliLiveTh()
                    self.buttonOneToStart.setEnabled(False)
                    self.catalog1.setEnabled(False)
                    self.catalog2.setEnabled(False)
                    self.buttonOneToStop.setEnabled(True)
                    self.buttonChooseLiveFile.setEnabled(False)
                else:
                    print("报错！！！！！！关键文件ffmpeg不存在，位置 ./resource/ffmpeg.exe")

            elif serverStatus == 'no':
                QMessageBox.about(self, "关于对话框", "授权已过期，请联系开发者")
            else:
                QMessageBox.about(self, "关于对话框", "网络错误或者开发者服务器已关闭")
        except:
            print("未知错误，请重新登录！")
            self.buttonLogin.setText("登录")
            self.buttonLogin.setIcon(qtawesome.icon('fa.sitemap', color='green'))
            self.buttonLiveStatus.setEnabled(False)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonChooseLiveFile.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)

        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()

    def getThTwoClick(self):
        """一键停播 function."""
        print('Running...')
        try:
            serverStatus = 'yes'
            stopstatus = BilibiRequest.stoprtmp()
            if serverStatus == "yes":
                self.buttonOneToStart.setEnabled(True)
                self.buttonOneToStop.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(True)

            elif serverStatus == 'no':
                self.buttonLiveStatus.setEnabled(False)
                self.buttonTitleStatus.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(False)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.button_resettitle.setEnabled(False)
                self.buttonLogin.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                QMessageBox.about(self, "关于对话框", "授权已过期，请联系开发者")
            else:
                self.buttonLiveStatus.setEnabled(False)
                self.buttonTitleStatus.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(False)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.button_resettitle.setEnabled(False)
                self.buttonLogin.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                QMessageBox.about(self, "关于对话框", "网络错误或者开发者服务器已关闭")
        except:
            self.buttonLiveStatus.setEnabled(False)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonChooseLiveFile.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.buttonLogin.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)
            QMessageBox.about(self, "关于对话框", "服务器未开，或者网络未连接")
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()

    def getThThreeClickOnResetTitle(self):
        """Runs the main function."""
        print("正在尝试修改标题！！！！！！！！！！！！")
        try:
            serverStatus = 'yes'
            if serverStatus == 'yes':
                title = self.LineEditForTitle.text()
                res = BilibiRequest.resettitle(title)
                if res == '房间存在':
                    self.LineTitleStatus.setText(title)
                    print("修改标题完成！！！！！！！！！！！！")

                elif res == '房间不存在':
                    print("请开通直播间！！！！！！！！！！！！！")
                    self.buttonTitleStatus.setEnabled(False)
                    self.buttonLiveStatus.setEnabled(False)
                    self.button_resettitle.setEnabled(False)
                    self.buttonChooseLiveFile.setEnabled(False)
                    self.buttonOneToStop.setEnabled(False)
                    self.buttonOneToStart.setEnabled(False)
                    self.catalog1.setEnabled(False)
                    self.catalog2.setEnabled(False)

                else:
                    print("未知错误！！！！！请检查网络！！！！！")
            elif serverStatus == 'no':
                QMessageBox.about(self, "关于对话框", "授权已过期，请联系开发者")
                self.buttonLogin.setEnabled(False)
                self.buttonTitleStatus.setEnabled(False)
                self.buttonLiveStatus.setEnabled(False)
                self.button_resettitle.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(False)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                print("修改标题失败！！！！！！！！！！！！")

            else:
                QMessageBox.about(self, "关于对话框", "网络错误或者开发者服务器已关闭")
                self.buttonLogin.setEnabled(False)
                self.buttonTitleStatus.setEnabled(False)
                self.buttonLiveStatus.setEnabled(False)
                self.button_resettitle.setEnabled(False)
                self.buttonChooseLiveFile.setEnabled(False)
                self.buttonOneToStop.setEnabled(False)
                self.buttonOneToStart.setEnabled(False)
                self.catalog1.setEnabled(False)
                self.catalog2.setEnabled(False)
                print("修改标题失败！！！！！！！！！！！！")
        except:
            print("未知错误，请重新登录！！！！！！！！！！")
            self.buttonLogin.setText("登录")
            self.buttonLogin.setIcon(qtawesome.icon('fa.sitemap', color='green'))
            self.buttonLiveStatus.setEnabled(False)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonChooseLiveFile.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()

    def getThFourClickOnLiveStatus(self):
        """Runs the main function."""
        print('Running...')
        print("正在获取直播状态！！！！！！")
        try:
            self.LineLiveStatus.setText("正在获取直播状态中..........")
            statusLive = BilibiRequest.getBilibiliLiveStatusFromURL()[0]
            self.LineLiveStatus.setText(statusLive)

            if statusLive == 'OnLive':
                self.buttonOneToStop.setEnabled(True)

            print("直播状态获取完成！！！！！！")
        except:
            print("未知错误，请重新登录！")
            self.buttonLogin.setText("登录")
            self.buttonLogin.setIcon(qtawesome.icon('fa.sitemap', color='green'))
            self.buttonLiveStatus.setEnabled(False)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonChooseLiveFile.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()

    def getThFiveClickOnTitleStatus(self):
        """Runs the main function."""

        print("正在获取直播标题！！！！！！")
        try:
            self.LineTitleStatus.setText("正在获取直播标题中..........")
            title = BilibiRequest.getBilibiliLiveStatusFromURL()[1]
            self.LineTitleStatus.setText(title)
            self.LineEditForTitle.setText(title)
            self.button_resettitle.setEnabled(True)
            print("标题状态获取完成！！！！！！")
        except:
            print("未知错误，请重新登录！")
            self.buttonLogin.setText("登录")
            self.buttonLogin.setIcon(qtawesome.icon('fa.sitemap', color='green'))
            self.buttonLiveStatus.setEnabled(False)
            self.buttonTitleStatus.setEnabled(False)
            self.buttonChooseLiveFile.setEnabled(False)
            self.buttonOneToStop.setEnabled(False)
            self.buttonOneToStart.setEnabled(False)
            self.button_resettitle.setEnabled(False)
            self.catalog1.setEnabled(False)
            self.catalog2.setEnabled(False)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()

    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        if self.RunAhoRight:
            a = QMessageBox.question(self, '退出', '你确定要退出吗?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)  # "退出"代表的是弹出框的标题,"你确认退出.."表示弹出框的内容
            if a == QMessageBox.Yes:
                if BilibiRequest.getBilibiliUserInfoLogin()[0]:
                    BilibiRequest.stoprtmp()
                event.accept()  # 接受关闭事件
                sys.stdout = sys.__stdout__
                super().closeEvent(event)
                pass
            else:
                event.ignore()  # 忽略关闭事件
                pass
        else:
            sys.stdout = sys.__stdout__
            sys.exit(0)
            pass

def TransferData(aera_v2):
    #定义外函数传递变量
    global  LiveAear
    LiveAear = aera_v2
    return LiveAear

def TransferData2(scanFlag1):
    #定义外函数传递变量
    global  scanFlag
    scanFlag = scanFlag1
    return scanFlag
def main():
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    gui = MainUi()
    gui.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
