from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from ToJson import to_json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)
urlSource = "https://www.elefant.ro/list/carti/carte?pag="
i, id = (open("index.txt", 'r').readline().split(" "))
i = int(i)
id = int(id)


def navigare(driver, i):
    global id
    while True:
        driver.get(urlSource + str(i))
        driver.maximize_window()
        height = driver.execute_script("return document.body.scrollHeight")
        for o in range(0, height, 800):
            driver.execute_script(f"window.scrollTo(0, {o});")
            sleep(0.5)
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="seg-cat-rec-4"]/h2'))
    )
        sleep(3)
        lista = driver.find_elements_by_xpath(
            '//div[@class="product-list-item col-lg-3 col-md-4 col-sm-4 col-xs-6 grid-view lazy"]')
        for j in range(id, len(lista)):
            line = lista[j]
            browser = webdriver.Firefox(options=options)

            elem = line.find_element_by_tag_name("a")
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
    global id
    list =[]
    pret_actual = browser.find_element_by_css_selector(".pdp-table-th > .current-price")
    pret_actual = pret_actual.text
    list.append('Pret')
    list.append(pret_actual)
    image_link = browser.find_element_by_css_selector('.product-thumb-set > .product-image')
    image_link = image_link.get_attribute('src')
    list.append('Imagine')
    list.append(image_link)
    detalii = browser.find_element_by_xpath('//*[@id]/div/dl')
    # detalii = browser.find_element_by_xpath('//dl[@class="ish-productAttributes"]')
    detalii = detalii.text
    detalii = detalii.split("\n")
    for j in range(0, len(detalii)):
        list.append(detalii[j])
    title = browser.find_element_by_xpath('//h1')
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