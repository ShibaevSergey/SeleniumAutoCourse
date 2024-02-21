import random
import time
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from generator.generator import colors, cars
from generator.generator import generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutocompltePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def test_accordian(self, accordian_num):
        accordian = {
            'first': {
                'title': self.locators.FIRST,
                'content': self.locators.FIRST_CONTENT
            },
            'second': {
                'title': self.locators.SECOND,
                'content': self.locators.SECOND_CONTENT
            },
            'third': {
                'title': self.locators.THIRD,
                'content': self.locators.THIRD_CONTENT
            }
        }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return section_title.text, len(section_content)

class AutocompltePage(BasePage):
    locators = AutocompltePageLocators()
    colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    def input_multi(self, count: int):

        colors_new = set()
        for i in range(count):
            colors_new.add(random.sample(self.colors, 1)[0])
        input = self.element_is_visible(self.locators.MULTI_INPUT)
        for i in colors_new:
            input.send_keys(i)
            input.send_keys(Keys.TAB)
        return list(colors_new), len(colors_new)

    def delete_colors(self, count):
        btns_delete = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for i in range(count):
            btns_delete[i].click()

    def check_colors(self):
        data = []
        values = self.elements_are_visible(self.locators.MULTI_VALUE)
        for i in values:
            data.append(i.text)
        return data

    def get_colors_count(self):
        btns_delete = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        return len(btns_delete)

    def input_single(self):
        color = self.colors[random.randint(0, len(self.colors)-1)]
        self.element_is_visible(self.locators.SINGLE_INPUT).send_keys(color)
        self.element_is_visible(self.locators.SINGLE_INPUT).send_keys(Keys.TAB)
        return color

    def get_inputed_single(self) -> str:
        return self.element_is_presence(self.locators.SINGLE_VALUE).text

