import time

from generator.generator import generated_person
from locators.alerts_frame_windows_locators import WindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogPageLocators
from pages.base_page import BasePage


class WindowsPage(BasePage):
    locators = WindowsPageLocators()

    def check_new_tab_or_window(self, checkedObject: str):
        if checkedObject == 'tab':
            self.element_is_visible(self.locators.NEW_TAB_BTN).click()
        elif checkedObject == 'window':
            self.element_is_visible(self.locators.NEW_WINDOW_BTN).click()
        self.switch_tab(1)
        text_title = self.element_is_visible(self.locators.TITLE_NEW_TAB).text
        return text_title

class AlertsPage(BasePage):
    locators = AlertsPageLocators()
    def see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT).click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def see_alert_after_five_second(self):
        self.element_is_visible(self.locators.SEE_ALERT_AFTER_FIVE_SECOND).click()
        time.sleep(6)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def accept_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        return self.element_is_presence(self.locators.SELECTED).text

    def dismiss_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        return self.element_is_presence(self.locators.SELECTED).text

    def input_name_alert(self):
        person = next(generated_person())
        first_name = person.first_name
        self.element_is_visible(self.locators.ENTER_ALERT).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(first_name)
        alert.accept()
        return first_name

    def get_input_name(self):
        return self.element_is_presence(self.locators.ENTERED).text

class FramePage(BasePage):
    locators = FramesPageLocators()
    def check_frame(self, frame_size):
        if frame_size == 'big':
            frame = self.element_is_presence(self.locators.BIG_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_presence(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return text, width, height
        elif frame_size == 'small':
            frame = self.element_is_presence(self.locators.SMALL_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_presence(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return text, width, height

class NestedFramePage(BasePage):
    locators = NestedFramesPageLocators()
    def check_nested_frames(self):
        parent_frame = self.element_is_presence(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.elements_are_presence(self.locators.PARENT_FRAME_TEXT)[0].text
        child_frame = self.element_is_presence(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_presence(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text

class ModalDialogPage(BasePage):
    locators = ModalDialogPageLocators()
    def check_small_modal(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BTN).click()
        small_modal_header = self.element_is_visible(self.locators.MODAL_HEADER).text
        len_small_modal_text = len(self.element_is_visible(self.locators.SMALL_MODAL_BODY).text)
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BTN).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BTN).click()
        large_modal_header = self.element_is_visible(self.locators.MODAL_HEADER).text
        len_large_modal_text = len(self.element_is_visible(self.locators.LARGE_MODAL_BODY).text)
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BTN).click()
        return small_modal_header, len_small_modal_text, large_modal_header, len_large_modal_text