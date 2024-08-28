#usermanager.py
import re


class User:
    def __init__(self, user_id, full_name, phone, email):
        if not all([user_id, full_name, phone, email]):
            raise ValueError("All fields must be filled")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format")
        if not self.is_valid_full_name(full_name):
            raise ValueError("Invalid full name format")

        self.user_id = user_id
        self.full_name = full_name
        self.phone = phone
        self.email = email

    @staticmethod
    def is_valid_email(email):
        return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) is not None

    @staticmethod
    def is_valid_phone(phone):
        return re.match(r"^0[2-9]\d{8}$", phone) is not None

    @staticmethod
    def is_valid_full_name(full_name):
        return re.match(r"^[A-Za-z]{3,30}( [A-Za-z]{3,30})*$", full_name) is not None
