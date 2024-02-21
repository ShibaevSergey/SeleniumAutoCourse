from conftest import driver
from pages.alerts_frame_windows_page import WindowsPage, AlertsPage, FramePage, NestedFramePage, ModalDialogPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            windows_page = WindowsPage(driver, 'https://demoqa.com/browser-windows')
            windows_page.open()
            assert windows_page.check_new_tab_or_window('tab') == 'This is a sample page'

        def test_new_window(self, driver):
            windows_page = WindowsPage(driver, 'https://demoqa.com/browser-windows')
            windows_page.open()
            assert windows_page.check_new_tab_or_window('window') == 'This is a sample page'

    class TestAlerts:
        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            assert alerts_page.see_alert() == 'You clicked a button'

        def test_see_alert_after_five_second(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            assert alerts_page.see_alert_after_five_second() == 'This alert appeared after 5 seconds'

        def test_check_confirm(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            assert 'Ok' in alerts_page.accept_alert()
            assert 'Cancel' in alerts_page.dismiss_alert()

        def test_input_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            assert alerts_page.input_name_alert() in alerts_page.get_input_name()

    class TestFrames:
        def test_frames(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            assert frame_page.check_frame('big') == ('This is a sample page', '500px', '350px'), 'фрейм не найден'
            assert frame_page.check_frame('small') == ('This is a sample page', '100px', '100px'), 'фрейм не найден'

    class TestNestedFrames:
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramePage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            nested_frame_page.check_nested_frames() == ('Parent frame', 'Child Iframe'), 'Фреймы не найденыс'

    class TestModalDialogs:
        def test_modal_dialogs(self, driver):
            modal_dialog_page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            assert modal_dialog_page.check_small_modal() == ('Small Modal', 47, 'Large Modal', 574)