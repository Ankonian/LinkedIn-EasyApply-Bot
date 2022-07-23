from email.contentmanager import raw_data_manager
import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing.connection import wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
login_email = 'langli1307@gmail.com'
login_pw = 'G0dD@mneD'
keywords = ['sdet', 'software engineer', 'IT', 'QA engineer']
locations = ['los angeles', 'pasadena', 'mountain view', 'california']
easy_apply = '?f_AL=true&'

#---------------------Login--------------------------------
driver.get('https://www.linkedin.com')
login_button = driver.find_element_by_link_text('Sign in')
time.sleep(2)
login_button.click()
login_username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
pw_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
login_username.send_keys(login_email)
time.sleep(1)
pw_input.send_keys(login_pw)
time.sleep(1)
pw_input.send_keys(Keys.RETURN)
#----------------------------------------------------------
driver.get('https://www.linkedin.com/jobs/search/' + easy_apply + 'keywords=' + keywords[0] + '&location=' + locations[0]) 

time.sleep(5)
rawLinks = driver.find_elements_by_tag_name('a')

productLinks = []
filteredLink = []

#Narrowing down the links we want
for rawLink in rawLinks:
    productLinks.append(rawLink.get_attribute('href'))

#Gathering links for all products in current page
sub = "https://www.linkedin.com/jobs/view/"
for s in productLinks:
    if(s != None):
            if(sub in s):
                if(s not in filteredLink):
                    filteredLink.append(s)
for link in filteredLink:
    print(link)
