# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:22:57 2021

@author: rrpat
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

''' time sleep are very essential as the button are made such that they change their class
with the time...so wait so that loading is properly completed...then the required buttons will
work properly '''

print("hello world")
from selenium import webdriver
import time
ph='9438639736'
pin=False
age=18
vaccine='covaxin'
pincodes=[751001]
state='Odisha'
district='Khurda'

gecko_path='C:\Program Files\Mozilla Firefox\geckodriver.exe'
driver=webdriver.Firefox(executable_path=gecko_path)
driver.get('https://selfregistration.cowin.gov.in/')


### mobile number entry
time.sleep(10)
searchbox=driver.find_element_by_xpath('//input[@id="mat-input-0"]')
button=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button')
searchbox.clear()

searchbox.send_keys(ph)
time.sleep(5)
button.click()

###otp entry
time.sleep(5)
otpbox=driver.find_element_by_xpath('//input[@id="mat-input-1"]')
confirm_otp_button=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]/div/ion-button')

otp=input('enter otp ')
time.sleep(5)
otpbox.send_keys(otp)
confirm_otp_button.click()

time.sleep(10)
## schedule
driver.find_element_by_link_text('Schedule').click()


### searching by pin
#mat-input-0
time.sleep(3)
if pin:
    for pinocde in pincodes:
        driver.find_element_by_css_selector('div.mat-form-field-infix>input').send_keys(str(pincode))
        time.sleep(1)
        driver.find_element_by_css_selector('.pin-search-btn').click()

else:    
    driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid[1]/ion-row[1]/ion-col[2]/div/label/div').click()
    driver.find_elements_by_css_selector('mat-select')[0].click()
    time.sleep(2)
    state_index=driver.find_elements_by_xpath('//mat-option')
    for d in state_index:
        if d.text==state:
            d.click()
            break
        elif d==state_index[-1]:
            exit("state provided not in list, check for casing and correctness")
    time.sleep(2)
    driver.find_elements_by_css_selector('mat-select')[1].click()
    time.sleep(2)
    district_index=driver.find_elements_by_xpath('//mat-option')
    for d in district_index:
        if d.text==district:
            d.click()
            break
        elif d==district_index[-1]:
            exit("district provided not in list, check for casing and correctness")
    time.sleep(2)
    driver.find_element_by_css_selector('.pin-search-btn').click()
    
    
    

##logout
time.sleep(5)
logout_btn=driver.find_element_by_xpath('/html/body/app-root/ion-app/app-header/ion-header/ion-grid/ion-row[1]/ion-col/ion-row/ion-col[2]/div/ul/li')
logout_btn.click()
time.sleep(10)
driver.close()
