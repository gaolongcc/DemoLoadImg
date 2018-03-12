from bs4 import BeautifulSoup
import requests
import re
import os

URL = "http://www.nationalgeographic.com.cn/index.php?m=content&c=index&a=lists&catid=596"
html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_url = soup.find_all('div',{"class": "showImg-list"})
os.makedirs('./img/' ,exist_ok = True)
for ul in img_url:
    imgs = ul.find_all('img',src=re.compile('\d+\.jpg'))
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream =True)
        image_name = url.split('/')[-1]
        with open('./img/%s'% image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
            print('Saved %s'% image_name)


