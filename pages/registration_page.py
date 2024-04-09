from selene import browser, have
import os


class RegistrationPage:

    def open(self):
        browser.open('/')

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
        browser.element('#uploadPicture').send_keys(os.path.abspath(user.file))
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()

    def submit(self):
        browser.element('.practice-form-wrapper [id=submit]').click()

    def should_have_registered(self, user):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form'))

    def check_for_submit_form_is_visible(self):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form'))

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
