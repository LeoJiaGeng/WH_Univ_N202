import requests
import random
from hashlib import md5
import time

# GET 请求
def trans_Baidu_GET(query, APPID, APPKEY, fromlanguage = 'auto', tolanguage = 'en', action = 0):
    '''
    query: 待翻译内容
    APPID: 申请的 APP ID
    APPKEY: 申请的密钥
    fromlanguage: 待翻译语言; 'auto' 表示自动识别
    tolanguage: 翻译目标语言; 'zh' 表示中文
    * 语言代码见: https://api.fanyi.baidu.com/doc/21

    action: 1: 使用自定义术语干预API; 0: 不使用自定义术语干预API
    '''
    # 定义函数，作用是进行 MD5 并将散列值转换为 16 进制
    def make_md5(s, encoding = 'utf-8'):
        return md5(s.encode(encoding)).hexdigest()
    
    # 在 32768 至 65536 的范围内取随机数
    Salt = random.randint(32768, 65536)
    # 使用 APPID、请求 query、随机数和密钥构成签名
    Sign = make_md5(APPID + query + str(Salt) + APPKEY)

    # 发送请求的 URL
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    # 以字典形式编辑查询参数
    parameters = {'appid': APPID, 'q': query, 'from': fromlanguage, 'to': tolanguage, 'salt': Salt, 'sign': Sign}

    # 返回响应信息，并提取响应中的翻译结果
    response = requests.get(url, params = parameters)
    result_list = response.json()['trans_result']
    ## 提取翻译结果中的翻译后内容 (dst)
    result = '\n'.join(item['dst'] for item in result_list)
    return result

# POST 请求
def trans_Baidu_POST(query, APPID, APPKEY, fromlanguage = 'auto', tolanguage = 'zh', action = 0):
    # 定义函数，作用是进行 MD5 并将散列值转换为 16 进制
    def make_md5(s, encoding = 'utf-8'):
        return md5(s.encode(encoding)).hexdigest()
    Salt = random.randint(32768, 65536)
    Sign = make_md5(APPID + query + str(Salt) + APPKEY)
   
    # 发送通用翻译请求的 URL
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    # 根据 API 接入文档，指定 Content-Type 为 application/x-www-form-urlencoded
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    parameters = {'appid': APPID, 'q': query, 'from': fromlanguage, 'to': tolanguage, 'salt': Salt, 'sign': Sign}
    
    time.sleep(1)
    # 保存响应，并提取响应中的翻译结果
    response = requests.post(url, params = parameters, headers = headers)
    result_list = response.json()['trans_result']

    # 提取翻译结果中的翻译后内容 (dst)
    result = '\n'.join(item['dst'] for item in result_list)
    return result

if __name__ == "main":
    APPID = '20240109001936084'
    APPKEY = 'tpphd5ZQSEvFG4fpcHRc'
    # GET 请求
    answer1 = trans_Baidu_GET('成为企研·社科大数据平台会员，用最独家的数据，学最实用的Python，画最酷的图！', APPID, APPKEY)
    print(answer1)
    '''
    Become a member of the Enterprise Research Social Science Big Data Platform, use the most exclusive data, learn the most practical Python, and draw the coolest pictures!
    '''

    # POST 请求
    answer2 = trans_Baidu_POST('成为企研·社科大数据平台会员，\n用最独家的数据，\n学最实用的Python，\n画最酷的图！', APPID, APPKEY)
    print(answer2)
    '''
    Becoming a member of the Enterprise Research · Social Science Big Data Platform,
    Using the most exclusive data,
    Learn the most practical Python,
    Draw the coolest picture!
    '''
