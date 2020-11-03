import requests
from bs4 import BeautifulSoup

url = "https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=3.def.0.base&wq=%E5%8D%8E%E4%B8%BA&pvid=c5541a7e95764263922284f59eefee00"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3777.400 QQBrowser/10.6.4212.400',
}

html = requests.get(
    url=url,
    headers=headers,
)
soup = BeautifulSoup(html.text, 'lxml')
title = soup.select("#J_goodsList > ul > li:nth-child(2) > div > div.p-name.p-name-type-2 > a")
print(title)
