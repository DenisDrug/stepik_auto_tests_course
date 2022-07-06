from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options as chrome_options




link = "http://suninjuly.github.io/simple_form_find_task.html"

def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=2560,1600')
    return options


options = get_chrome_options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path='../curses/tests/chromedriver.exe', options=options)
driver.get(link)

get_text1 = driver.find_element(By.XPATH, "//input[@name='first_name']")
print(get_text1)
get_text1.send_keys('Ivan')
get_text2 = driver.find_element(By.XPATH, "//input[@name='last_name']")
print(get_text2)
get_text2.send_keys('Petrov')
get_text3 = driver.find_element(By.XPATH, "//input[@class='form-control city']")
print(get_text3)
get_text3.send_keys('Smolensk')
get_text4 = driver.find_element(By.XPATH, "//input[@id='country']")
print(get_text4)
get_text4.send_keys('Russia')
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
# успеваем скопировать код за 30 секунд
time.sleep(10)
# закрываем браузер после всех манипуляций
driver.quit()

# не забываем оставить пустую строку в конце файла