from src.encryption import Encrypt
from src.decryption import Decrypt, is_english
from unittest import TestCase


class TestEnglish(TestCase):
    def test_single_word(self):
        self.assertTrue(is_english('Hello'))
        self.assertTrue(is_english('Mouse'))
        self.assertFalse(is_english('Buongiorno'))   # check different language
        self.assertFalse(is_english('Goood'))        # check misspelled english word

    def test_longer_text(self):
        self.assertTrue(is_english('Hello there'))
        self.assertTrue(is_english('This is valid english sentence'))
        self.assertFalse(is_english('Buona sera amico'))                     # check sentence in different language
        self.assertFalse(is_english('This is not walid english sentence'))   # check english sentence with mistake

    def test_empty_text(self):
        self.assertRaises(ValueError, is_english, '')