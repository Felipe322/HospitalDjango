from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


options = Options()
extset = ['enable-automation', 'ignore-certificate-errors']
options.add_argument("--window-size=600,600")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", extset)


driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('http://192.168.33.20:8000/login')
driver.find_element_by_name('username').send_keys('alex@asdas.mx')
driver.find_element_by_name('password').send_keys('alex123' + Keys.ENTER)
time.sleep(0.5)


driver.find_element_by_xpath('/html/body/div[1]/nav/ul[1]/li[1]/a').click()
time.sleep(0.5)

driver.find_element_by_xpath('/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/ul/li[2]/a').click()

driver.find_element_by_name('nombre').send_keys('Juan')
driver.find_element_by_name('primerApellido').send_keys('Pérez')
driver.find_element_by_name('segundoApellido').send_keys('López')

driver.find_element_by_name('numero_ss').send_keys('4651646416516')
driver.find_element_by_name('fecha_nac').send_keys('1970-10-01')
driver.find_element_by_name('tipo_sangre').send_keys('A positivo')
driver.find_element_by_name('estado').send_keys('Zacatecas')
driver.find_element_by_name('municipio').send_keys('Calera')

driver.find_element_by_tag_name('html').send_keys(Keys.END)
time.sleep(0.5)

driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div[1]/div[2]/div/form/div[2]/input').click()


# tbody = driver.find_element_by_tag_name('tbody')
# trs = [tr.text for tr in tbody.find_elements_by_tag_name('tr')]



# print (str(trs))
