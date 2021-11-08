import requests


kw=input('请录入搜索词：')
url='https://www.sogou.com/web?'
parm={"query":kw}
Header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
theresponse=requests.get(url=url,params=parm,headers=Header)

with open('./sogou.html','w',encoding='utf-8') as fp:
    fp.write(theresponse.text)