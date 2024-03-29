from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

class CheckBoxPageLocators:
    # COLLAPSE_ALL = (By.CSS_SELECTOR, 'button[title="Collapse all"]')
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = './/ancestor::span[@class="rct-text"]'
    RESULT_ITEMS = (By.CSS_SELECTOR, 'span[class="text-success"]')

class RadioButtonPageLocator:
    RB_YES = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    RB_IMPRESSIVE = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    RB_NO = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    TEXT_SUCCESS = (By.CSS_SELECTOR, 'span[class="text-success"]')

class WebTablePageLocator:
    #person form
    ADD_BTN = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    #table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    TBX_SEARCH = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    BTN_DELETE = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    BTN_EDIT = (By.CSS_SELECTOR, 'span[title="Edit"]')
    NO_DATA_TEXT = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    SELECT_ROWS_PER_PAGE = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

class ButtonsPageLocator:
    DOUBLE_CLICK_BTN = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_BTN = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    CLICK_BTN = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button')
    CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')

class LinksPageLocator:
    HOME = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')
    LINK_RESPONCE = (By.CSS_SELECTOR, 'p[id="linkResponse"]')

class UploadDownloadLocator:
    UPLOAD = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    SUBMIT_UPLOAD = (By.ID, 'file-submit')
    UPLOAD_FILE_NAME = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    DOWNLOAD_BTN = (By.CSS_SELECTOR, 'a[id="downloadButton"]')

class DynamicPropertiesLocator:
    ENABLE = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
    COLOUR = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')