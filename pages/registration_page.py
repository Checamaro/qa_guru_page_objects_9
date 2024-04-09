from selene import browser, have
from pathlib import Path
from data.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.user_email)
        browser.element('[for="gender-radio-1"]').click()
        browser.element('#userNumber').type(user.user_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('option[value="2024"]').click()
        browser.element('.react-datepicker__day--011').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()

    def path(file):
        return str(Path(__file__).parent.parent.joinpath(f'data/img/{file}'))

    def submit(self):
        browser.element('.practice-form-wrapper #submit').click()

    def should_have_registered(self):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form'))

    def check_for_submit_form_is_visible(self, users: User):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form'))

        browser.element('.table').all('tr td:nth-child(2)').should(have.texts
            (
            f'{users.first_name} {users.last_name}',
            users.user_email,
            users.user_gender,
            users.user_number,
            users.date,
            users.subject,
            users.hobby,
            users.file,
            users.current_address,
            f'{users.state} {users.city}'
        ))
