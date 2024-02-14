from conftest import driver
from pages.alerts_frame_windows_page import AlertsFrameWindowsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            alerts_frame_windows_page = AlertsFrameWindowsPage(driver, 'https://demoqa.com/browser-windows')
            alerts_frame_windows_page.open()
            assert alerts_frame_windows_page.check_new_tab_or_window('tab') == 'This is a sample page'

        def test_new_window(self, driver):
            alerts_frame_windows_page = AlertsFrameWindowsPage(driver, 'https://demoqa.com/browser-windows')
            alerts_frame_windows_page.open()
            assert alerts_frame_windows_page.check_new_tab_or_window('window') == 'This is a sample page'

    class TestAlerts:
        def test_see_alert(self, driver):
            alerts_frame_windows_page = AlertsFrameWindowsPage(driver, 'https://demoqa.com/alerts')
            alerts_frame_windows_page.open()
            assert alerts_frame_windows_page.see_alert() == 'You clicked a button'

        def test_see_alert_after_five_second(self, driver):
            alerts_frame_windows_page = AlertsFrameWindowsPage(driver, 'https://demoqa.com/alerts')
            alerts_frame_windows_page.open()
            assert alerts_frame_windows_page.see_alert_after_five_second() == 'This alert appeared after 5 seconds'

        def test_check_confirm(self, driver):
            alerts_frame_windows_page = AlertsFrameWindowsPage(driver, 'https://demoqa.com/alerts')
            alerts_frame_windows_page.open()
            assert 'Ok' in alerts_frame_windows_page.accept_alert()
            assert 'Cancel' in alerts_frame_windows_page.dismiss_alert()

        def test_input_alert(self, driver):
            alerts_frame_windows_page = AlertsFrameWindowsPage(driver, 'https://demoqa.com/alerts')
            alerts_frame_windows_page.open()
            assert alerts_frame_windows_page.input_name_alert() in alerts_frame_windows_page.get_input_name()