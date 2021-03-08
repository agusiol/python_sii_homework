""""Napisz klase która przyjmuje stringa.
dodaj metode validate, która zwraca True gdy string jest poprawny
Metoda zwraca False, gdy nie podaliśmy stringa

Dodaj testy jednostkowe zapewniajace pelne pokrycie
"""
import re


class EmailCheck:
    def __init__(self, text):
        if not isinstance(text, str):
            raise Exception("To nie jest string")

        self.text = text

    def validate_email(self):
        email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        if not email_pattern.search(self.text):
            return False

        return True


# moj_email = EmailCheck("agnieszka.rohm@gmail.com")
# print(moj_email.validate_email())
