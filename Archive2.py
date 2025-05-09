#!/usr/bin python
# -*- coding: utf-8 -*-

#srieck 4.11.2025

#mods & libs
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 
import re
import main

############### xpath values ###############

pool_xpath = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/db-search/div/mat-form-field[2]/div/div[1]/div[4]/button"
win_pool = "/html/body/div[6]/div[2]/div/div/div/mat-option[2]/span"
app_one = "//*[@id='mat-input-0']"
button_ui = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/db-search/div/div/button"
find_application = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[1]/db-applications/div/div/div/div[1]/lls-table/p-treetable/div/div[1]/div/p-scroller/div/table/tbody/tr/td[1]"
archive_message = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[3]/db-details/div/div[2]/lls-card[2]/mat-card/mat-card-content/div/db-detail-validation/div[4]/div/button[1]/span[1]"
archive_button = "/html/body/div[6]/div[2]/div/mat-dialog-container/lorenz-confirm-default-dialog/div[2]/button[1]"
validate = "/html/body/div[3]/p-contextmenusub/ul/li[2]"
rules = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[3]/db-details/div/div[2]/lls-card[2]/mat-card/mat-card-content/div/db-detail-validation/div[3]/lls-table/p-treetable/div/div[1]/div/p-scroller/div/table/tbody"
rclickValidate = "/html/body/div[3]/p-contextmenusub/ul/li[2]/a"
validation_date = '/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[3]/db-details/div/div[2]/lls-card[2]/mat-card/mat-card-content/div/db-detail-validation/div[1]/lorenz-data-fields/lorenz-labels-list[1]/div/div[2]/div/div'
rules = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[3]/db-details/div/div[2]/lls-card[2]/mat-card/mat-card-content/div/db-detail-validation/div[3]/lls-table/p-treetable/div/div[1]/div/p-scroller/div/table/tbody"
tester = '/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[3]/db-details/div/div[2]/lls-card[2]/mat-card/mat-card-content/div/db-detail-validation/div[1]/lorenz-data-fields/lorenz-labels-list[2]/div/div[2]/div/div'
sequencefunc = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/lls-toolbar/div/div/div/lorenz-menu/button[3]"
archiveseq = "/html/body/div[6]/div[2]/div/div/div/button[5]"

check_app_status = r"p-ripple p-element p-menuitem-link p-disabled ng-star-inserted"
skip_error = r"p-element far fa-check-circle lls-ok-default-text ng-star-inserted"

############### functions ###############


def click_thing(driver, click_that):
    try:
        found_thing = driver.find_element(By.XPATH, value=click_that)
        found_text = driver.find_element(By.XPATH, value=click_that).text
        print(found_text)
    except Exception as e: 
        print(e)
        pass
    else:
        found_thing.click()
    

def send_thing(driver, find_this, send_this):
    found_thing = driver.find_element(By.XPATH, value=find_this)
    found_thing.send_keys(send_this)


def right_click(driver, click_that):
    try:
        element = driver.find_element(By.XPATH, value=click_that)
        # found_text = driver.find_element(By.XPATH, value=click_that).text
        # # print(found_text)
    except Exception as e: 
        print(e)
        pass
    else:        
        ActionChains(driver).context_click(element).perform()


def contains_regex(text, pattern):
    """
    Checks if a string contains a regular expression pattern.

    Args:
        text: The string to search within.
        pattern: The regular expression pattern to search for.

    Returns:
        True if the string contains the pattern, False otherwise.
    """
    match = re.search(pattern, text)
    return bool(match)



def check_regex(driver, r_value, pattern):
    element = driver.find_element(By.XPATH, value=r_value)
    text = element.get_attribute('class')
    print(text)
    print(pattern)
    contains = contains_regex(text, pattern)
    print(contains)
    return contains
        


def grab_thing(driver, grab_that):
    try:
        found_thing = driver.find_element(By.XPATH, value=grab_that).text
    except Exception as e: 
        print(e)
        pass
    else:
        return found_thing


