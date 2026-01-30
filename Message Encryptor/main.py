'''
This is a message encryptor program. It allows users to encrypt and decrypt messages using a key based encryption.
'''
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters 
chars= list(chars)
key=chars.copy()
random.shuffle(key)

#Encrypt
plain_text=input("Enter the messgae ")
cipher_text=""
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]
print(f"Orgianl message: {plain_text}")
print(f"Encrypted message: {cipher_text}")
#Decrypt
cipher_text=input("Enter the messgae to decrypt ")
plain_text=""
for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]
print(f"Decrypted message: {plain_text}")