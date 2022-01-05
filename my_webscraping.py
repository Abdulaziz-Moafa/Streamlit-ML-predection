import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv

items = []
item =name= []


dataframe=pd.read_csv(r"C:\Users\zezo0\Downloads\Gharwaalaa1\Gharwaalaa\GHPD11.csv", usecols=['name'])

dataframe.replace(to_replace ="Cake",
                 value = "cake",
                  inplace = True)
with open(r"C:\Users\zezo0\Downloads\Gharwaalaa1\Gharwaalaa\GHPD11.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        item.append(row['name'])


sub = 'cake'

cakes = [i for i in item if sub in i]

grocery = [i for i in item if sub not in i]


webdriver_path = r'C:\Users\zezo0\Downloads\chromedriver_win32\chromedriver.exe'
search_item = item
item_price = item_name2 = item_name1 = item_name = item_list = item_list1 = item = mrp = []
options = webdriver.ChromeOptions()

options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')


def scraping():
    global item_name1, item_name2, item_name, item_price, productlist, mrp, name, rp
    browser = webdriver.Chrome(webdriver_path, options=options)

    jiomart_url = 'https://www.jiomart.com/'

    browser.get(jiomart_url)
    search_bar = browser.find_element_by_id('search')

    for each in grocery:
        search_bar.send_keys(each)
        search_bar.send_keys(Keys.ENTER)

        try:
            item_name1 = browser.find_element_by_xpath('//*[@id="hits"]/div/div/ol/li[1]/div/a/span[4]').text.strip()

            item_name2 = browser.find_element_by_xpath('//*[@id="hits"]/div/div/ol/li[1]/div/a/span[3]').text.strip()
            item_name = item_name1 + item_name2
        except:
            item_name = each


        try:
            item_price = browser.find_element_by_xpath('//*[@id="final_price"]').text.strip()
        except:
            item_price = '-item_notavailable'

        try:
            mrp = browser.find_element_by_xpath('//*[@id="price"]').text.strip()
            rp = mrp[0][0]
            mrp = mrp.replace(rp, "")
        except:
            mrp = ""
        pr=item_price[0][0]
        item_price=item_price.replace(pr,"")

        productlist = {
            'name': item_name,

            'price': item_price,

            'MRP': mrp,

        }

        item_list.append(productlist)
        print(productlist)

        search_bar = browser.find_element_by_id('search')
    data = pd.DataFrame(item_list)
    data.to_csv("jiostore_data.csv")



def winniscrap():
    global item_name1, item_name2, name, item_name, names, item_price, price
    winni_url='https://www.winni.in/cake'
    browser = webdriver.Chrome(webdriver_path, options=options)
    browser.get(winni_url)
    for product in cakes:
        browser.get(winni_url)
        search_bar = browser.find_element_by_id('search-input-in-desktop')
        search_bar.send_keys(product)
        search_bar.send_keys(Keys.ENTER)

        try:
            item_n = browser.find_element_by_xpath('/html/body/main/div/div/div[1]/div/div[2]').click()
            window_after = browser.window_handles[1]
            browser.switch_to.window(window_after)

            quantity = browser.find_element_by_xpath(
                '/html/body/main/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div/div[1]/label[2]/span').click()

            item_name = browser.find_element_by_xpath(
                '/html/body/main/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[1]/div/h1').text.strip()
            item_price = browser.find_element_by_xpath(
                '/html/body/main/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div/span[2]').text.strip()

        except:
            item_name = '-notavailable'

        try:

            mrp = browser.find_element_by_xpath(
                '/html/body/main/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/span/span[2]').text.strip()

        except:
            mrp = ''

        name = item_name
        price = item_price

        productlist = {
            'name': name,

            'price': price,

            'MRP': mrp

        }

        item_list.append(productlist)
        print(productlist)
        browser.close()
        previous = browser.window_handles[0]
        browser.switch_to.window(previous)
        search_bar = browser.find_element_by_id('search-input-in-desktop').clear()

    data = pd.DataFrame(item_list)
    data.to_csv("winnistore_data.csv")



def manakr():
    global price2, item_name, names
    browser = webdriver.Chrome(webdriver_path, options=options)
    manakiranam_url = 'https://manakiranam.com/'
    browser.get(manakiranam_url)
    for each in grocery:
        search_bar = browser.find_element_by_class_name('s')
        search_bar.click()
        search_bar.send_keys(each)
        search_bar.send_keys(Keys.ENTER)

        try:

            item_name0 = browser.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/h1').text.strip()
            item_name1=browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/h1').text.strip()
            item_name2=browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[6]/div[1]/h3/a').text.strip()
            item_name=item_name0+item_name1+item_name2

        except:
            item_name = each
        try:
            price1 = browser.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p/span/bdi').text.strip()

        except:
            price1 = ''
        try:
            price2= browser.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p/ins/span/bdi').text.strip()

        except:
            price2 = ""
        try:
            price3=browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[6]/div[1]/span/ins/span/bdi').text.strpi()
        except:
            price3=''

        price = price1 + price2+price3
        if not  price:
            price="NA"

        price2 = ""
        try:
            mrp1 = browser.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/p/del/span/bdi').text.strip()
            mrp2=browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[6]/div[1]/span/del/span/bdi').text.strip()
            mrp=mrp1+mrp2
            rp = mrp[0][0]
            mrp = mrp.replace(rp, "")
        except:
            mrp = '-'


        pr=price[0][0]
        price=price.replace(pr,"")

        productlist = {
            'name': item_name,

            'price': price,

            'MRP':mrp

        }

        item_list.append(productlist)

        print(productlist)
        search_bar = browser.find_element_by_class_name('s').clear()

    data = pd.DataFrame(item_list)
    data.to_csv("manakiranam_data.csv")
