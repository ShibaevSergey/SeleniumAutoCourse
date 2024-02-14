from conftest import driver
from pages.form_page import FormPage


class TestForm:
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.input_data_in_form()
        result = form_page.get_data_from_result()
        assert f'{person.first_name} {person.last_name}' == result.full_name
        assert person.email == result.email
        assert person.gender == result.gender
        assert person.mobile_number == result.mobile_number
        assert person.date_of_birth == result.date_of_birth
        assert person.subjects == result.subjects
        assert person.hobbie == result.hobbie
        assert person.picture == result.picture
        assert person.current_address == result.current_address
        assert f'{person.state} {person.city}' == result.permanent_address