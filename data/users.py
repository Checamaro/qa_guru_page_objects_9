from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_number: str
    user_gender: str
    date: str
    subject: str
    hobby: str
    file: str
    current_address: str
    state: str
    city: str