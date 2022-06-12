from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://opac.biblioteca.ase.ro/opac/bibliographic_view/4")
urlSursa="http://opac.biblioteca.ase.ro/opac/bibliographic_view/"
i=int(open("../i.txt", 'r').read())
j = ((i//100000)+1)*100000
urlStr=""
try:
    while i<j:
        driver.get(urlSursa+str(i))
        if driver.current_url[-10:] !="status=404":
            urlStr += str(i)+"\n"
        i +=1
except KeyboardInterrupt:
    pass
driver.close()
file = open("urlValid.txt", "a")
open("../i.txt", 'w').write(str(i))
file.write(urlStr)
file.close()