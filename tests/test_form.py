from pages.registration_page import RegistrationPage


def test_fill_form(browser_management):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Kirill')
    registration_page.fill_last_name('Sharevich')
    registration_page.fill_email('email@example.com')
    registration_page.fill_gender()
    registration_page.fill_number('9119119191')
    registration_page.fill_birthdate()
    registration_page.fill_subject('Maths')
    registration_page.choose_hobbies_checkbox()
    registration_page.upload_picture('../img/pivottable1.png')
    registration_page.fill_current_address('Saint-Petersburg')
    registration_page.choose_state('Haryana')
    registration_page.fill_city('Karnal')
    registration_page.submit_registration()

    registration_page.check_for_submit_form_is_visible()
    registration_page.assert_registered_info()
