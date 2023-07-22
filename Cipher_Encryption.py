def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


print('''### Caesar Cipher Encryptor/Decryptor ###
-----------------------------------------''')
print('''1. Encrypt Text
2. Decrypt Text''')

inp=int(input('Enter your Choice: '))

if inp==1:
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = caesar_cipher_encrypt(text, shift)
    print("Encrypted Text:", encrypted_text)

elif inp==2:
    encrypted_text = input("Enter the text to decrypt: ")
    shift = int(input("Enter the shift value: "))
    decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
    print("Decrypted Text:", decrypted_text)

