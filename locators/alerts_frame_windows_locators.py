from selenium.webdriver.common.by import By

class WindowsPageLocators:
    NEW_TAB_BTN = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BTN = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    TITLE_NEW_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

class AlertsPageLocators:
    SEE_ALERT = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    SEE_ALERT_AFTER_FIVE_SECOND = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    SELECTED = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    ENTER_ALERT = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    ENTERED = (By.CSS_SELECTOR, 'span[id="promptResult"]')

class FramesPageLocators:
    BIG_FRAME = (By.CSS_SELECTOR,'iframe[id="frame1"]')
    SMALL_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_FRAME_TEXT = (By.XPATH, '/html/body')
    CHILD_FRAME = (By.XPATH, '//body/iframe')
    CHILD_FRAME_TEXT = (By.XPATH, '//body/p')

class ModalDialogPageLocators:
    SMALL_MODAL_BTN = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BTN = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    MODAL_HEADER = (By.CSS_SELECTOR, 'div[class="modal-title h4"]')
    LARGE_MODAL_BTN = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    SMALL_MODAL_BODY = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    LARGE_MODAL_BODY = (By.XPATH, '//div[2]/p')
    LARGE_MODAL_CLOSE_BTN = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')

