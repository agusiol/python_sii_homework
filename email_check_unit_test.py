import unittest
from unit_test_exercise import EmailCheck


class TestEmailCheck(unittest.TestCase):

    def test_not_a_string(self):
        self.assertRaises(Exception, EmailCheck, 123)

    def test_validate_email_correct(self):
        self.assertTrue(EmailCheck("agnieszka.rohm@gmail.com").validate_email())

    def test_validate_email_correct_withnumbers(self):
        self.assertTrue(EmailCheck("agnieszka.rohm123@gmail.com").validate_email())

    def test_validate_email_missing_malpa(self):
        self.assertFalse(EmailCheck("agnieszka.gmail.com").validate_email())

    def test_validate_email_missing_dotcom(self):
        self.assertFalse(EmailCheck("agnieszka@gmail").validate_email())


if __name__ == '__main__':
    unittest.main()