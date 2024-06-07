#import selene
from selene import query
from selene.api import by, be, have
from selene.support.shared import config
from selenium.webdriver import Keys

from .locators import LocatorsMainPage, LocatorPopUpWindows
from time import sleep
import os
import json

datapath = './static/data/stedent.txt'
impath = './static/image/dtjxK5Y9Bt8.jpg'
impath_abs = os.path.abspath(impath)
im_file_name = impath.split('/')[-1]
page_url = 'https://demoqa.com/automation-practice-form'

datadict = {'fist_name': 'Serg',
            'last_name': 'Sper',
            'email': 'test@test.te',
            'gender': 'Male',
            'mobile_num': '0123456789',
            'date_of_birch': '8 Jan 1985',
            'hobbies': ['sport', 'music'],
            'subjects': "subg_text",
            'file_name': impath_abs,
            'current_address': 'krasniy pahar',
            'state': 'Haryana',
            'city': 'Panipat'}
def precondition_function(page):
    #page = selene.browser.open(page_url)
    page.element(LocatorsMainPage.fist_name_locator).send_keys(datadict['fist_name'])
    page.element(LocatorsMainPage.last_name_locator).send_keys(datadict['last_name'])
    page.element(LocatorsMainPage.email_locator).send_keys(datadict['email'])
    page.element(LocatorsMainPage.gender_male_locator).click()
    page.element(LocatorsMainPage.mobile_num_locator).send_keys(datadict['mobile_num'])
    dk = datadict['date_of_birch']
    dob = page.element(LocatorsMainPage.date_of_birch_locator)
    dn = dob.get(query.value)
    dob.set_value(dk)
    dob.send_keys(Keys.HOME)
    for i in dn:
        dob.send_keys(Keys.DELETE)
    dob.press_escape()

    page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    page.element(LocatorsMainPage.hobbies_music_locator).click()
    page.element(LocatorsMainPage.hobbies_sport_locator).click()
    page.element(LocatorsMainPage.file_locator).send_keys(datadict['file_name'])
    page.element(LocatorsMainPage.current_address_locator).send_keys(datadict['current_address'])

    page.element(LocatorsMainPage.select_states_locator).click()
    page.element(LocatorsMainPage.state_Haryana_locator).click()
    page.element(LocatorsMainPage.select_city_locator).click()
    page.element(LocatorsMainPage.city_Haryana_Panipat_locator).click()

    page.element(LocatorsMainPage.subjects_locator).send_keys(datadict['subjects'])
    sleep(10)
    page.element(LocatorsMainPage.submit_locator).submit()
    return page

def postcondition_function(page):
    sleep(10)
    page.element(LocatorPopUpWindows.button_locator).click()
    sleep(5)
    page.quit()
    print('end')

def student_name(page):
     names = page.element(LocatorPopUpWindows.student_name).get(query.text).split(' ')
     assert names[0] == datadict['fist_name'] and names[1] == datadict['last_name']
def mobile(page):
    page.element(LocatorPopUpWindows.mobile_locator).should(have.exact_text(datadict['mobile_num']))
def email(page):
    page.element(LocatorPopUpWindows.student_email_locator).should(have.exact_text(datadict['email']))

def mobile_neg(page):
    page.element(LocatorPopUpWindows.mobile_locator).should(have.exact_text('012345678'))
