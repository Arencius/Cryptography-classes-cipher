class Encrypt:
    ALPHABET  = 'abcdefghijklmnopqrstuwxyz'

    def __init__(self, key:int):
        """
        Class designed to encode the text with asymmetric encryption. To properly encrypt the message,
        algorithm uses the provided key and a secret value not known for a user.
        :param key:
        """
        assert 1 < key, "Key must be positive odd number higher than 1"
        assert key % 5, "Key cannot be divisible by 5"  # encrypting algorithm doesnt work properly
        self.key = key
        self.secret_value = 12
        assert 1 < self.secret_value <= 25, "Secret value must be int in range [2,25]" # limited for reducing computation time during decrypting

    def encrypt_letter(self, letter:str) -> str:
        """
        Function calculates the new index of a letter from text, using the predefined key and secret value.
        :param letter: letter to encrypt
        :return: encrypted letter
        """
        alphabet_length = len(Encrypt.ALPHABET)
        new_letter_index = ((Encrypt.ALPHABET.index(letter) + self.secret_value) * self.key) % alphabet_length

        return Encrypt.ALPHABET[new_letter_index]

    def encrypt_text(self, text:str) -> str:
        """
        Applies the encryption to the whole text
        :param text: text to encrypt
        :return: encrypted text
        """
        return ''.join(self.encrypt_letter(letter) if letter in Encrypt.ALPHABET else letter for letter in text.lower())