import re
import time
from random import random

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from tinread.IsRealCover import is_real_cover


def getDataBook(url: str,id:int,id_photo:str,id_sit:str) -> str:
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    data = ""
    try:
        driver.get(url)
        time.sleep(random()*10)

        driver.find_element(By.XPATH, f"//img[@id='Any_{id_photo}']").screenshot('a.png')
        img =Image.open("a.png")
        if is_real_cover(img):
            img.save(f"img/{id_sit}_{id}.png")
        data = driver.find_element(By.XPATH, "//li[contains(., 'LDR')]").get_attribute('innerHTML')
        regularExpression = r'(<script(\s|\S)*?<\/script>)|(<style(\s|\S)*?<\/style>)|(<!--(\s|\S)*?-->)|(<\/?(\s|\S)*?>)'
        data = re.sub(regularExpression, ' ', data) #eleimin toate tagurile html
        data = re.sub(r"[ +]+", ' ', data) #elim toate spatiile suplimentare
        data = re.sub(r"\n", '', data) # elimin toate new line-urile
        data = re.sub(r" +",' ', data) #ne asiguram ca nu a ramas nimic nedorit din codul html
        data=data[1:]   #luam toate literele din data
    except KeyboardInterrupt:
        pass
    finally:
        driver.quit()
        return data
