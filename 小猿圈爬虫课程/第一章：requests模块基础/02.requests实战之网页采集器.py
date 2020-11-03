import requests


def main():
    url = 'https://www.sogou.com/web'
    kw = input('enter a word：')
    param = {
        'query': kw
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功')


if __name__ == '__main__':
    main()
