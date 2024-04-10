from selene import browser, have

from pathlib import Path



class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_gender(self):
        browser.element('[for="gender-radio-1"]').click()
        return self

    def fill_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_birthdate(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('option[value="2024"]').click()
        browser.element('.react-datepicker__day--011').click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def choose_hobbies_checkbox(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        return self

    def upload_picture(file):
        return str(Path(__file__).parent.parent.joinpath(f'data/img/{file}'))

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def choose_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()
        return self

    def fill_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()
        return self

    def submit_registration(self):
        browser.element('.practice-form-wrapper #submit').click()
        return self

    def check_for_submit_form_is_visible(self):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form'))
        return self

    def assert_registered_info(self):
        browser.element('.table').all('tr td:nth-child(2)').should(have.texts
            (
            'Kirill Sharevich',
            'email@example.com',
            'Male',
            '9119119191',
            '11 April,2024',
            'Maths',
            'Sports',
            'pivottable1.png',
            'Saint-Petersburg',
            'Haryana Karnal'
        ))
        return self

