import urllib.request, sys
import ssl

def get_phone_address(phone_number = '15629862601'):
    host = 'https://lhsjgsd.market.alicloudapi.com'
    path = '/sjgsd/mobile/area'
    method = 'POST'
    appcode = '71e6b749f047437dacdd80ee6476d49c'
    querys = ''
    bodys = {}
    url = host + path

    bodys['mobile'] = phone_number
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
    get_phone_address('13140121269')