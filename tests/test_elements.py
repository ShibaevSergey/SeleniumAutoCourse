import random
import time
from conftest import driver
from locators.elements_page_locators import RadioButtonPageLocator
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage


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

        def test_web_table_search_person(self, driver):
            web_tables_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            key_word = web_tables_page.add_new_person()[random.randint(0, 5)]
            web_tables_page.search_some_person(key_word)
            table_result = web_tables_page.check_search_person()
            assert key_word in table_result, 'Пользователь не был найден в таблице'

        def test_change_person_card(self, driver):
            web_tables_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            last_name = web_tables_page.add_new_person()[1]
            web_tables_page.search_some_person(last_name)
            age = web_tables_page.update_person_info()
            row = web_tables_page.check_search_person()
            assert age in row, 'Возраст не был изменен'

        def test_delete_person(self, driver):
            web_tables_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            email = web_tables_page.add_new_person()[3]
            web_tables_page.search_some_person(email)
            web_tables_page.delete_person()
            assert web_tables_page.check_deleted() == 'No rows found', 'Пользователь не был удален'

        def test_web_table_change_count_rows(self, driver):
            web_tables_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            assert web_tables_page.select_up_to_some_rows() == [5, 10, 20, 25, 50, 100], 'Количество строк в таблице не соответствует установленному'

    class TestButtonsPage:
        def test_click_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            assert buttons_page.check_double_click() == 'You have done a double click', 'Двойной клик не был совершен'
            assert buttons_page.check_right_click() == 'You have done a right click', 'Клик правой кнопкой мыши не был совершен'
            assert buttons_page.check_click() == 'You have done a dynamic click', 'Клик не был совершен'

    class TestLinksPage:
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_home()
            assert href_link == current_url, 'Переход по ссылке произошел не корректно'

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            assert links_page.check_bad_request_link() == 'Link has responded with staus 400 and status text Bad Request'


    class TestUploadDownload:
        def test_upload(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            upload_file_name = upload_download_page.upload_file()
            read_uploaded_file_name = upload_download_page.read_uploaded_file_name()
            assert upload_file_name == read_uploaded_file_name, 'Загруженный файл имеет неверное имя'

        def test_download(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True

    class TestDynamicProperties:
        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            assert dynamic_properties_page.check_enable() == False
            assert dynamic_properties_page.check_colour() == 'rgba(255, 255, 255, 1)'
            assert dynamic_properties_page.check_exists() == False
            time.sleep(5)
            assert dynamic_properties_page.check_enable() == True
            assert dynamic_properties_page.check_colour() == 'rgba(220, 53, 69, 1)'
            assert dynamic_properties_page.check_visible() == True