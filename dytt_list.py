import requests
from bs4 import BeautifulSoup
import time

url_head = 'http://www.dytt8.net'

urls = []
for i in range(1,175):
    url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(i)
    urls.append(url)

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Connection':'keep-alive',
    'Cookie':'UM_distinctid=1611c509adb3e4-006a5f0a156593-5b412f19-100200-1611c509adc222; XLA_CI=7f1c7c1a329abe7169659f52a0f1edb3; CNZZDATA1260535040=1864926224-1516595346-null%7C1518398990',
    'Host':'www.dytt8.net',
    'If-Modified-Since':'Sun, 11 Feb 2018 06:24:33 GMT',
    'If-None-Match':"80a6fbfa0a3d31:2d8",
    'Referer':'http://www.dytt8.net/html/gndy/dyzz/20180211/56303.html',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'
}
# content = requests.get(url=url).content
# html = content.decode("gb2312","ignore")
# print(content.text)
# print(html.status_code)
def download(url,header):
    wb_data = requests.get(url,headers = header)
    wb_data.encoding = 'gb2312'
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.bd2 > div.bd3 > div.bd3r > div.co_area2 > div.co_content8 > ul  b > a')
    hrefs = soup.select('div.bd2 > div.bd3 > div.bd3r > div.co_area2 > div.co_content8 > ul  b > a')

    for title,href in zip(titles,hrefs):
        data = {
            'title' : title.get_text(),
            'href' : url_head+href.get('href'),
        }
        print(data)
        with open('.\\dytt_list.txt','a+',encoding='UTF-8') as f:
            f.write(str(title.get_text()) + ':' + url_head + href.get('href') + '\n')

for url1 in urls:
    time.sleep(1)
    download(url1,headers)


