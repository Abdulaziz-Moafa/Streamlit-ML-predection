from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import PIL
import os
import os.path
from PIL import Image
import pandas as pd
import urllib
import time
import csv

webdriver_path = r'C:\Users\zezo0\Downloads\chromedriver_win32\chromedriver.exe'
url = 'https://www.google.com/'

item = []
with open(r"C:\Users\zezo0\Downloads\Gharwaalaa1\Gharwaalaa\GHPD11.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        item.append(row['name'])

search_item = item

options = webdriver.ChromeOptions()

options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')



for each in item:
    browser = webdriver.Chrome(webdriver_path, options=options)
    browser.get(url)

    search_bar = browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search_bar.send_keys(each)
    search_bar.send_keys(Keys.ENTER)
    browser.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

    browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').screenshot('C:/Users/jeevanasree/PycharmProject/gharwaalaa/products/p(' + str(each) + ').png')
    browser.close()

# for resizing the images
"""f = r'products'
   for file in os.listdir(f):
        f_img = f + "/" + file
        img = Image.open(f_img)
        img = img.resize((600, 450))
        img.save(f_img)"""



