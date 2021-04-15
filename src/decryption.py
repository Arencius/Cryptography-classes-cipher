import random
import enchant
from src.encryption import Encrypt
import re


def is_english(text:str) -> bool:
    """
    Checks if given word is a correct word in english.
    :param text: text to check
    :return: returns True if given text consists of only valid english words
    """

    # initialize the english dictionary
    english_dict = enchant.Dict('en_US')

    for word in text.split():
        if not english_dict.check(word):  # if word is not in dictionary
            return False
    return True


class Decrypt:
    def __init__(self, key:int):
        """
        Class used to decrypt previously encoded message, with the same key that was used to encrypt it.
        :param key: key used in encrypting the message
        """
        self.key = key

    def decrypt_letter(self, letter: str, secret_value: int) -> str:
        """
        Giving the different secret value used to encrypt the message, function returns the letter that matches
        the output of the encrypting algorithm. For example if letter 'd' before encryption was 'm', function
        returns 'm'.

        :param letter: letter to decrypt
        :param secret_value: secret value used for encrypting the text.
                            Function gives the correct output only if those values match.
        :return:
        """
        indexes = list(range(len(Encrypt.ALPHABET)))
        for index in indexes:
            if ((index + secret_value) * self.key) % len(Encrypt.ALPHABET) == Encrypt.ALPHABET.index(letter):
                return Encrypt.ALPHABET[index]

    def decrypt_text(self, text: str) -> str:
        """
        De
        :param text:
        :return:
        """

        for sv in range(2, 26):
            decrypted_text = ''.join(self.decrypt_letter(letter, sv) if letter in ALPHABET else letter for letter in text.lower())
            # text with removed punctuation
            decrypted_text_clear = re.sub(r'[,!?.]', '', decrypted_text)

            # if whole text consists of valid english words, then it's correctly decrypted message
            if is_english(decrypted_text_clear):
                return decrypted_text


text = 'your stuff, is broken. hello carpenter'
e = Encrypt(key = 4)
encrypted = e.encrypt_text(text)
print('Encrypted word:', encrypted)

d = Decrypt(key = 4)
print('Decrypted word:', d.decrypt_text(encrypted))
