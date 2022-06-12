import re
import time
from random import random

from PIL import Image
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tinread.IsRealCover import is_real_cover

dateTinread = {
    "lDR": "",
    "000": "",
    "001": "",
    "003": "",
    "005": "",
    "006": "",
    "007": "",
    "008": "",
    "009": "",
    "020": "",
    "031": "",
    "035": "",
    "036": "",
    "041": "",
    "044": "",
    "050": "",
    "075": "",
    "076": "",
    "080": "",
    "082": "",
    "100": "",
    "110": "",
    "113": "",
    "116": "",
    "136": "",
    "138": "",
    "140": "",
    "152": "",
    "154": "",
    "166": "",
    "168": "",
    "169": "",
    "175": "",
    "184": "",
    "189": "",
    "197": "",
    "204": "",
    "206": "",
    "216": "",
    "218": "",
    "223": "",
    "224": "",
    "227": "",
    "229": "",
    "230": "",
    "232": "",
    "240": "",
    "244": "",
    "245": "",
    "250": "",
    "260": "",
    "269": "",
    "271": "",
    "273": "",
    "274": "",
    "276": "",
    "281": "",
    "292": "",
    "294": "",
    "300": "",
    "304": "",
    "312": "",
    "318": "",
    "321": "",
    "336": "",
    "341": "",
    "344": "",
    "355": "",
    "356": "",
    "359": "",
    "362": "",
    "366": "",
    "374": "",
    "382": "",
    "406": "",
    "408": "",
    "414": "",
    "428": "",
    "430": "",
    "448": "",
    "464": "",
    "483": "",
    "490": "",
    "500": "",
    "504": "",
    "507": "",
    "511": "",
    "518": "",
    "546": "",
    "571": "",
    "587": "",
    "603": "",
    "608": "",
    "624": "",
    "650": "",
    "651": "",
    "658": "",
    "687": "",
    "696": "",
    "700": "",
    "800": "",
    "802": "",
    "804": "",
    "807": "",
    "811": "",
    "852": "",
    "855": "",
    "857": "",
    "891": "",
    "911": "",
    "913": ""
}


def getDataBook(url: str,id:int,id_photo:str,id_sit:str) -> str:
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    data = ""
    try:
        driver.get(url)
        time.sleep(random()*10)

        driver.find_element_by_xpath(f"//img[@id='Any_{id_photo}']").screenshot('a.png')
        img =Image.open("a.png")
        if is_real_cover(img):
            img.save(f"img/{id_sit}_{id}.png")
        data = driver.find_element_by_xpath("//li[contains(., 'LDR')]").get_attribute('innerHTML')
        regularExpression = r'(<script(\s|\S)*?<\/script>)|(<style(\s|\S)*?<\/style>)|(<!--(\s|\S)*?-->)|(<\/?(\s|\S)*?>)'
        data = re.sub(regularExpression, ' ', data)
        data = re.sub(r"[ +]+", ' ', data)
        data = re.sub(r"\n", '', data)
        data = re.sub(r" +",' ', data)
        data=data[1:]
    except KeyboardInterrupt:
        pass
    finally:
        driver.quit()
        return data
