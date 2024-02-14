import time

from generator.generator import generated_person
from locators.alerts_frame_windows_locators import AlertsFrameWindowsPageLocators
from pages.base_page import BasePage


class AlertsFrameWindowsPage(BasePage):
    locators = AlertsFrameWindowsPageLocators()

    def check_new_tab_or_window(self, checkedObject: str):
        if checkedObject == 'tab':
            self.element_is_visible(self.locators.NEW_TAB_BTN).click()
        elif checkedObject == 'window':
            self.element_is_visible(self.locators.NEW_WINDOW_BTN).click()
        self.switch_tab(1)
        text_title = self.element_is_visible(self.locators.TITLE_NEW_TAB).text
        return text_title

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

