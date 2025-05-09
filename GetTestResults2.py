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
from datetime import date
from selenium.common.exceptions import NoSuchElementException
import main
from selenium.webdriver.common.by import By

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
tester = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[3]/db-details/div/div[2]/lls-card[2]/mat-card/mat-card-content/div/db-detail-validation/div[1]/lorenz-data-fields/lorenz-labels-list[2]/div/div[2]/div"
validation_ok ="/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[3]/db-details/div/div[2]/lls-card[2]/mat-card/mat-card-content/div/db-detail-validation/div[2]"

check_app_status = r"p-ripple p-element p-menuitem-link p-disabled ng-star-inserted"
# skip_error = r"Open Report in Browser  Archive  Delete"

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
        found_text = driver.find_element(By.XPATH, value=click_that).text
        print(found_text)
    except Exception as e: 
        pass
        print(e)
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
    contains = contains_regex(text, pattern)
    print(contains)
    return contains
        
def skip_error(driver, validation_ok):
    text = driver.find_element(By.XPATH, value=validation_ok).get_attribute("textContent")
    pattern = r"Open Report in Browser"
    # print(text, pattern)
    contains = contains_regex(text, pattern)
    # print(contains)
    return contains



def results_match(e_error, r_error):
    expected = re.findall(r'\b\d+\b', str(e_error))
    resultE = re.findall(r'\b\d+\b', str(r_error))
    print(expected, resultE)
    # print(error_match)
    pattern = r"Verify no findings"
    x = contains_regex(e_error, pattern)
    for item in expected:
        if item in resultE[::-1] and x is False:
            p_f = "Pass"
        elif expected not in resultE and x is True:
            p_f = "Pass"
        else:
            p_f = "Rule gap"
        return p_f
    # if x is True and expected not in resultE:
    #     p_f = "Pass"
    # elif x is False and all(item in expected for item in resultE[::-1]):
    #     p_f = "Pass"
    # else:
    #     p_f = "rule gap"    
    # return p_f



def grab_thing(driver, grab_that):
    try:
        found_thing = driver.find_element(By.XPATH, value=grab_that).get_attribute("textContent")
        # print(found_thing)
    except Exception as e: 
        print(e)
    return found_thing


def get_sequence(driver, sequence_num):
    one_sequence = "/html/body/lorenz-root/lorenz-main-shell/lorenz-shell/lls-shell-nav/mat-sidenav-container/mat-sidenav-content/div/div[2]/db-submission-repository/div/as-split/as-split-area[2]/db-sequences/div/div/div[1]/div[1]/db-sequences-table/div/lls-table/p-treetable/div/div[1]/div/p-scroller/div/table/tbody/tr/td[2]"
    found_text = driver.find_element(By.XPATH, value=one_sequence).text
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


def get_restults():
    error = []
    val_date = []
    val_tester = []
    df = main.df
    for i in range(main.i_start, main.i_end):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--log-level=1") # this was added to address a weird tensor flow error that stopped testing
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
        print(app_num)
        sequence_num = df['Sequence'].iloc[i]
        print("DataFrame index number {} of {}".format(i, main.i_end))
    # select test_win_pool
        click_thing(driver, pool_xpath)
        click_thing(driver, win_pool)
    #find & select application BLA125106
        print("input app num")
        send_thing(driver, app_one, app_num)
        driver.implicitly_wait(20000)
        click_thing(driver, button_ui)
        click_thing(driver, find_application)
    # find sequence 0190
        print("click sequence")
        click_that = get_sequence(driver, sequence_num)
        click_thing(driver, click_that)
        driver.implicitly_wait(20000)
    #check rules 
        val = skip_error(driver, validation_ok)
        print(val)
        if val == False:
    #grab rules 
            r = grab_thing(driver, rules)
            driver.implicitly_wait(40000)
            print(r)
            print("got text!")
        else:
            r = "0 validation errors"
        error.append(r)
        print(error)
    #grab date 
        d = grab_thing(driver, validation_date)
        print("got date")
    #update dataframe
        val_date.append(d)
        print(val_date)
        print("date list updated")
    #grab tester 
        t = grab_thing(driver, tester)
        print("got tester")
        driver.implicitly_wait(40000)
    #update dataframe
        val_tester.append(t)
        print(val_tester)
        print("tester list updated")
    #refresh the drive
        driver.quit()
        print("driver restart")
    df1 = pd.DataFrame(error, columns=['Errors'])
    df2 = pd.DataFrame(val_date, columns=['Date'])
    df3 = pd.DataFrame(val_tester, columns=['Tester'])
    frames = [df1, df2, df3]
    re = pd.concat(frames, axis=1)
    df4 = pd.DataFrame(re)
    print(df4)
    return df4



def check_pass_fail():
    testResults = get_restults()
    df2 = main.df
    print(len(df2))
    print(len(testResults))
    frames = [df2, testResults]
    f_results = pd.concat(frames, axis=1)
    match = []
    for i in range(0, len(f_results)):
        e_error = f_results['Expected Error'].iloc[i]
        r = f_results['Errors'].iloc[i]
        m = results_match(e_error, r)
        match.append(m)
    dfm = pd.DataFrame(match, columns=['Results'])
    frames = [f_results, dfm]
    final_df = pd.concat(frames, axis=1)
    return final_df



DF = check_pass_fail()
print(DF)
DF.to_csv(r'C:\Users\Sara.Rieck\Code\TestResults.csv', index=False)
