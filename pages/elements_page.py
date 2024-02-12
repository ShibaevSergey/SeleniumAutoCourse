import random
import time
from generator.generator import generated_person
from selenium.webdriver.common.by import By
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocator, \
    WebTablePageLocator
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_field_form(self):
        full_name = self.element_is_presence(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_presence(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_presence(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_presence(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self) -> []:
        checked_list = self.elements_are_presence(self.locators.CHECKED_ITEMS)
        list = []
        for i in checked_list:
            title_item = i.find_element(By.XPATH, self.locators.TITLE_ITEM)
            list.append(title_item.text.split('.')[0].replace(' ', '').lower())
        return list

    def get_result(self) -> []:
        result = self.elements_are_presence(self.locators.RESULT_ITEMS)
        list = []
        for i in result:
            list.append(i.text.lower())
        return list

class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocator()

    def click_rbвот_and_return_name(self, rb: RadioButtonPageLocator) -> str:
        rb = self.element_is_visible(rb)
        rb.click()
        return rb.text

    def get_str_rb_is_selected(self) -> str:
        return self.element_is_presence(self.locators.TEXT_SUCCESS).text

class WebTablePage(BasePage):
    locators = WebTablePageLocator()

    def add_new_person(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        self.element_is_visible(self.locators.ADD_BTN).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SALARY).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
        self.element_is_visible(self.locators.SUBMIT).click()
        return [first_name, last_name, str(age), email, str(salary), department]

    def get_all_rows_person_table(self):
        data = []
        person_list = self.elements_are_presence(self.locators.FULL_PEOPLE_LIST)
        for item in person_list:
            data.append(item.text.splitlines())
        return data