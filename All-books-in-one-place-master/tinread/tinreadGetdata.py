from random import random
from time import sleep

from tinread.getDataBook import getDataBook
from tinread.toJson import to_json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def tinread_get_data(urlSursa: str, id: str, id_photo: str):
    file_name = f"All-books-in-one-place-master/data/tinread/{id}.txt"
    list_fields = ['LDR', '000', '001', '003', '005', '006', '007', '008', '009', '020', '031', '035', '036', '041',
                   '044', '050', '075', '076', '080', '082', '100', '110', '113', '116', '136', '138', '140', '152',
                   '154', '166', '168', '169', '175', '184', '189', '197', '204', '206', '216', '218', '223', '224',
                   '227', '229', '230', '232', '240', '244', '245', '250', '260', '269', '271', '273', '274', '276',
                   '281', '292', '294', '300', '304', '312', '318', '321', '336', '341', '344', '355', '356', '359',
                   '362', '366', '374', '382', '406', '408', '414', '428', '430', '448', '464', '483', '490', '500',
                   '504', '507', '511', '518', '546', '571', '587', '603', '608', '624', '650', '651', '658', '687',
                   '696', '700', '800', '802', '804', '807', '811', '852', '855', '857', '891', '911', '913']

    f = open(file_name, "r")
    index = int(f.readline())
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    try:
        while True:
            driver.get(urlSursa + str(index))
            if driver.current_url[-10:] != "status=404":
                sleep(random() * 5)
                mylist = []
                list = getDataBook(urlSursa + str(index), index, id_photo, id)
                a = list.split(' ')
                i = 1

                mylist.append(a[0])
                while i < (len(a)):

                    value = ""
                    while i < len(a):
                        if not a[i] in list_fields:
                            value += a[i]
                            i += 1
                        else:
                            break
                    mylist.append(value)
                    if (i < len(a)):
                        mylist.append(a[i])
                    i += 1
                if not to_json(mylist, id):
                    print("error")
            index += 1
            open(file_name, "w").write(str(index))

    except KeyboardInterrupt:
        pass
    finally:
        driver.close()
        pass
        # jsonFileTinread =open("../data/tinread.json", "a+")
        # jsonFileTinread.write(list)
        # jsonFileTinread.close()
