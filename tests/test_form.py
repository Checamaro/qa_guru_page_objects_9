from selene import have
from selene import browser
import os


"""Заполняем форму регистрации"""


def test_form():
    browser.open('/')
    browser.element('#firstName').type('Kirill') # input first name
    browser.element('#lastName').type('Sharevich') # input last name
    browser.element('#userEmail').type('email@example.com') # input email
    browser.element('[for="gender-radio-1"]').click() # click gender radio-button
    browser.element('#userNumber').type('9119119191') # input phone number
    browser.element('#dateOfBirthInput').click() # click calender
    browser.element('option[value="2024"]').click() # choose year
    browser.element('.react-datepicker__day--011').click() # choose date
    browser.element('#subjectsInput').type('Maths').press_enter() # choose subject from drop-menu
    browser.element('[for="hobbies-checkbox-1"]').click() # click hobby checkbox
    browser.element('#uploadPicture').send_keys(os.path.abspath('../data/img/pivottable1.png')) # download picture
    browser.element('#currentAddress').type('Saint-Petersburg') # typing address
    browser.element('#react-select-3-input').type('Haryana').press_enter() # choose state from drop-menu
    browser.element('#react-select-4-input').type('Karnal').press_enter() # choose state from drop-menu
    browser.element('.practice-form-wrapper [id=submit]').click() # click submit button
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form'))  # check for filled form is visible
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
    )) # check for all data
