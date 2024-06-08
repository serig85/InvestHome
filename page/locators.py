class LocatorsMainPage:
    fist_name_locator = '//input[@id ="firstName"]'
    last_name_locator = '//input[@id ="lastName"]'
    email_locator = '//div[@id ="userEmail-wrapper"]//input'

    gender_dict = {
        'Male': '//input[@id ="gender-radio-1"]/parent::div',
        'Female': '//input[@id ="gender-radio-2"]/parent::div',
        'Other': '//input[@id ="gender-radio-3"]/parent::div'}

    mobile_num_locator = '//input[@id ="userNumber"]'
    date_of_birch_locator = '//input[@id ="dateOfBirthInput"]'
    subjects_locator = '//input[@id = "subjectsInput"]'
    hobbies_dict = {
                    'Sports': '//input[@id = "hobbies-checkbox-1"]/parent::div',
                    'Reading': '//input[@id = "hobbies-checkbox-2"]/parent::div',
                    'Music': '//input[@id = "hobbies-checkbox-3"]/parent::div'}

    file_locator = '//input[@id = "uploadPicture"]'

    current_address_locator = '//textarea[@id = "currentAddress"]'

    select_states_locator = '//div[@id = "state"]'

    state_dict = {
                'NCR': '//div[@class =" css-11unzgr"]/div[text() ="NCR"]',
                'Uttar Pradesh': '//div[@class =" css-11unzgr"]/div[text() ="Uttar Pradesh"]',
                'Haryana': '//div[@class =" css-11unzgr"]/div[text() ="Haryana"]',
                'Rajasthan': '//div[@class =" css-11unzgr"]/div[text() ="Rajasthan"]'}

    select_city_locator = '//div[@id = "city"]'

    city_dict = {
        # NCR
        'Delhi': '//div[@class = " css-11unzgr"]//div[text() ="Delhi"]',
        'Gurgaon': '//div[@class = " css-11unzgr"]//div[text() ="Gurgaon"]',
        'Noida': '//div[@class = " css-11unzgr"]//div[text() ="Noida"]',
        # Uttar Pradesh
        'Agra': '//div[@class = " css-11unzgr"]//div[text() ="Agra"]',
        'Lucknow': '//div[@class = " css-11unzgr"]//div[text() ="Lucknow"]',
        'Merrut': '//div[@class = " css-11unzgr"]//div[text() ="Merrut"]',
        # Haryana
        'Karnal': '//div[@class = " css-11unzgr"]//div[text() ="Karnal"]',
        'Panipat': '//div[@class = " css-11unzgr"]//div[text() ="Panipat"]',
        # Rajasthan
        'Jaipur': '//div[@class = " css-11unzgr"]//div[text() ="Jaipur"]',
        'Jaiselmer': '//div[@class = " css-11unzgr"]//div[text() ="Jaiselmer"]'}

    submit_locator = '//button[@id = "submit"]'


class LocatorPopUpWindows:
    student_name = '//td[text()="Student Name"]/following-sibling::td'
    student_email_locator = '//td[text()="Student Email"]/following-sibling::td'
    gender_locator = '//td[text()="Gender"]/following-sibling::td'
    mobile_locator = '//td[text()="Mobile"]/following-sibling::td'
    date_of_birth_locator = '//td[text()="Date of Birth"]/following-sibling::td'
    subjects_locator = '//td[text()="Subjects"]/following-sibling::td'
    hobbies_locator = '//td[text()="Hobbies"]/following-sibling::td'
    picture_locator = '//td[text()="Picture"]/following-sibling::td'
    address_locator = '//td[text()="Address"]/following-sibling::td'
    state_and_city_locator = '//td[text()="State and City"]/following-sibling::td'
    button_locator = '//button[@id="closeLargeModal"]'
