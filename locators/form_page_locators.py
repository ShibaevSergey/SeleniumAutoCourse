from selenium.webdriver.common.by import By

class FormPageLocators:
    # форма
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    MOBILE_NUMBER = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SUBJECTS = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    UPLOAD_PICTURE = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    SELECT_STATE = (By.XPATH, '//div[10]/div[2]/div/div/div[1]/div[1]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.XPATH, '//div[10]/div[3]/div/div/div[1]/div[1]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # результат
    STUDENT_NAME = (By.XPATH, '//tr[1]/td[2]')
    STUDENT_EMAIL = (By.XPATH, '//tr[2]/td[2]')
    GENDER_RESULT = (By.XPATH, '//tr[3]/td[2]')
    MOBILE_RESULT = (By.XPATH, '//tr[4]/td[2]')
    DATE_OF_BIRTH_RESULT = (By.XPATH, '//tr[5]/td[2]')
    SUBJECTS_RESULT = (By.XPATH, '//tr[6]/td[2]')
    HOBBIES_RESULT = (By.XPATH, '//tr[7]/td[2]')
    PICTURE = (By.XPATH, '//tr[8]/td[2]')
    ADDRESS = (By.XPATH, '//tr[9]/td[2]')
    STATE_AND_CITY = (By.XPATH, '//tr[10]/td[2]')
    CLOSE = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')