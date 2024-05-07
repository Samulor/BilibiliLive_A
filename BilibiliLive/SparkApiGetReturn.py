import SparkApi

#以下密钥信息从控制台获取
appid = "填写你的appid"     #填写控制台中获取的 APPID 信息
api_secret = "填写你的APISecret"   #填写控制台中获取的 APISecret 信息
api_key ="填写你的APIKey"    #填写控制台中获取的 APIKey 信息

#用于配置大模型版本，默认“general/generalv2”
#domain = "general"   # v1.5版本
domain = "generalv3"    # v2.0版本
#云端环境的服务地址
#Spark_url = "ws(s)://spark-api.xf-yun.com/v3.1/chat"  # v1.5环境的地址
Spark_url = "ws://spark-api.xf-yun.com/v3.1/chat"  # v2.0环境的地址


text =[]

# length = 0

def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text
    


def Msg_Xinghuo_Retrun(Msg):
    Msg = Msg + "(现在你是玩CF的B站女主播，你叫婷婷，娇俏可爱，15个字内回复，不要官方和生硬，像邻居家妹妹一样)"
    text.clear

    question = checklen(getText("user",Msg))
    SparkApi.answer = ""
    print("星火:",end = "")
    SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
    getText("assistant", SparkApi.answer)

    for i in range(len(question)):
        if question[i]['content'] == Msg:
            Msgquestion = Msg
    respon = "1"
    for i in range(len(text)):
        if text[i]['content']==Msgquestion:
            respon = text[i + 1]['content']
            break
    return respon

