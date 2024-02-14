import os
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class FormPage(BasePage):
    locators = FormPageLocators()


    def input_data_in_form(self):
        person = next(generated_person())
        path = generated_file()
        gender_index = person.gender_index
        hobbie_index = person.hobbie_index
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        radio_button = self.driver.find_element(By.CSS_SELECTOR, f'label[for="gender-radio-{gender_index}"]')
        ActionChains(self.driver).move_to_element(radio_button).click(radio_button).perform()
        person.gender = radio_button.text
        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(person.mobile_number)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.CONTROL, 'a')
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(person.date_of_birth)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(person.subjects)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        check_box = self.driver.find_element(By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{hobbie_index}"]')
        ActionChains(self.driver).move_to_element(check_box).click(check_box).perform()
        person.hobbie = check_box.text
        self.element_is_presence(self.locators.UPLOAD_PICTURE).send_keys(path)
        person.picture = os.path.basename(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.go_to_element(self.element_is_presence(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.go_to_element(self.element_is_presence(self.locators.SELECT_CITY))
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.go_to_element(self.element_is_presence(self.locators.SUBMIT))
        person.state = self.element_is_presence(self.locators.SELECT_STATE).text
        person.city = self.element_is_presence(self.locators.SELECT_CITY).text
        self.element_is_visible(self.locators.SUBMIT).click()
        os.remove(path)
        return person

    def get_data_from_result(self):
        person = next(generated_person())
        person.full_name = self.element_is_visible(self.locators.STUDENT_NAME).text
        person.email = self.element_is_visible(self.locators.STUDENT_EMAIL).text
        person.gender = self.element_is_visible(self.locators.GENDER_RESULT).text
        person.mobile_number = int(self.element_is_visible(self.locators.MOBILE_RESULT).text)
        person.date_of_birth = self.element_is_visible(self.locators.DATE_OF_BIRTH_RESULT).text.replace(',', ' ')
        person.subjects = self.element_is_visible(self.locators.SUBJECTS_RESULT).text
        person.hobbie = self.element_is_visible(self.locators.HOBBIES_RESULT).text
        person.picture = self.element_is_visible(self.locators.PICTURE).text
        person.current_address = self.element_is_visible(self.locators.ADDRESS).text
        person.permanent_address = self.element_is_visible(self.locators.STATE_AND_CITY).text
        self.element_is_visible(self.locators.CLOSE).click()
        return person