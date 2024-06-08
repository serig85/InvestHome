"""Main page"""
import os
import json
from time import sleep

from selene import query
from selene.api import have
from selene.support.shared import config
from selenium.webdriver import Keys

from static.data import data
from .locators import LocatorsMainPage, LocatorPopUpWindows


config.reports_folder = 'reports'
DATA_PATH = './static/data/stedent.txt'
IMPATH = './static/image/dtjxK5Y9Bt8.jpg'
IMPATH_ABS = os.path.abspath(IMPATH)


datadict = {'fist_name': 'Serg',  # Любой текст
            'last_name': 'Sper',  # Любой текс
            'email': 'test@test.te',  # Адрес электронной почты (проверяется по шаблону)
            'gender': 'Male',  # Одно из трёх Male, Female, Other
            'mobile_num': '0123456789',  # 10 цифр
            'date_of_birch': '08 Aug 1985',  # формат число из 2 цифр пробел месяц сокращенно пробел год 4 цифры
            'hobbies': ['Sports', 'Music'],  # Список составленный из одного/нескольки
            # выбранных из: Sports,Reading,Music
            'subjects': "subg_text",  # Любой текс
            'file_name': IMPATH_ABS,  # Абсолютный путь к файлу изображения.
            'current_address': 'krasniy pahar',  # Любой текс
            'state': 'Uttar Pradesh',  # открыть на странице список выбор штата и выбрать один.
            'city': 'Lucknow'}  # После выбора штата открыть список городов и выбрать один.


def save_data():
    with open(DATA_PATH, 'w') as file:
        json.dump(datadict, file)


def precondition_function(page):
    """ Running before tests """
    page.element(LocatorsMainPage.fist_name_locator).send_keys(datadict['fist_name'])
    page.element(LocatorsMainPage.last_name_locator).send_keys(datadict['last_name'])
    page.element(LocatorsMainPage.email_locator).send_keys(datadict['email'])
    page.element(LocatorsMainPage.gender_dict[datadict['gender']]).click()
    page.element(LocatorsMainPage.mobile_num_locator).send_keys(datadict['mobile_num'])
    dk = datadict['date_of_birch']
    dob = page.element(LocatorsMainPage.date_of_birch_locator)
    dn = dob.get(query.value)
    dob.set_value(dk)
    dob.send_keys(Keys.HOME)
    for _ in dn:
        dob.send_keys(Keys.DELETE)
    dob.press_escape()

    page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    for hobbi in datadict['hobbies']:
        page.element(LocatorsMainPage.hobbies_dict[hobbi]).click()

    page.element(LocatorsMainPage.file_locator).send_keys(datadict['file_name'])
    page.element(LocatorsMainPage.current_address_locator).send_keys(datadict['current_address'])

    page.element(LocatorsMainPage.select_states_locator).click()
    page.element(LocatorsMainPage.state_dict[datadict['state']]).click()
    page.element(LocatorsMainPage.select_city_locator).click()
    page.element(LocatorsMainPage.city_dict[datadict['city']]).click()

    page.element(LocatorsMainPage.subjects_locator).send_keys(datadict['subjects'])
    sleep(10)
    page.element(LocatorsMainPage.submit_locator).submit()
    return page


def postcondition_function(page):
    """Running after tests"""
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
    (page.element(LocatorPopUpWindows.student_email_locator).
     should(have.exact_text(datadict['email'])))


def mobile_neg(page):
    page.element(LocatorPopUpWindows.mobile_locator).should(have.exact_text('012345678'))


def gender(page):
    page.element(LocatorPopUpWindows.gender_locator).should(have.exact_text(datadict['gender']))


def date_of_birch(page):
    date_split = datadict['date_of_birch'].split(' ')
    month_short = date_split[1]

    data_modal = f'{date_split[0]} {data.month_dict[month_short]},{date_split[2]}'
    page.element(LocatorPopUpWindows.date_of_birth_locator).should(have.exact_text(data_modal))


def subjects(page):
    page.element(LocatorPopUpWindows.subjects_locator).should(have.exact_text(datadict['subjects']))


def hobbies(page):
    list_hobbies = page.element(LocatorPopUpWindows.hobbies_locator).get(query.text).split(' ')
    list_hobbies = [i.removesuffix(',') for i in list_hobbies]
    for hobbi in datadict['hobbies']:
        list_hobbies.remove(hobbi)
    assert len(list_hobbies) == 0


def picture(page):
    (page.element(LocatorPopUpWindows.picture_locator).
     should(have.exact_text(datadict['file_name'].rsplit('\\', maxsplit=1)[-1])))


def current_address(page):
    (page.element(LocatorPopUpWindows.address_locator).
     should(have.exact_text(datadict['current_address'])))


def state_city(page):
    (page.element(LocatorPopUpWindows.state_and_city_locator).
     should(have.exact_text(f'{datadict['state']} {datadict['city']}')))
