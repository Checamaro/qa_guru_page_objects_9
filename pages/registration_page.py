import os

from selene import browser, have

import data


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def fill_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_number(self, number):
        browser.element('#userNumber').type(number)

    def fill_birthdate(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def choose_hobbies_checkbox(self, hobby):
        if hobby == "Sports":
            browser.element('[for="hobbies-checkbox-1"]').click()
        elif hobby == "Reading":
            browser.element('[for="hobbies-checkbox-2"]').click()
        elif hobby == "Music":
            browser.element('[for="hobbies-checkbox-3"]').click()

    def upload_picture(self, file):
        browser.element('#uploadPicture').set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(data.__file__), f'img/{file}')
            )
        )

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def choose_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def fill_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def submit_registration(self):
        browser.element('.practice-form-wrapper #submit').click()

    def check_for_submit_form_is_visible(self, text):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text(text))
        return self

    def assert_registered_info(self, first_name_and_second_name, email, gender, phone_number, birthday, subject, hobby,
                               file, address, state_and_city):
        browser.element('.table').all('td').even.should(have.texts(

            first_name_and_second_name,
            email,
            gender,
            phone_number,
            birthday,
            subject,
            hobby,
            file,
            address,
            state_and_city
        ))
