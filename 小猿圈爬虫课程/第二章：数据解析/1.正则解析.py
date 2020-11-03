import requests
import re
import os

'''
<div class="thumb">

<a href="/article/123668279" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12366/123668279/medium/96XDZ5N9MEPQMX5J.jpg" alt="糗事#123668279" class="illustration" width="100%" height="auto">
</a>
</div>

'''


def main():
    # 创建一个文件夹，用来保存所有的图片数据
    url = 'https://www.qiushibaike.com/imgrank/'
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    ex = '<div class="thumb">.*?<img src="(.*?) alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)
    for src in img_src_list:
        src = 'http:' + src
        print(src)
        # 请求到图片的二进制
        img_data = requests.get(url=src, headers=headers).content
        print(img_data)
        # 生成图片名称
        img_name = src.split('/')[-1]
        imgPath = 'qiutuLibs/' + img_name
        with open(imgPath, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！！！')


if __name__ == '__main__':
    main()
