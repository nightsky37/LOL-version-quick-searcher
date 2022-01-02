import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as req
import time


date = []
versionURL = []
picUrl = []


def dynamicScraping():
    url = "https://lol.garena.tw/news/patch"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    driver.get(url)
    html = driver.find_element_by_tag_name('html')
    for i in range(4):
        html.send_keys(Keys.END)
        time.sleep(1)
    time.sleep(1)
    root = bs4.BeautifulSoup(driver.page_source, "html.parser")
    return root


root = dynamicScraping()


def getDate():  # 擷取更新日期
    titles = root.find_all("h2")
    for title in titles:
        tmp = ""
        for t in range(5):
            tmp += title.string[t]
        date.append(tmp)


def getVerUrl():  # 取得版本更新網址
    version_list = root.select("div.newItem a")
    for v in version_list:
        tmp = "https://lol.garena.tw/"
        tmp += v['href']
        versionURL.append(tmp)


def getPicUrl():
    for url in versionURL:
        request = req.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        })
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(data, "html.parser")

        pic = root.find("div", class_="content black")
        picUrl.append(pic.img['src'])


getDate()
getVerUrl()
getPicUrl()
