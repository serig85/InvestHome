class LocatorsMainPage:
    fist_name_locator = '//input[@id ="firstName"]'
    last_name_locator = '//input[@id ="lastName"]'
    email_locator = '//div[@id ="userEmail-wrapper"]//input'

    gender_male_locator = '//input[@id ="gender-radio-1"]/parent::div'
    gender_female_locator = '//input[@id ="gender-radio-2"]/parent::div'
    gender_other_locator = '//input[@id ="gender-radio-3"]/parent::div'

    mobile_num_locator = '//input[@id ="userNumber"]'
    date_of_birch_locator = '//input[@id ="dateOfBirthInput"]'
    subjects_locator = '//input[@id = "subjectsInput"]'

    hobbies_sport_locator = '//input[@id = "hobbies-checkbox-1"]/parent::div'
    hobbies_reading_locator = '//input[@id = "hobbies-checkbox-2"]/parent::div'
    hobbies_music_locator = '//input[@id = "hobbies-checkbox-3"]/parent::div'

    file_locator = '//input[@id = "uploadPicture"]'

    current_address_locator = '//textarea[@id = "currentAddress"]'

    select_states_locator = '//div[@id = "state"]'

    state_NCR_locator = '//div[@class =" css-11unzgr"]/div[text() ="NCR"]'
    state_Uttar_Pradesh_locator = '//div[@class =" css-11unzgr"]/div[text() ="Uttar Pradesh"]'
    state_Haryana_locator = '//div[@class =" css-11unzgr"]/div[text() ="Haryana"]'
    state_Rajasthan_locator = '//div[@class =" css-11unzgr"]/div[text() ="Rajasthan"]'

    select_city_locator = '//div[@id = "city"]'

    city_NCR_Delhi_locator = '//div[@class = " css-11unzgr"]//div[text() ="Delhi"]'
    city_NCR_Gurgaon_locator = '//div[@class = " css-11unzgr"]//div[text() ="Gurgaon"]'
    city_NCR_Noida_locator = '//div[@class = " css-11unzgr"]//div[text() ="Noida"]'

    city_Uttar_Pradesh_Agra_locator = '//div[@class = " css-11unzgr"]//div[text() ="Agra"]'
    city_Uttar_Pradesh_Lucknow_locator = '//div[@class = " css-11unzgr"]//div[text() ="Lucknow"]'
    city_Uttar_Pradesh_Merrut_locator = '//div[@class = " css-11unzgr"]//div[text() ="Merrut"]'

    city_Haryana_Karnal_locator = '//div[@class = " css-11unzgr"]//div[text() ="Karnal"]'
    city_Haryana_Panipat_locator = '//div[@class = " css-11unzgr"]//div[text() ="Panipat"]'

    city_Rajasthan_Jaipur_locator = '//div[@class = " css-11unzgr"]//div[text() ="Jaipur"]'
    city_Rajasthan_Jaiselmer_locator = '//div[@class = " css-11unzgr"]//div[text() ="Jaiselmer"]'

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