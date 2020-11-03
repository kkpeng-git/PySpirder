import re

import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
# from bs4 import BeautifulSoup


def get_page_index(offset, keyword):
    data = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': '1583582997991',
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 "
                      "Safari/537.36 Core/1.70.3742.400 QQBrowser/10.5.3864.400",
        'cookie': 'csrftoken=2f9474bc7bbf66f39a7a4cb1b0798042; tt_webid=6801435111272809992; SLARDAR_WEB_ID=3e958e79-d9c5-4d91-a78d-ff304ea49868; s_v_web_id=verify_k7hl89fu_iP3uRNgZ_Z7LC_4jOb_9tWs_SXfHn5bXDYFK; __tasessionId=kd7lxfgnb1583584341129; ttcid=3fc308a922124ea186ad84ab86dce8ba54; tt_scid=Ao4IXu5JoLSWTXKkJf7H2v-ZaUWZsNk6fYT4SL6x806GN7ghKVp6xQyhrC7u1UjTf7db; tt_webid=6801435111272809992; WEATHER_CITY=%E5%8C%97%E4%BA%AC'
    }
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response.text
    except RequestException:
        print('请求失败')
        return None


def parse_page_index(html):
    data = json.loads(html)  # 字符串转Json数据
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'cookie': 'csrftoken=2f9474bc7bbf66f39a7a4cb1b0798042; tt_webid=6801435111272809992; SLARDAR_WEB_ID=3e958e79-d9c5-4d91-a78d-ff304ea49868; s_v_web_id=verify_k7hl89fu_iP3uRNgZ_Z7LC_4jOb_9tWs_SXfHn5bXDYFK; __tasessionId=kd7lxfgnb1583584341129; ttcid=3fc308a922124ea186ad84ab86dce8ba54; tt_scid=6cZ6MDHjsPgGbdYkn8C67VC.YCXINS9dJf8.0xrohoZYerYR6JgOJjWRqI.x0t6-a802',
        'authority': 'www.toutiao.com',
        'path': '/a6777243413981954575/',
        'scheme': 'https',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3742.400 QQBrowser/10.5.3864.400'
    }
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response.text
    except RequestException:
        print('请求详细页出错', url)
        return None


def parse_page_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()  # 获取标题
    print(title)
    images_pattern = re.compile('articleInfo: {.*?content:(.*?)groupId', re.S)
    result = re.search(images_pattern, html)
    if result:
        print(result.group(1))


def main():
    html = get_page_index(0, '街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            parse_page_detail(html)
            print("==================")


if __name__ == '__main__':
    main()
