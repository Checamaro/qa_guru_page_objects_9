from pages.registration_page import RegistrationPage
from data.users import User


def test_fill_form():
    kirill = User(
        first_name='Kirill',
        last_name='Sharevich',
        user_email='email@example.com',
        user_gender='Male',
        user_number='9119119191',
        year='1988',
        month='April',
        day='30',
        subject='Maths',
        hobby='Sports',
        file='pivottable1.png',
        current_address='Saint-Petersburg',
        state='Haryana',
        city='Karnal'
    )

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill(kirill)
    registration_page.submit()
    registration_page.check_for_submit_form_is_visible(kirill)





