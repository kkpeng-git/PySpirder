import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq

base_url = 'https://weixin.sogou.com/weixin?'

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'cookie': 'SUID=BF09C27A2C18960A000000005E4573F8; usid=W0akB2NKCdcXyMAL; SUV=000D7A697AC209FD5E4573FAE456C229; QIDIANID=/j13mbLilO00Wq0q0ml5Ssx2rV2ISxugD3cGkOuz9gKpnUNl8aIdJrjFPs6wFiuU1oJ/fJnu1H5FtU9Hhbcimw==; SMYUV=1581610858703725; UM_distinctid=1703f5a7a09660-02b656fa4a8e22-34564a78-1fa400-1703f5a7a0a298; ld=akllllllll2Wvv@NlllllViJGG7lllllWulo0yllllwlllll9llll5@@@@@@@@@@; IPLOC=CN3201; ABTEST=0|1583648547|v1; weixinIndexVisited=1; sct=1; JSESSIONID=aaaUJLe3jS2wrfwny8mcx; ppinf=5|1583648805|1584858405|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo2OkhhZG9vcHxjcnQ6MTA6MTU4MzY0ODgwNXxyZWZuaWNrOjY6SGFkb29wfHVzZXJpZDo0NDpvOXQybHVIWURZUFc3M3NGSFg5NDRxbWF6MUR3QHdlaXhpbi5zb2h1LmNvbXw; pprdig=oh4T1bkdqI01i9FqAsIX6wh_PLcn95dIhucGekLkuFSW2QHZrc6-Wl-Ynj-w4LOfTiIq_J1FWivjAszKpcF6DjyGEYkDyJ7av3T7jq-t3noASVnmYPi0LGPi0tKPK-nPusk87p__q3tOXTcFEuX1M5k_1uOWS45Z-yksX_FGQfM; sgid=21-46439795-AV5kkCWaaRBomAWDnQ9lHt4; PHPSESSID=aomk29g8v1lo8spri7mfnro3s2; CXID=063FF02E1E37AE1219D3B6F3AA970E30; ad=Llllllllll2WBJCklllllVi6XQllllllW7wJTZllllwllllljVxlw@@@@@@@@@@@; ppmdig=1583654719000000b17aaef107e2c28ef3e0f301d6d34aa2; SNUID=758145FD888D28DBDE0244528867CFD2',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3742.400 QQBrowser/10.5.3864.400',
}
keyword = '风景'
proxy_pool_url = 'http://localhost:5556/random'  # 代理接口

proxy = None  # 初始化代理为空
max_count = 5  # 定义失败的请求次数


def get_proxy():  # 使用代理
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def get_html(url, count=1):
    print('Crawling', url)
    print('Trying Count', count)
    global proxy  # 引用全局变量
    if count >= max_count:
        print("Tried Too Many Count")  # 请求次数已经达到上限，终止当前页面
        return None
    try:
        if proxy:
            proxies = {'http': 'https://' + proxy}
            response = requests.get(url, allow_redirects=False, headers=header,
                                    proxies=proxies)  # allow_redirects=False  不让他进行跳转  如果有代理，就使用代理
        else:
            response = requests.get(url, allow_redirects=False, headers=header)  # allow_redirects=False  不让他进行跳转
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:  # 如果 302 将设置代理
            print("===============302=============")
            proxy = get_proxy()
            if proxy:
                print('Using Proxy', proxy)
                count += 1
                return get_html(url,count)
            else:
                print("Get Proxy Failed")  # 获取不到代理了  爬不到了
                return None
    except ConnectionError as e:
        print('Error Occurred', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page,
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')


def main():
    for page in range(1, 101):
        html = get_index(keyword, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                print(article_url)


if __name__ == '__main__':
    main()

'''
/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS25R-Wyx2sSiTzCfmfqhrCIUaAyhhEBeMVqXa8Fplpd9mXE2CBPI-zfkarrLx8LaUc6sa11nZCTdY5lzLCWoLGrJ4d4LLnlxBlCvgW4__n0vXB8qnNC5MVeZy-3qwl_-bDbnVoJCXZSKR0DtURz2nw9xPR2oQnnqwuYMZkBCAMlbTqAP441D-w5BwYOyXH2BpQLICcZd8qOP6ZmgCy48plZ6VKrzu_4XKA..&type=2&query=%E9%A3%8E%E6%99%AF&token=0CD78B72758145FD888D28DBDE0244528867CFD25E64AE34
https://mp.weixin.qq.com/s?src=11&timestamp=1583656180&ver=2203&signature=apl7hMin7n7YntTwJeNcODLqAKRn0PvaMjUdxQo0z6SrWX77GD3j9pdAssklufQv7mTVhioN22E6O*lGH0nrW6oCCznKS8UIomAcX51rfwW-Vb5zNOB18kwqqBctvLvw&new=1
//img01.sogoucdn.com/net/a/04/link?appid=100520033&url=http://mmbiz.qpic.cn/mmbiz_jpg/XefnaOQb1gqTkWYt3bQrHWoklfL8vDf0FpRiajM5FQhkBCPVTQgCRgLqYBjjFzG9cz8OrsaKTKzblMSjNZkAnDA/0?wx_fmt=jpeg
'''
