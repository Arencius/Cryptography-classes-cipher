import random
import enchant

ALPHABET = 'abcdefghijklmnopqrstuwxyz'


def is_english(word):
    """
    Checks if given word is a correct word in english.
    :param word: word to check
    :return: bool, True if given word is a correct english word
    """
    english_dict = enchant.Dict('en_US')
    return english_dict.check(word)


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
        while True:
            original_index = random.choice(indexes)
            if ((original_index + secret_value) * self.key) % len(ALPHABET) == ALPHABET.index(letter):
                return ALPHABET[original_index]

    def decrypt_text(self, text):
        """

        :param text:
        :return:
        """
        # odd numbers from 3 to 21
        secret_values = list(range(3, 22, 2))
        text_translated = False
        new_text = ''

        while not text_translated:
            secret_value = random.choice(secret_values)
            new_text += self.decrypt_letter(text.split()[0], secret_value)

            if is_english(new_text):
                return new_text