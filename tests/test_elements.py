import time
from conftest import driver
from locators.elements_page_locators import RadioButtonPageLocator
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_field_form()
            assert full_name == output_name, 'Не совпадает введенное имя'
            assert email == output_email, 'Не совпадает введенный email'
            assert current_address == output_current_address, 'Не совпадает текущий адрес'
            assert permanent_address == output_permanent_address, 'Не совпадает постоянный адрес'

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            assert check_box_page.get_checked_checkboxes().sort() == check_box_page.get_result().sort(), 'Чек-бокс не отмечен'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            assert radio_button_page.click_rb_and_return_name(
                RadioButtonPageLocator.RB_YES) == radio_button_page.get_str_rb_is_selected(), 'Клик по радиобаттон Yes не был обработан'
            assert radio_button_page.click_rb_and_return_name(
                RadioButtonPageLocator.RB_IMPRESSIVE) == radio_button_page.get_str_rb_is_selected(), 'Клик по радиобаттон Impressive не был обработан'
            assert radio_button_page.click_rb_and_return_name(
                RadioButtonPageLocator.RB_NO) != radio_button_page.get_str_rb_is_selected(), 'Клик по радиобаттон No был обработан, а не должен был, так как он Disable'

    class TestWebTables:
        def test_web_tables(self, driver):
            web_tables_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            new_person = web_tables_page.add_new_person()
            table = web_tables_page.get_all_rows_person_table()
            assert new_person in table
            time.sleep(5)