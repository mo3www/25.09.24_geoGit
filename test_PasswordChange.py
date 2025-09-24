# test_PasswordChange.py

import unittest
from PasswordChange import check_password_strength

class TestCheckPasswordStrength(unittest.TestCase):
    def test_too_short(self):
        self.assertEqual(check_password_strength("Ab1!"), "Weak")
        self.assertEqual(check_password_strength("aB3$7"), "Weak")

    def test_missing_uppercase(self):
        self.assertEqual(check_password_strength("password1!"), "Weak")
        self.assertEqual(check_password_strength("weakpass9@"), "Weak")

    def test_missing_lowercase(self):
        self.assertEqual(check_password_strength("PASSWORD1!"), "Weak")
        self.assertEqual(check_password_strength("UPPERCASE2#"), "Weak")

    def test_missing_digit(self):
        self.assertEqual(check_password_strength("Password!"), "Weak")
        self.assertEqual(check_password_strength("NoDigits!@"), "Weak")

    def test_missing_special(self):
        self.assertEqual(check_password_strength("Password1"), "Weak")
        self.assertEqual(check_password_strength("StrongPass2"), "Weak")

    def test_strong_password(self):
        self.assertEqual(check_password_strength("Password1!"), "Strong")
        self.assertEqual(check_password_strength("A1b2c3d4!"), "Strong")
        self.assertEqual(check_password_strength("Zz9@abcd"), "Strong")

    def test_edge_cases(self):
        # Exactly 8 chars, all requirements
        self.assertEqual(check_password_strength("A1b2c3!d"), "Strong")
        # 8 chars, missing special
        self.assertEqual(check_password_strength("A1b2c3d4"), "Weak")
        # 8 chars, missing digit
        self.assertEqual(check_password_strength("Abcdef!g"), "Weak")
        # 8 chars, missing uppercase
        self.assertEqual(check_password_strength("a1b2c3!d"), "Weak")
        # 8 chars, missing lowercase
        self.assertEqual(check_password_strength("A1B2C3!D"), "Weak")

if __name__ == "__main__":
    unittest.main()