from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from ToJson import to_json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
urlSource = "https://www.elefant.ro/list/carti/carte?pag="
i, id = (open("index.txt", 'r').readline().split(" "))
i = int(i)
id = int(id)


def navigare(driver, i):
    global id
    while True:
        sleep(2)
        driver.get(urlSource + str(i))
        try:
            sleep(3)
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')))
            driver.find_element(By.XPATH,'//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
            sleep(3)


            driver.maximize_window()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="close"]')))
            driver.refresh()
        except:
            print("nu a aparut pop-up")
        finally:


            height = driver.execute_script("return document.body.scrollHeight")
            for o in range(0, height, 800):
                driver.execute_script(f"window.scrollTo(0, {o});")
                sleep(0.5)


            lista = driver.find_elements(By.XPATH,'//a[@class="product-title"]')

            for j in range(id, len(lista),9):
                browser = webdriver.Firefox(options=options)
                elem = lista[j]
                link = elem.get_attribute("href")
                browser.get(link)
                browser.implicitly_wait(3)
                sleep(2)
                '''mai_mult = browser.find_element_by_xpath('//div[2]/a[2]/span')
                mai_mult.click()'''
                sleep(2)
                to_json(extragere(browser, i), link)
                browser.quit()
            i += 1
            id = 0
    driver.close()


def extragere(browser, i) -> list:
    sleep(2)
    global id
    list =[]
    pret_actual = browser.find_elements(By.XPATH,'//*[@class="product-price vendor-offer-data js-vendor-price"]//*[(@class="current-price")]')
    for value in pret_actual:
        pret_actual = value.text
    list.append('Pret')
    list.append(pret_actual)
    image_link = browser.find_element(by=By.CSS_SELECTOR, value='.product-thumb-set > .product-image')
    #image_link = browser.find_element_by_css_selector('.product-thumb-set > .product-image')
    image_link = image_link.get_attribute('src')
    list.append('Imagine')
    list.append(image_link)
    #detalii = browser.find_elements(by=By.XPATH, value='//*[@class="panel-body"]')


    # detalii = browser.find_elements(by=By.XPATH, value='//dl[@class="ish-productAttributes"]//dd')
    # for k in detalii:
    #     detalii=k.text
    #     detalii = detalii.split("\n")

    #detalii = browser.find_element_by_xpath('//*[@id]/div/dl')
    #detalii = browser.find_element_by_xpath('//dl[@class="ish-productAttributes"]')
    # for j in range(0, len(detalii)):
    #     list.append(detalii[j])
    title = browser.find_element(by=By.XPATH, value='//h1')
    #title = browser.find_element_by_xpath('//h1')
    title = title.text.split(" - ", 1)[0]
    list.append("Titlu")
    list.append(title)
    print(list)
    id = id + 1
    open("index.txt", 'w').write(str(i) + ' ' + str(id))
    return list


if __name__ == "__main__":
    try:
        navigare(driver, i)
    except KeyboardInterrupt:
        pass