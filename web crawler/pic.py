#請修改:
#1.存圖位置
#2.爬取頁面網址
#3.啟動chrome瀏覽器
#4.請依照景點名稱更改'_???????'，到單引號中底線後面

from selenium import webdriver
import time
import urllib.request
import os

S='Pond Du Garre'
# 存圖位置
local_path = 'D:/Users/KoToRi/Desktop/0726/English/'+S
#local_path = 'D:/Users/KoToRi/Desktop/0511/Chinese/'+S
#爬取頁面網址

url = 'https://pic.sogou.com/pics?ie=utf8&p=40230504&interV=kKIOkrELjboLmLkElbYTkKIKmbELjboJmLkEkL8TkKIRmLkEk78TkKILkbFAwuUJk7nlWlyPNCSUM6IPje55zLcKkKR7zOMTNzSLBlyGHlgElKJ7ye9GwvAGwOVFmUHpGz2IOzXejb0Ew+dByOsG0OV/zPsGwOVF_1417321195&query=' + S
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1588951254340_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word='+S
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1595780401179_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E7%BD%97%E9%A9%AC%E6%A1%A5'



# 目標元素的xpath
#xpath = '//div[@class="figure-result"]/ul/li/a/img'
xpath = '//div[@id="imgid"]/div/ul/li/div/a/img'


# 啟動chrome瀏覽器
chromeDriver = r'D:/Users/KoToRi/Desktop/web crawler/chromedriver/chromedriver'  # chromedriver檔案放的位置
driver = webdriver.Chrome(chromeDriver)


# 最大化窗口，因為每一次爬取只能看到視窗内的圖片
driver.maximize_window()

# 紀錄下載過的圖片網址，避免重複下載
img_url_dic = {}

# 瀏覽器打開爬取頁面
driver.get(url)

# 模擬滾動視窗瀏覽更多圖片
pos = 0
m = 0  # 圖片編號
for i in range(100):
    pos += i * 500  # 每次下滾500
    js = "document.documentElement.scrollTop=%d" % pos
    driver.execute_script(js)
    time.sleep(1)

    for element in driver.find_elements_by_xpath(xpath):
        try:
            img_url = element.get_attribute('src')

            # 保存圖片到指定路徑
            if img_url != None and not img_url in img_url_dic:
                img_url_dic[img_url] = ''
                m += 1
                # print(img_url)
                ext = img_url.split('/')[-1]
                # print(ext)
 ###請依照景點名稱更改'_???????'，到單引號中底線後面.

                filename = str(m) + '_'+ S + '_' + ext + '.jpg'
                print(filename)

                # 保存圖片
                urllib.request.urlretrieve(img_url, os.path.join(local_path, filename))



        except OSError:
            print('發生OSError!')
            print(pos)
            break;


driver.close()