class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_by_text(self.locators.DATE_MONTH, date.month)
        self.select_by_text(self.locators.DATE_YEAR, date.year)
        self.select_day(self.locators.DATE_DAY, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_by_text(self, element, value):
        select = Select(self.element_is_presence(element))
        select.select_by_visible_text(value)

    def select_day(self, elements, value):
        item_list = self.elements_are_presence(elements)
        for i in item_list:
            if i.text == value:
                i.click()
                break

    def select_month(self, elements, value):
        item_list = self.elements_are_visible(elements)
        for i in item_list:
            if i.text == value:
                i.click()
                break

    def select_time(self, elements, value):
        item_list = self.elements_are_visible(elements)
        for i in item_list:
            if i.text == value:
                i.click()
                break

    def select_year(self, elements, value):
        while ...:
            item_list = self.elements_are_visible(elements)
            data = []
            for i in item_list:
                data.append(i.text)
            if value in data:
                for i in item_list:
                    if i.text == value:
                        i.click()
                        break
                break
            elif int(value) < int(data[1]):
                for i in range(int(data[1]) - int(value)):
                    item_list[len(item_list)-1].click()

    def select_date_time(self):
        date = next(generated_date())
        input_date_time = self.element_is_visible(self.locators.DATE_TIME)
        value_date_time_before = input_date_time.get_attribute('value')
        input_date_time.click()
        self.element_is_visible(self.locators.DATE_TIME_MONTH).click()
        self.select_month(self.locators.DATE_TIME_MONTHS, date.month)
        self.element_is_visible(self.locators.DATE_TIME_YEAR).click()
        self.select_year(self.locators.DATE_TIME_YEARS, date.year)
        self.select_day(self.locators.DATE_TIME_DAYS, date.day)
        self.select_time(self.locators.DATE_TIME_TIME, date.time)
        value_date_time_after = input_date_time.get_attribute('value')
        return date, value_date_time_after

class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_value_slider(self, side):
        slider = self.element_is_visible(self.locators.SLIDER_INPUT)
        slider_value_before = slider.get_attribute('value')
        print(slider_value_before)
        if side == 'right':
            count = random.randint(0, 75)
            print(count)
            for i in range(count):
                slider.send_keys(Keys.RIGHT)
        elif side == 'left':
            count = random.randint(0, int(slider_value_before))
            for i in range(count):
                slider.send_keys(Keys.LEFT)
        slider_value_after = slider.get_attribute('value')
        slider_value = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return count, int(slider_value_after), int(slider_value)

class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()
    def progressing_bar(self):
        start_stop_btn = self.element_is_visible(self.locators.START_STOP_BTN)
        progress_bar = self.element_is_presence(self.locators.PROGRESS_BAR)
        value_before_start = progress_bar.get_attribute('aria-valuenow')
        start_stop_btn.click()
        timer = random.randint(0, 10)
        time.sleep(timer)
        start_stop_btn.click()
        value_after_start = progress_bar.get_attribute('aria-valuenow')
        start_stop_btn.click()
        time_reset = 12 - timer
        time.sleep(time_reset)
        self.element_is_visible(self.locators.RESET_BTN).click()
        value_after_reset = progress_bar.get_attribute('aria-valuenow')
        return value_before_start, value_after_start, value_after_reset

class TabsPage(BasePage):
    locators = TabsPageLocators()
    def check_tabs(self):
        data = []
        data.append(self.check_tab(self.locators.WHAT_TAB))
        data.append(self.check_tab(self.locators.ORIGIN_TAB))
        data.append(self.check_tab(self.locators.USE_TAB))
        data.append(self.check_tab(self.locators.MORE_TAB))
        return data
    def check_tab(self, tab):
        checked_tab = self.element_is_visible(tab)
        try:
            checked_tab.click()
        except ElementClickInterceptedException:
            if checked_tab.get_attribute('aria-disabled') == 'true':
                return 'false'
        return checked_tab.get_attribute('aria-selected')

class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()
    def check_tool_tips(self):
        btn = self.element_is_visible(self.locators.BTN)
        tbx = self.element_is_visible(self.locators.TBX)
        contrary_link = self.element_is_visible(self.locators.CONTRARY_LINK)
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        self.move_to_element(btn)
        time.sleep(0.5)
        btn_tool_tip = self.element_is_visible(self.locators.TOOLTIP_TEXT).text
        self.move_to_element(tbx)
        time.sleep(0.5)
        tbx_tool_tip = self.element_is_visible(self.locators.TOOLTIP_TEXT).text
        self.move_to_element(contrary_link)
        time.sleep(0.5)
        contrary_link_tool_tip = self.element_is_visible(self.locators.TOOLTIP_TEXT).text
        self.move_to_element(simple_link)
        time.sleep(0.5)
        simple_link_tool_tip = self.element_is_visible(self.locators.TOOLTIP_TEXT).text
        return btn_tool_tip, tbx_tool_tip, contrary_link_tool_tip, simple_link_tool_tip

class MenuPage(BasePage):
    locators = MenuPageLocators()
    def check_menu(self):
        main_item_2 = self.element_is_visible(self.locators.MAIN_ITEM)
        self.move_to_element(main_item_2)
        main_item_2.click()
        time.sleep(0.5)
        sub_items = []
        sub_main_items = self.elements_are_visible(self.locators.SUB_MAIN_ITEM_2)
        for i in sub_main_items:
            sub_items.append(i.text)
        sub_main_item_2 = self.element_is_visible(self.locators.SUB_MAIN_ITEM)
        self.move_to_element(sub_main_item_2)
        sub_sub_main_items = self.elements_are_visible(self.locators.SUB_SUB_MAIN_ITEM_2)
        sub_sub_items = []
        for i in sub_sub_main_items:
            sub_sub_items.append(i.text)
        return sub_items, sub_sub_items

class SelectMenuPage(BasePage):
    locators = SelectMenuLocators()
    def select_value(self):
        self.element_is_visible(self.locators.CMB_SELECT).click()
        time.sleep(0.5)
        rand = random.randint(0, 5)
        choosenText = self.element_is_visible(self.locators.SELECT_VALUES_MENU[rand]).text
        self.element_is_visible(self.locators.SELECT_VALUES_MENU[rand]).click()
        value = self.element_is_visible(self.locators.CMB_SELECT_VALUE).text
        return choosenText, value

    def select_one(self):
        self.element_is_visible(self.locators.CMB_SELECT_ONE).click()
        time.sleep(0.5)
        rand = random.randint(0, 5)
        choosenText = self.element_is_visible(self.locators.SELECT_ONE_VALUES[rand]).text
        self.element_is_visible(self.locators.SELECT_ONE_VALUES[rand]).click()
        value = self.element_is_visible(self.locators.CMB_SELECT_ONE_VALUE).text
        return choosenText, value

    def old_select(self):
        rand = random.randint(0, len(colors) - 1)
        select = self.select_by_text(self.locators.OLD_SELECT, colors[rand])
        return select, colors[rand]


    def select_by_text(self, element, value):
        select = Select(self.element_is_presence(element))
        select.select_by_visible_text(value)
        option = select.first_selected_option
        return option.text
    def multiselect_by_text(self, element, values):
        select = Select(self.element_is_presence(element))
        for i in values:
            select.select_by_visible_text(i)
        data = []
        for i in select.all_selected_options:
            data.append(i.text)
        return data

    def multiselect(self):
        rand_count = random.randint(1, 4)
        choosen_colors = []
        self.element_is_visible(self.locators.MULTISELECT).click()
        time.sleep(0.5)
        for i in range(rand_count):
            colors = self.elements_are_visible(self.locators.MULTISELECT_VALUES_TEST)
            rand = random.sample(colors, k=1)
            choosen_colors.append(rand[0].text)
            rand[0].click()
        added_colors = self.elements_are_visible(self.locators.MULTISELECT_SELECTED)
        choosed_colors = []
        for i in added_colors:
            choosed_colors.append(i.text)
        return choosen_colors, choosed_colors

    def standard_multiselect(self):
        choosen_cars = set()
        for i in range(random.randint(1, 4)):
            choosen_cars.add(random.sample(cars, k=1)[0])
        multi = self.multiselect_by_text(self.locators.STANDARD_MULTISELECT, choosen_cars)
        return choosen_cars, multi