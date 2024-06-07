import allure
import selene

from page.main_page import *
import allure_pytest
import pytest


page_url = 'https://demoqa.com/automation-practice-form'

class TestPage:
    def setup_class(self):
        print('hello')
        self.page = selene.browser.open(page_url)
        precondition_function(self.page)


    def teardown_class(self):
        print('by')
        postcondition_function(self.page)

    @allure.title("Test fist/last name")
    def test_student_name(self):
        student_name(self.page)

    @allure.title("Test mobile")
    @allure.story("Good test")
    def test_mobile(self):
        mobile(self.page)


    @allure.title("Bed test")
    def test_mobile_neg(self):
        mobile_neg(self.page)

    @allure.title("Test email")
    def test_email(self):
        email(self.page)
