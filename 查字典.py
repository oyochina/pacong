import requests


kw=input('请录入搜索词：')
url='https://fanyi.baidu.com/sug'
parm={"kw":kw}
Header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
theresponse=requests.post(url=url,params=parm,headers=Header)
result=theresponse.json()
with open('./sogou.html','w',encoding='utf-8') as fp:
    fp.write(theresponse.text)