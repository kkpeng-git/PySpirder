import requests
import json


def main():
    url = 'https://fanyi.baidu.com/sug'
    word = input('enter a word:')
    data = {
        'kw': word
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    response = requests.post(url=url, data=data, headers=headers)
    dic_obj = response.json()

    fileName = word+'.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)  # 有中文使用 ensure_ascii=False
    print('over')


if __name__ == '__main__':
    main()
