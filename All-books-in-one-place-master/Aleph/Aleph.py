from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from ToJson import to_json
from random import random


def getdataaleph(cataloglink: str, idcatalog: int):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    i = int(open(f'../data/Aleph/{idcatalog}.txt').readline())
    id = 1
    while True:
        driver.get(cataloglink)
        driver.find_element_by_xpath("//input[@name='ccl_term']").send_keys("SYS=" + str(i))
        driver.find_element_by_xpath("//input[@type='image']").click()
        try:
            driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[4]/td[1]/img")  # eroare

            sleep(random() * 10)
        except:
            list = []
            sleep(2)
            driver.find_element_by_xpath("//td[@width ='30%']/a").click()  # carte
            sleep(2)
            driver.find_element_by_xpath("/html/body/table[3]/tbody/tr/td[5]/a").click()  # etichete
            sleep(2)
            data = driver.find_element_by_xpath("//html//body//table[5]")  # elemnte Etichete MARC
            for line in data.find_elements_by_xpath('//tbody//tr//td'):
                list.append(line.text)
            k = 0
            for k in range(len(list)):
                if list[k] == "FMT":
                    break
            list = list[k:]
            k = 0
            for k in range(len(list)):
                if list[k] == "SYS":
                    break
            list = list[:k + 2]
            to_json(list, "1", idcatalog)
            id = id + 1
            open("../data/Aleph/2.txt", "w").write(str(i))

        finally:
            i = i + 1
