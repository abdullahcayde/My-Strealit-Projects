import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

print('---------------------- Part 2 Real Time Consumption ML----------------------')
def sleep(x):
    time.sleep(x)
def wait(x):
    driver.implicitly_wait(x)

start_date = '01.06.2022'
end_date = '05.06.2022'


#  1 - Create Driver
Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

#  2 - Go to Website
driver.get('https://seffaflik.epias.com.tr/transparency/tuketim/gerceklesen-tuketim/uecm.xhtml')
wait(10)
sleep(2)

#  3 - ActionChain Object created
# 3.1 - Click Banned Accept
actions = ActionChains(driver)
start_date_buton = driver.find_element(By.ID, 'j_idt231:date1_input')
actions.click(start_date_buton).perform()
actions.key_down(Keys.BACK_SPACE).perform()
actions.send_keys(start_date).perform()
wait(10)

end_date_buton = driver.find_element(By.ID, 'j_idt231:date2_input')
actions.click(end_date_buton).perform()
actions.key_down(Keys.BACK_SPACE).perform()
actions.send_keys(end_date).perform()
wait(10)


execute_button = driver.find_element(By.ID, 'j_idt231:goster')
actions.click(execute_button).perform()
wait(10)
sleep(0.5)

csv_clic

sleep(120)
print('Code Run without Problem :)')
driver.quit()