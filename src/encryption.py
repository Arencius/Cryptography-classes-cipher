import random


class Encrypt:
    ALPHABET  = 'abcdefghijklmnopqrstuwxyz'

    def __init__(self, key):
        assert 1 < key, "Key must be positive odd number higher than 1"
        self.key = key
        self.secret_value = 4

    def encrypt_letter(self, letter):
        alphabet_length = len(Encrypt.ALPHABET)
        new_letter_index = ((Encrypt.ALPHABET.index(letter) + self.secret_value) * self.key) % alphabet_length

        return Encrypt.ALPHABET[new_letter_index]

    def encrypt_text(self, text):
        return ''.join(self.encrypt_letter(letter) if letter in Encrypt.ALPHABET else letter for letter in text.lower())


#e = Encrypt(3)
#x = 'abcdefghijklmnopqrstuwxyz'
#print(e.encrypt_text(x))