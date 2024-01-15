import urllib.request, sys
import ssl

def send_verify_sms():
    host = 'https://dfsns.market.alicloudapi.com'
    path = '/data/send_sms'
    method = 'POST'
    appcode = '71e6b749f047437dacdd80ee6476d49c'
    querys = ''
    bodys = {}
    url = host + path

    bodys['content'] = '''code:1234'''
    bodys['template_id'] = '''CST_ptdie100'''
    bodys['phone_number'] = '''13140121269'''
    post_data = urllib.parse.urlencode(bodys).encode('utf-8')
    request = urllib.request.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    # 根据API的要求，定义相对应的Content-Type
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request, context=ctx)
    content = response.read().decode('utf-8')
    if (content):
        print(content)

if __name__ == '__main__':
    send_verify_sms()