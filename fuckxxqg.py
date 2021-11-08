import requests
url='https://login.xuexi.cn/login/qrcommit?'
parm={'showmenu':'false',
    'code':'qr:E5C153C8-63D1-4D35-B52E-03D9F66E5B54',
    'appId':'dingoankubyrfkttorhpou'}
heads={'User-Agent':'Mozilla/5.0 (Linux; U; Android 10; zh-CN; Redmi K20 Pro Premium Edition Build/QKQ1.190716.003) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.2.96 Mobile Safari/537.36 AliApp(DingTalk/4.5.15) cn.xuexi.android/12446789 Channel/700169 language/zh-CN Device/XueXi XueXi/2.8.0'}

result=requests.get(url,headers=heads,params=parm)

with open('./xuexi.html','w',encoding='utf-8') as fp:
    fp.write(result.text)
    
print('ok')