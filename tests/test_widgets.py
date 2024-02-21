import random

from conftest import driver
from pages.widgets_page import AccordianPage, AutocompltePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


class TestWidgets:
    class TestAccordian:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            assert accordian_page.test_accordian('first') == ('What is Lorem Ipsum?', 574)
            assert accordian_page.test_accordian('second') == ('Where does it come from?', 763)
            assert accordian_page.test_accordian('third') == ('Why do we use it?', 613)

    class TestAutocomplite:
        def test_multi_autocomplete(self, driver):
            autocomplete_page = AutocompltePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.input_multi(5)
            colors_list = colors[0]
            colors_count = colors[1]
            checked_list = autocomplete_page.check_colors()
            for i in colors_list:
                assert i in checked_list
            value = random.randint(1, colors_count-1)
            autocomplete_page.delete_colors(value)
            assert autocomplete_page.get_colors_count() == colors_count - value

        def test_single_autocomplete(self, driver):
            autocomplete_page = AutocompltePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            assert autocomplete_page.input_single() == autocomplete_page.get_inputed_single()

    class TestDatePickerPage:
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date = date_picker_page.select_date()
            assert date[0] != date[1]

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_time = date_picker_page.select_date_time()
            assert date_time[0].day in date_time[1]
            assert date_time[0].month in date_time[1]
            assert date_time[0].year in date_time[1]
            assert date_time[0].time in date_time[1]

    class TestSliderPage:
        def test_change_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            slider = slider_page.change_value_slider('right')
            assert slider[0] + 25 == slider[1] == slider[2]

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            progress_bar = progress_bar_page.progressing_bar()
            assert progress_bar[0] == progress_bar[2]
            assert progress_bar[0] != progress_bar[1]

    class TestTabsPage:
        def test_tabs_page(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            data = tabs_page.check_tabs()
            assert data == ['true', 'true', 'true', 'false']

    class TestToolTipsPage:
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            tool_tips = tool_tips_page.check_tool_tips()
            assert tool_tips[0] == 'You hovered over the Button'
            assert tool_tips[1] == 'You hovered over the text field'
            assert tool_tips[2] == 'You hovered over the Contrary'
            assert tool_tips[3] == 'You hovered over the 1.10.32'

    class TestMenuPage:
        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            menu = menu_page.check_menu()
            assert menu[0] == ['Sub Item', 'Sub Item', 'SUB SUB LIST »']
            assert menu[1] == ['Sub Sub Item 1', 'Sub Sub Item 2']

    class TestSelectMenu:
        def test_select_value(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            select = select_menu_page.select_value()
            assert select[0] == select[1]

        def test_select_one(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            select = select_menu_page.select_one()
            assert select[0] == select[1]

        def test_select_old_style(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            select = select_menu_page.old_select()
            assert select[0] == select[1]

        def test_multiselect(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            multiselect = select_menu_page.multiselect()
            assert multiselect[0] == multiselect[1]

        def test_standard_multiselect(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            standard_multiselect = select_menu_page.standard_multiselect()
            for i in standard_multiselect[1]:
                assert i in standard_multiselect[0]
            assert len(standard_multiselect[0]) == len(standard_multiselect[1])
