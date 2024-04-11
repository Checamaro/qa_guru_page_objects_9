from pages.registration_page import RegistrationPage
from data.users import User


def test_fill_form():
    kirill = User(
        first_name='Kirill',
        last_name='Sharevich',
        user_email='email@example.com',
        user_gender='Male',
        user_number='9119119191',
        date='02 October,2020',
        subject='Maths',
        hobby='Sports',
        file='',
        current_address='Saint-Petersburg',
        state='Haryana',
        city='Karnal'
    )

    page = RegistrationPage()

    page.open()
    page.fill(kirill)
    # page.path()
    page.submit()
    # page.should_have_registered()
    page.check_for_submit_form_is_visible(kirill)





