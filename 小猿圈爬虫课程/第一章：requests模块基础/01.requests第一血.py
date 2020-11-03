import requests


def main():
    url = 'https://www.sogou.com/'
    responese = requests.get(url)
    page_text = responese.text
    print(page_text)
    with open('./sougou.html', 'w', encoding='utf-8') as fq:
        fq.write(page_text)
    print('爬取结束')


if __name__ == '__main__':
    main()
