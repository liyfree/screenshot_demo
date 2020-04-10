from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time


def get_image(url, pic_name):
    # chromedriver的路径
    chromedriver = r"/Users/huangyan/PycharmProjects/screenshot_demo/demo/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    # 设置chrome开启的模式，headless就是无界面模式
    # 一定要使用这个模式，不然截不了全页面，只能截到你电脑的高度
    chrome_options = Options()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    # 控制浏览器写入并转到链接
    driver.get(url)
    driver.set_window_size(375, 812)
    time.sleep(1)
    # 接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(width, height)
    # 将浏览器的宽高设置成刚刚获取的宽高
    driver.set_window_size(width, height)
    time.sleep(1)
    # 截图并关掉浏览器
    driver.save_screenshot(pic_name)
    driver.close()

if __name__ == '__main__':
    # 你输入的参数
    url = 'http://127.0.0.1:5000/select'
    now = datetime.now().strftime('%Y%m%d')
    get_image(url, now+'.png')

