from selenium.webdriver.common.by import By

class AccordianPageLocators:
    FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')

class AutocompltePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_CLEAR_ALL = (By.CSS_SELECTOR, 'div[class="auto-complete__indicator auto-complete__clear-indicator css-tlfecz-indicatorContainer"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-12jo7m5 auto-complete__multi-value__label"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')

class DatePickerPageLocators:
    DATE = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_DAY = (By.CSS_SELECTOR, 'div[class="react-datepicker__month"] div div')


    DATE_TIME = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_TIME_MONTH = (By.CSS_SELECTOR, 'span[class="react-datepicker__month-read-view--selected-month"]')
    DATE_TIME_MONTHS = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-dropdown-container react-datepicker__month-dropdown-container--scroll"] div div')
    DATE_TIME_YEAR = (By.CSS_SELECTOR, 'span[class="react-datepicker__year-read-view--selected-year"]')
    DATE_TIME_YEARS = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-dropdown-container react-datepicker__year-dropdown-container--scroll"] div div')
    DATE_TIME_TIME = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_TIME_DAYS = (By.CSS_SELECTOR, 'div[class="react-datepicker__month"] div div')

class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')

class ProgressBarPageLocators:
    PROGRESS_BAR = (By.CSS_SELECTOR, 'div[role="progressbar"]')
    START_STOP_BTN = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    RESET_BTN = (By.CSS_SELECTOR, 'button[id="resetButton"]')

class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    ORIGIN_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    USE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    MORE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')

class ToolTipsPageLocators:
    BTN = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TBX = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    CONTRARY_LINK = (By.XPATH, '//div[3]/a[1]')
    SIMPLE_LINK = (By.XPATH, '//div[3]/a[2]')
    TOOLTIP_TEXT = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')

class MenuPageLocators:
    MAIN_ITEM = (By.XPATH, '//ul/li[2]/a')
    SUB_MAIN_ITEM = (By.XPATH, '//ul/li[2]/ul/li[3]/a')
    SUB_MAIN_ITEM_2 = (By.XPATH, '//ul/li[2]/ul/li/a')
    SUB_SUB_MAIN_ITEM_2 = (By.XPATH, '//ul/li[2]/ul/li[3]/ul/li/a')

class SelectMenuLocators:
    CMB_SELECT = (By.CSS_SELECTOR, 'div[id="withOptGroup"]')
    CMB_SELECT_VALUE = (By.CSS_SELECTOR, 'div[class=" css-1uccc91-singleValue"]')
    SELECT_VALUES_MENU = [(By.XPATH, '//div[2]/div/div[1]/div[2]/div[1]'),
                          (By.XPATH, '//div[2]/div/div[1]/div[2]/div[2]'),
                          (By.XPATH, '//div[2]/div/div[2]/div[2]/div[1]'),
                          (By.XPATH, '//div[2]/div/div[2]/div[2]/div[2]'),
                          (By.XPATH, '//div[2]/div/div/div[2]/div/div[3]'),
                          (By.XPATH, '//div[2]/div/div/div[2]/div/div[4]')]
    CMB_SELECT_ONE = (By.CSS_SELECTOR, 'div[id="selectOne"]')
    CMB_SELECT_ONE_VALUE = (By.CSS_SELECTOR, 'div[class=" css-1uccc91-singleValue"]')
    SELECT_ONE_VALUES = [(By.XPATH, '//div[2]/div/div/div[2]/div[1]'),
                         (By.XPATH, '//div[2]/div/div/div[2]/div[2]'),
                         (By.XPATH, '//div[2]/div/div/div[2]/div[3]'),
                         (By.XPATH, '//div[2]/div/div/div[2]/div[4]'),
                         (By.XPATH, '//div[2]/div/div/div[2]/div[5]'),
                         (By.XPATH, '//div[2]/div/div/div[2]/div[6]')]
    OLD_SELECT = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')
    MULTISELECT = (By.XPATH, '//div[7]/div/div')
    MULTISELECT_SELECTED = (By.CSS_SELECTOR, 'div[class="css-12jo7m5"]')
    MULTISELECT_VALUES_TEST = (By.CSS_SELECTOR, 'div[class=" css-26l3qy-menu"] div div')
    STANDARD_MULTISELECT = (By.CSS_SELECTOR, 'select[name="cars"]')

