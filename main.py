from src.encryption import Encrypt
from src.decryption import Decrypt

if __name__ == '__main__':
    key = int(input('Key to encode: '))
    encryptor = Encrypt(key)
    decryptor = Decrypt(key)

    with open('text.txt', 'a+') as file:
        # program reads the whole content of the file, encrypts it and appends the encrypted text
        # to the file
        file.seek(0)   # return with cursor to the beginning of file
        text = file.read()

        # saving the encrypted text
        encrypted = encryptor.encrypt_text(text)
        file.write(f'\n\n{encrypted}')

        # saving the decrypted text
        decrypted = decryptor.decrypt_text(encrypted)
        file.write(f'\n\n{decrypted}')


