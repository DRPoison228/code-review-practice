import unittest

from utils.validators import is_valid_email


class TestIsValidEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("user@example.com"))

    def test_missing_domain_dot(self):
        self.assertFalse(is_valid_email("user@.com"))

    def test_empty_string(self):
        self.assertFalse(is_valid_email(""))

    def test_none_value(self):
        self.assertFalse(is_valid_email(None))

    def test_one_letter_tld(self):
        self.assertFalse(is_valid_email("user@example.c"))

    def test_not_an_email(self):
        self.assertFalse(is_valid_email("not-an-email"))


if __name__ == "__main__":
    unittest.main()
