import random
import enchant
from src.encryption import Encrypt

ALPHABET = 'abcdefghijklmnopqrstuwxyz'


def is_english(text):
    """
    Checks if given word is a correct word in english.
    :param word: word to check
    :return: bool, True if given word is a correct english word
    """
    english_dict = enchant.Dict('en_US')

    for word in text.split():
        if not english_dict.check(word):  # if word is not english
            return False
    return True


class Decrypt:
    def __init__(self, key):
        self.key = key

    def decrypt_letter(self, letter, secret_value):
        """

        :param letter:
        :param secret_value:
        :return:
        """
        indexes = list(range(len(ALPHABET)))
        for index in indexes:
            if ((index + secret_value) * self.key) % len(ALPHABET) == ALPHABET.index(letter):
                return ALPHABET[index]

    def decrypt_text(self, text):
        """

        :param text:
        :return:
        """
        # odd numbers from 3 to 21
        secret_values = list(range(2, 25))
        new_text = ''

        for sv in secret_values:
            new_text = ''.join(self.decrypt_letter(letter, sv) if letter in ALPHABET else letter for letter in text.lower())

            if is_english(new_text):
                return new_text


text = 'good evening my dear friends whom I love with all my heart'
e = Encrypt(23)
encrypted = e.encrypt_text(text)
print('Encrypted word:', encrypted)

d = Decrypt(23)
print('Decrypted word:', d.decrypt_text(encrypted))
