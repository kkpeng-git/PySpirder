from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
from selenium.webdriver.chrome.options import Options
import pymongo
import time
from JDmeishi.config import MONGO_URL, MONGO_DB, MONGO_TABLE, KEYWORD

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

browser = webdriver.Chrome()   # 有界面
# browser = webdriver.Chrome(chrome_options=chrome_options)  # 无界面
wait = WebDriverWait(browser, 10)
browser.set_window_size(1400, 900)


def search():
    print("正在搜索")
    try:
        browser.get('https://www.jd.com/')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))  # 翻页的输入框
        input.send_keys(KEYWORD)  # 往输入框中打印  " 美食 "
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#search > div > div.form > button")))  # 获取搜索按钮
        submit.click()  # 点击搜索
        scroll_loading()  # 滚动进度条 用于抓取image时  已经加载了
        total = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b')))  # 总共多少页
        get_products()  # 获取数据
        return total.text
    except TimeoutException:
        return search()


def scroll_loading():  # 滚动进度条 用于抓取image时  已经加载了
    number = 400
    # 循环拖动鼠标滚轮，使当前页的所有商品信息加载完成
    for line in range(20):
        js = 'window.scrollTo(0,%s)' % number
        number += 500
        browser.execute_script(js)
        time.sleep(0.5)


def next_page(page_number):  # 翻页操作
    print("当前翻页", page_number)
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input')))  # 翻页的输入框
        input.clear()  # 清除当前内容
        input.send_keys(page_number)  # 往输入框中打印  页数
        input.send_keys(Keys.RETURN)  # 回车
        # 根据页数地方的高亮显示  判断是否进行翻页
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'),
                                             str(page_number)))
        scroll_loading()  # 滚动进度条 用于抓取image时  已经加载了
        get_products()
    except TimeoutException:
        next_page(page_number)


def get_products():  # 获取数据
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList > ul > li')))
    html = browser.page_source  # 拿到网页源代码
    doc = pq(html)  # 格式化,初始化
    items = doc('#J_goodsList > ul > li').items()
    for item in items:
        product = {
            'image': item.find('div.p-img > a > img').attr('src'),

            'price': item.find('div.p-price > strong > i').text(),
            'comment': item.find('div.p-commit > strong > a').text(),
            'title': item.find('div.p-name.p-name-type-2 > a').attr('title'),
            'shop': item.find('div.p-shop > span > a').text(),
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MONGODB成功', result)
    except Exception:
        print('存储到MONGODB失败', result)


def main():
    try:
        total = int(search())
        for i in range(2, total + 1):  # 翻页循环   从第2页开始
            next_page(i)
    except Exception:
        print('出错啦！！！')
    finally:  # finally  不管有没有出现这个异常，最后都要执行下面的操作
        browser.close()


if __name__ == '__main__':
    main()
