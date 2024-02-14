from selenium.webdriver.common.by import By

class AlertsFrameWindowsPageLocators:
    # windows
    NEW_TAB_BTN = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BTN = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    TITLE_NEW_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

    # alerts
    SEE_ALERT = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    SEE_ALERT_AFTER_FIVE_SECOND = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    SELECTED = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    ENTER_ALERT = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    ENTERED = (By.CSS_SELECTOR, 'span[id="promptResult"]')