def get_sequence(driver, sequence_num):
    one_sequence = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[2]/db-sequences/div/div/div[1]/div[1]/db-sequences-table/div/lls-table/p-treetable/div/div[1]/div/p-scroller/div/table/tbody/tr/td[2]"
    found_text = driver.find_element(By.XPATH, value=one_sequence).text
    # print("This is the text it found and the sequence number {} & {}".format(found_text, sequence_num))
    if str(found_text) == str(sequence_num):
        print("Use first xpath")
        return one_sequence
    elif str(found_text) != str(sequence_num):
        for i in range(1, 100):
            alt_sequence = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[2]/db-sequences/div/div/div[1]/div[1]/db-sequences-table/div/lls-table/p-treetable/div/div[1]/div/p-scroller/div/table/tbody/tr[{}]/td[2]".format(i)
            found_text = driver.find_element(By.XPATH, value=alt_sequence).text
            print(sequence_num, found_text)
            if str(found_text) == str(sequence_num):
                print("Use second xpath")
                return alt_sequence


        
############### test starts ###############
   #56, 65      


def test_app():
    df = main.df
    for i in range(main.i_start, main.i_end): ### index number will be printed if loop breaks, change the first index number and the code will start where it broke 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--log-level=2") # this was added to address a weird tensor flow error that stopped testing
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
    # launch the Submission repository
        driver.get("https://docubridge-cder.test.fda.gov/auth/signin?ReturnUrl=https%3A%2F%2Fdocubridge-cder.test.fda.gov%2Fdocubridge%2Fsubmission-repository")
        print('Step 1: Launch Submission Repository')
    # maximize the window
        driver.maximize_window()
        print('Maximize the window')
    # login
        username = driver.find_element(By.XPATH, value="//*[@id='UserName']") 
        password = driver.find_element(By.XPATH, value="//*[@id='Password']")
        username.send_keys("")
        password.send_keys("")
        driver.find_element(By.XPATH, value="//*[@id='SubmitButton']").click()
        print('Login success!')
    # # wait 5 sec for find button
        driver.implicitly_wait(20000)
        print("find app")
        app_num = df['Application'].iloc[i]
        sequence_num = df['Sequence'].iloc[i]
        print("DataFrame index number {} of {}".format(i, main.i_end))
        print("Testing Application {} Sequence {}".format(app_num, sequence_num))
    # select win_pool
        print("Winpool found")
        click_thing(driver, pool_xpath)
        click_thing(driver, win_pool)
    #find & select application 
        send_thing(driver, app_one, app_num)
        driver.implicitly_wait(20000)
        click_thing(driver, button_ui)
        driver.implicitly_wait(20000)
        click_thing(driver, find_application)
    # find sequence
        print("Click sequence")
        click_that = get_sequence(driver, sequence_num)
        click_thing(driver, click_that)
        driver.implicitly_wait(20000)
#    right click and open folder
        click_that = get_sequence(driver, sequence_num)
        right_click(driver, click_that)
        print("Right clicked")
        driver.implicitly_wait(40000)
    #check element is not disabled 
        print("Checking value validate")
        driver.implicitly_wait(40000)
        app_status = check_regex(driver, rclickValidate, check_app_status)
        if app_status is True:
    # archive validation
            click_thing(driver, sequencefunc)
            driver.implicitly_wait(2)
            click_thing(driver, archiveseq)
            # click_thing(driver, archive_message)
            click_thing(driver, archive_button)
            driver.implicitly_wait(2)
    #right click again 
            click_that = get_sequence(driver, sequence_num)
            right_click(driver, click_that)
            driver.implicitly_wait(1)
            print("App Archived")
            driver.quit()
        else: 
            print("Skipped")
            driver.quit()
            






if __name__ == '__main__':
    test_app()
    print("Test Complete!")
