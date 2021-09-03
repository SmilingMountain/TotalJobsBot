from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import re

# Initiate the browser
# create nstance of webdriver
path='/usr/local/bin/chromedriver'
driver = webdriver.Chrome(path)
url='https://www.totaljobs.com/account/signin?ReturnUrl=/'
driver.get(url)
loginemail= input('What is your Totaljobs email?')
passw=input('What is your Totaljobs password?')
time.sleep(2)
driver.find_element_by_id('ccmgt_explicit_accept').click()
driver.find_element_by_name('Form.Email').send_keys(loginemail)
driver.find_element_by_id('Form_Password').send_keys(passw)
driver.find_element_by_id('btnLogin').click()

def collectLynx():
    for a in driver.find_elements_by_xpath('.//a'):
        links.append(a.get_attribute('href'))
    for val in links:
        if val != None:
            href.append(val)
def nxtPag():
    page_number = 1
    while True:
        try:
            link = driver.find_element_by_link_text(str(page_number))
        except NoSuchElementException:
            break
        link.click()
        collectLynx()
        time.sleep(5)
        print(driver.current_url)
        page_number += 1

role = input("Enter the role you'd like to search for?")
where = input("Enter postcode/location?")
range = input("Range? Choose from:0,5,10,20 & 30?")

select = Select(driver.find_element_by_id('LocationType'))

if role != None and where != None and range != None:
    driver.find_element_by_id('keywords').send_keys(role)
    driver.find_element_by_id('location').send_keys(where)
    select.select_by_value(range)


driver.find_element_by_id('search-button').click()

href=[]
links=[]
uniq=[]
time.sleep(5)

nxtPag()

for i in range(0,len(href)):
    uniq.append(re.findall("\d+", href[i]))
id=[]
for val in uniq:
    if val != []:
        id.append(val)
id1=[]
for i in range(0,len(id)):
    if len(id[i][0])==8:
        id1.append(id[i][0])
lyn=[]
print(len(lyn))
for i in id1:
    lyn.append('https://www.totaljobs.com/job/' + i + '/apply/oneclick?TemplateType=Standard')

lyn1=list(set(lyn))
for i in lyn1:
    #quite primitive but does the ones which one click apply\! (what i was after)
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    driver.get(i)
    time.sleep(5)
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    print('sent')
else:
    print('Fail')
