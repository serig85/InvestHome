import allure
import selene
from page.main_page import (save_data, precondition_function, postcondition_function,
                            student_name, email, gender, mobile, mobile_neg,
                            date_of_birch, subjects, hobbies, picture,
                            current_address, state_city)

PAGE_URL = 'https://demoqa.com/automation-practice-form'


class TestPage:

    def setup_class(self):
        print('hello')
        save_data()
        self.page = selene.browser.open(PAGE_URL)
        precondition_function(self.page)

    def teardown_class(self):
        print('by')
        postcondition_function(self.page)

    @allure.title("Test fist/last name")
    @allure.story("Flickering test")
    def test_student_name(self):
        student_name(self.page)

    @allure.title("Test email")
    @allure.story("Good test")
    def test_email(self):
        email(self.page)

    @allure.title("Test gender")
    @allure.story("Good test")
    def test_gender(self):
        gender(self.page)

    @allure.title("Test mobile")
    @allure.story("Good test")
    def test_mobile(self):
        mobile(self.page)

    @allure.title("Bad test mobile rigged")
    @allure.story("Bad test")
    def test_mobile_neg(self):
        mobile_neg(self.page)

    @allure.title("Test date_of_birch")
    @allure.story("Good test")
    def test_date_of_birch(self):
        date_of_birch(self.page)

    @allure.title("Test subjects")
    @allure.story("Bad test")
    def test_subjects(self):
        subjects(self.page)

    @allure.title("Test hobbies")
    @allure.story("Good test")
    def test_hobbies(self):
        hobbies(self.page)

    @allure.title("Test picture")
    @allure.story("Good test")
    def test_picture(self):
        picture(self.page)

    @allure.title("Test current_address")
    @allure.story("Good test")
    def test_current_address(self):
        current_address(self.page)

    @allure.title("Test state and city")
    @allure.story("Good test")
    def test_state_city(self):
        state_city(self.page)
