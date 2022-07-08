from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from helper.clickHelper import waitUntilItVisibal
import time
import json
import os
import copy

from selenium.webdriver.support.wait import WebDriverWait


def to_json(data: list):
    """
    functie pentru introducerea informatiilor in fisierul json
    :param data: lista cu nume, pret, isbn, etc
    """

    for i in range(3, len(data)):  # in cazul in care apar caractere cum ar fi tab, new line ele sunt elimintae
        for j in ["\t", "\n", "\u00a0", '"']:
            data[i] = data[i].replace(j, '')
    carte = data[0][data[0].find(':') + 2:]
    dict = {carte: []}
    fild = \
        {
            "fld":
                {
                    "fld_name": "",
                    "val": ""
                },
        }

    for index, i in enumerate(data):
        dict[carte].append(copy.deepcopy(fild))
        dict[carte][index]["fld"]["fld_name"] = i[:i.find(':')]
        dict[carte][index]["fld"]["val"] = i[i.find(':') + 2:]

    with open("../data/libris.json", 'r+', encoding="utf-8") as file:
        data = file.read().strip()
        json_file = json.loads(data or '{}')
        json_file.update(dict)
        file.seek(0)
        json.dump(json_file, file)
        file.truncate()


def libris():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox()  # options=options)
    driver.get("https://www.libris.ro/")
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
        (By.XPATH, '//a[@class="close modal-close-c modal-close-x-c modal-close-x-c-newsletter"]')))
    driver.find_element(By.XPATH,
                        '//a[@class="close modal-close-c modal-close-x-c modal-close-x-c-newsletter"]').click()
    # waitUntilItVisibal(By.XPATH,).click()
    # if driver.find_element(By.CLASS_NAME, "close modal-close-c modal-close-x-c modal-close-x-c-newsletter"):
    # daca apare popup-ul cu abonari se incearca inchiderea lui
    # driver.find_element(By.CLASS_NAME, "close modal-close-c modal-close-x-c modal-close-x-c-newsletter").click()

    # if driver.find_element(By.XPATH, '//a[@class="back-to-site-link"]'):
    #     driver.get(driver.find_element(By.XPATH, '//a[@class="back-to-site-link"]').get_attribute("href"))

    if driver.find_element(By.XPATH, '//button[@class ="btn btn-primary btn-sm acceptcookiesLibris"]'):
        time.sleep(10)
        driver.find_element(By.XPATH, '//button[@class ="btn btn-primary btn-sm acceptcookiesLibris"]').click()
        waitUntilItVisibal(By.XPATH, '//button[@class ="btn btn-primary btn-sm acceptcookiesLibris"]')
        driver.find_element(By.XPATH, '//button[@class ="btn btn-primary btn-sm acceptcookiesLibris"]').click()
    # numarul categoriilor
    k = driver.find_element(By.XPATH, '//li[@class="subcateg-dwn"]')
    ActionChains(driver).move_to_element(k).click(k).perform()
    x = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//ul[@class="col-3 nav nav-tabs tabs-left"]')))

    x = x.find_elements(By.XPATH, ".//a")
    categorii = []

    for element in x:
        ActionChains(driver).move_to_element(element).click(element).perform()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="subcateg-list-wr"]')))
        # y = driver.find_element(By.XPATH,   # numarul de coloane din fiecare categorie
        #   '//div[@class="tab-pane tab-pane-header tab-subcategorie"][' + str(i) + ']/div/div[@class="col-md-3"]')
        y = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="subcateg-list-wr"]')))
        y = y.find_elements(By.XPATH, ".//*")
        time.sleep(5)
        for j in range(1, len(y) + 1):
            z = driver.find_element(By.XPATH,  # numarul subcategoriilor
                                    '//div[@class="tab-pane tab-pane-header tab-subcategorie"][' + element + ']/div/div[@class="col-md-3"][' + str(
                                        j) + ']/ul/li[@class="menuTitleSubCateg"]')
            time.sleep(5)

            for k in range(1, len(z) + 1):  # preluam link-ul fiecarei subcategorii si o inseram in lista categorii
                xpath_val = driver.find_element(By.XPATH,
                                                '//div[@class="tab-pane tab-pane-header tab-subcategorie"[' + element + ']/div/div[@class="col-md-3"][' + str(
                                                    j) + ']/ul/li[@class="menuTitleSubCateg"][' + str(
                                                    k) + ']/a')
                val = xpath_val.get_attribute("href")
                categorii.append(val)
            time.sleep(5)

    for i in range(0, len(categorii)):
        driver.get(categorii[i] + '?pgn=100')  # accesam fiecare subcategorie
        # '?pgn=100'  -  se vor afisa 100 de carti in pagina
        j = 1
        while len(driver.find_elements(By.XPATH,
                                       '//div[@class="col-md-7 text-right paginatie-top"]/ul/li[last()]/a//i[@class="fa fa-angle-right"]')) == 1:
            # cat timp gasim in pagina curenta un link catre pagina urmatoare
            # preluam date despre carti
            driver.get(categorii[i] + '?pgn=100&pg=' + str(j))

            carti = []

            for k in range(len(driver.find_elements(By.XPATH,
                                                    '//div[@class="container-produs-singur border-box-ct-sg border-box-categ"]/a[@class="linkNumeProd"]'))):
                # preluam linkul de la fiecare carte din pagina
                xpath = driver.find_element(By.XPATH,
                                            '//div[@class="container-produs-singur border-box-ct-sg border-box-categ"][' + str(
                                                k + 1) + ']/a[@class="linkNumeProd"]')
                carti.append(xpath.get_attribute("href"))
            j += 1

            # deschidem un tab nou in care vom accesa linkul de la fiecare carte is vom prelua informatii in legatura
            # cu titlu, pret, etc
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])

            for k in carti:
                driver.get(k)
                carte = []
                titlu = driver.find_element(By.XPATH, '//h1[@id="product_title rating"]').get_attribute('textContent')
                for replace in '/":?|<>\\': titlu = titlu.replace(replace, "")
                carte.append('Titlu: ' + titlu)  # adaugam in lista numele cartii
                carte.append('Sursa: ' + k)  # adaugam in lista linkul de la fiecare carte

                if not os.path.isfile("../data/libris coperta/" + str(carte[0]) + ".png"):
                    img = driver.find_element(By.XPATH, '//img[@class="imgProdus"]')  # se preia coperta fiecarei carti
                    driver.execute_script("arguments[0].scrollIntoView();", img)
                    img.screenshot("../data/libris coperta/" + str(carte[0]) + ".png")
                carte.append("Coperta: ./data/libris coperta/" + str(carte[0]) + ".png")

                pret = driver.find_element(By.XPATH, '//div[@id="text_container"]/p[1]').get_attribute('textContent')
                if pret.count('Lei') == 1:
                    carte.append('Pret: ' + pret)
                    carte.append('Pret redus: -')
                else:
                    carte.append("Pret: " + pret[pret.find("Lei", 2) + 3:])
                    carte.append("Pret redus: " + pret[:pret.find("Lei", 2) + 3])

                carte.append('Stoc: ' + driver.find_element(By.XPATH, '//div[@id="text_container"]/p[3]').get_attribute(
                    'textContent'))
                for l in range(4, len(driver.find_elements(By.XPATH, '//div[@id="text_container"]/p')) + 1):
                    # adaugam in lista celelate informatii cum ar fi ISBN, descriere ator
                    informatie = driver.find_element(By.XPATH,
                                                     '//div[@id="text_container"]/p[' + str(l) + ']').get_attribute(
                        'textContent')
                    carte.append(informatie)

                to_json(carte)  # adaugam continutul listei in fisierul json
            # dupa ce am preluat informatiile de la toate cartile inchidem tab-ul
            # si continuam cu urmatoarea pagina

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    driver.close()
