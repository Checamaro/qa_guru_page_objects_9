from pages.registration_page import RegistrationPage
from data.users import User


def test_fill_form():
    kirill = User(
        first_name='Kirill',
        last_name='Sharevich',
        user_email='email@example.com',
        user_gender='Male',
        user_number='9119119191',
        date='11 April,2024',
        subject='Maths',
        hobby='Sports',
        file='pivottable1.png',
        current_address='Saint-Petersburg',
        state='Haryana',
        city='Karnal'
    )

    page = RegistrationPage()

    page.open()
    page.fill(kirill)
    page.path()
    page.submit()
    page.should_have_registered()





