#-------------------------------------------------------------------------------
# Name:        LinkedInSearch
# Purpose:
#
# Author:      Barry Hammer
#
# Created:     27/07/2020
# Copyright:   (c) Barry Hammer 2020
#-------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import ctypes
import PySimpleGUI as sg

###########################
# Enter search criteria
###########################

sg.ChangeLookAndFeel('Tan')
layout = [
                 [sg.Text("Please enter qualifications (such as 'Developer') in the first row", font = 'Helvetica')],
                 [sg.Text("and location (such as 'Tel Aviv') in the second row.", font = 'Helvetica')],
                 [sg.Text('Qualifications: ', font = 'Helvetica', size=(15, 1)), sg.InputText()],
                 [sg.Text('Location: ', font = 'Helvetica', size=(15, 1)), sg.InputText()],
                 [sg.Button('Submit Data')]
        ]

window = sg.Window('Enter search criteria', layout)

event, values = window.read()
window.close()

qualifications = values[0]
my_location = values[1]
search_title = qualifications + " jobs in " + my_location
my_list = []

###########################
# Start script headless
###########################
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:/Users/Family Hammer/Downloads/chromedriver.exe")

driver.get("https://www.linkedin.com/jobs/")

assert "LinkedIn" in driver.title

search_box = driver.find_element_by_xpath("//*[@id='JOBS']/section[1]/input")
location = "//*[@id='JOBS']/section[2]/input"

search_box.send_keys(qualifications)
driver.find_element(By.XPATH, location).clear()
loc_enter = driver.find_element(By.XPATH, location).send_keys(my_location + Keys.ENTER)

###########################
# Verify elememts located
###########################
try:
    # wait 5 seconds before looking for element
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/header/section/form/ul/li[1]/div/button"))
    )
except:
    # else quit
    print("Could not find element")
    driver.quit()

time_button = driver.find_element_by_xpath("/html/body/header/section/form/ul/li[2]/div/button").click()
last_week = driver.find_element_by_xpath("//*[contains(text(), 'Past Week')]").click()
filter_btn = driver.find_element_by_xpath("//*[@id='TIME_POSTED-dropdown']/fieldset/div[2]/button").click()

###########################
# Check sort
###########################

try:
    # wait 5 seconds before looking for element
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"il.linkedin.com/jobs/view")]'))
    )
    elems = driver.find_elements_by_xpath('//a[contains(@href,"il.linkedin.com/jobs/view")]')
    for elem in elems:
        my_list.append(elem.get_attribute("text"))

    ctypes.windll.user32.MessageBoxW(0, "You have the following values: {}.".format(my_list), "Result message box", 1)
except:
    # else quit
    ctypes.windll.user32.MessageBoxW(0, "No matches found for {} in {}.".format(qualifications, my_location), "Result message box", 1)

###########################
# Quit session
###########################
driver.quit()
