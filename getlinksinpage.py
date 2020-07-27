from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ctypes

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:/Users/Family Hammer/Downloads/chromedriver.exe")

driver.get("http://www.python.org")

assert "Python" in driver.title

news = driver.find_element_by_xpath('//*[@title="More News"]')

news.click()

assert "Insider" in driver.title

my_list = []

elems = driver.find_elements_by_xpath('//a[contains(@href,"blog.python.org/2020/07")]')
for elem in elems:
    #print(elem.get_attribute("href")
    my_list.append(elem.get_attribute("text"))

ctypes.windll.user32.MessageBoxW(0, "You have the following values: {}.".format(my_list), "My message box", 1)

driver.quit()
