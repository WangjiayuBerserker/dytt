import requests
from bs4 import BeautifulSoup
import time



header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'UM_distinctid=1611c509adb3e4-006a5f0a156593-5b412f19-100200-1611c509adc222; CNZZDATA1260535040=1864926224-1516595346-null%7C1521023083',
    'Host':'www.dytt8.net',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'
}


def download_ftp(url,header):
    wb_data = requests.get(url,headers = header)
    wb_data.encoding = 'gb2312'
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select(' div.title_all > h1 > font')
    ftps = soup.select(' tbody > tr > td > a')
    for title,ftp in zip(titles,ftps):
        data = {
            'title':title.get_text(),
            'ftp':ftp.get_text()
        }
        with open('dytt_ftp.txt','a+',encoding='UTF-8') as f:
            f.write(title.get_text() + ' : ' + ftp.get_text() + '\n')


with open('.\\dytt_list.txt','r',encoding='UTF-8') as f:
    texts = f.readlines()
    for text in texts:
        time.sleep(1)
        url = text.split(':',1)[1].rstrip('\n')
        print(url)
        download_ftp(url,header)