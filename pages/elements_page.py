import base64
import random
import time

from selenium.common import TimeoutException

from generator.generator import generated_person, generated_file
from selenium.webdriver.common.by import By
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocator, \
    WebTablePageLocator, ButtonsPageLocator, LinksPageLocator, UploadDownloadLocator, DynamicPropertiesLocator
from pages.base_page import BasePage
import requests
import os



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

    def click_rb_and_return_name(self, rb: RadioButtonPageLocator) -> str:
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

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.TBX_SEARCH).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_visible(self.locators.BTN_DELETE)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.BTN_EDIT).click()
        self.element_is_visible(self.locators.AGE).clear()
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.BTN_DELETE).click()

    def check_deleted(self) -> str:
        return self.element_is_presence(self.locators.NO_DATA_TEXT).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            self.go_to_element(self.locators.SELECT_ROWS_PER_PAGE)
            self.element_is_visible(self.locators.SELECT_ROWS_PER_PAGE).click()
            locator = (By.CSS_SELECTOR, f'option[value="{x}"]')
            self.element_is_visible(locator).click()
            rows_list = self.elements_are_presence(self.locators.FULL_PEOPLE_LIST)
            data.append(len(rows_list))
        return data

class ButtonsPage(BasePage):
    locators = ButtonsPageLocator()

    def check_double_click(self) -> str:
        element = self.element_is_visible(self.locators.DOUBLE_CLICK_BTN)
        self.double_click(element)
        return self.element_is_visible(self.locators.DOUBLE_CLICK_MESSAGE).text

    def check_right_click(self) -> str:
        element = self.element_is_visible(self.locators.RIGHT_CLICK_BTN)
        self.right_click(element)
        return self.element_is_visible(self.locators.RIGHT_CLICK_MESSAGE).text

    def check_click(self) -> str:
        self.element_is_visible(self.locators.CLICK_BTN).click()
        return self.element_is_visible(self.locators.CLICK_MESSAGE).text

class LinksPage(BasePage):
    locators = LinksPageLocator()

    def check_new_tab_home(self):
        home_link = self.element_is_visible(self.locators.HOME)
        home_href = home_link.get_attribute('href')
        request = requests.get(f'{home_href}')
        if request.status_code == 200:
            home_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return home_href, url
        else:
            raise Exception(f'Bad request. Status code: {request.status_code}')

    def check_bad_request_link(self) -> str:
        bad_request_link = self.element_is_visible(self.locators.BAD_REQUEST)
        request = requests.get('https://demoqa.com/bad-request')
        if request.status_code == 400:
            bad_request_link.click()
            return self.element_is_visible(self.locators.LINK_RESPONCE).text
        else:
            raise Exception(f'Incorrect request. Status code: {request.status_code}, must be 400')

class UploadDownloadPage(BasePage):
    locators = UploadDownloadLocator()

    def upload_file(self) -> str:
        path = generated_file()
        file_input = self.element_is_presence(self.locators.UPLOAD)
        file_input.send_keys(path)
        os.remove(path)
        return os.path.basename(path)

    def read_uploaded_file_name(self) -> str:
        return self.element_is_presence(self.locators.UPLOAD_FILE_NAME).text.split('\\')[-1]

    def download_file(self) -> bool:
        href = self.element_is_presence(self.locators.DOWNLOAD_BTN).get_attribute('href')
        href_b = base64.b64decode(href)
        file = fr'C:\Users\shibaev_SA\Desktop\{random.randint(1, 999)}.jpg'
        with open(file, 'wb+') as image:
            offset = href_b.find(b'\xff\xd8')
            image.write(href_b[offset:])
            check_exist = os.path.isfile(file)
        os.remove(file)
        return check_exist

class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocator()

    def check_enable(self) -> bool:
        return self.element_is_visible(self.locators.ENABLE).is_enabled()

    def check_colour(self):
        return self.element_is_visible(self.locators.COLOUR).value_of_css_property("color")

    def check_exists(self):
        try:
            self.element_is_visible(self.locators.VISIBLE, 1)
        except TimeoutException:
            return False
        return True