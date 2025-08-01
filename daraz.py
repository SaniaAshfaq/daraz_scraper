from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


driver_url = "C:\\Users\\User\\Downloads\\chromedriver-win32\\chromedriver.exe"
service = Service(driver_url)
driver = webdriver.Chrome(service= service)

driver.get("https://www.daraz.pk/#?")
href = []
price = []
title = []
elements = driver.find_elements(By.XPATH , '//div[@class="card-jfy-wrapper"] //a[@class="pc-custom-link jfy-item hp-mod-card-hover"]')

for count in range(1, 5):
    for ele in elements:
        img = ele.find_element(By.XPATH , './/div[@class="picture-wrapper common-img jfy-item-image img-w100p"]//img')
        img_href = img.get_attribute("src")
        mytitle = ele.find_element(By.XPATH, './/div[@class="card-jfy-item-desc"]//div[@class="card-jfy-title two-line-clamp"]').text
        myprice = ele.find_element(By.XPATH , './/div[@class="card-jfy-item-desc"]//span[@class="price"]').text
        price.append(myprice)
        title.append(mytitle)
        href.append(img_href)
        
    load_more = driver.find_element(By.XPATH , ' //div[@class="load-more-button"]')

    load_more.click()



combined = list(zip(title, href , price))
df = pd.DataFrame(combined, columns=["title","href", "price"])
df.to_csv("daraz.csv", index= False)

driver.quit()