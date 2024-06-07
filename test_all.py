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



    @allure.title("Test email")
    def test_email(self):
        email(self.page)

    @allure.title("Test gender")
    def test_gender(self):
        gender(self.page)

    @allure.title("Test mobile")
    @allure.story("Good test")
    def test_mobile(self):
        mobile(self.page)


    @allure.title("Bed test")
    def test_mobile_neg(self):
        mobile_neg(self.page)

    @allure.title("Test date_of_birch")
    def test_date_of_birch(self):
        date_of_birch(self.page)

    @allure.title("Test subjects")
    def test_subjects(self):
        subjects(self.page)

    @allure.title("Test hobbies")
    def test_hobbies(self):
        hobbies(self.page)

    @allure.title("Test picture")
    def test_picture(self):
        picture(self.page)

    @allure.title("Test current_address")
    def test_current_address(self):
        current_address(self.page)