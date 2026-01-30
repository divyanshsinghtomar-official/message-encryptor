🔐 Message Encryptor in Python

A simple Python program that encrypts and decrypts text messages using a key-based substitution encryption technique.
Each character in the message is replaced using a randomized key, and the same key is used to decrypt the message back to its original form.

This project was built to practice Python fundamentals and understand basic encryption logic.

🚀 Features

Encrypts plain text messages

Decrypts encrypted messages

Uses a randomized character key

Beginner-friendly and easy to understand

🧠 How It Works

A list of characters (letters, digits, symbols, space) is created

A shuffled copy of this list acts as the encryption key

Each character in the message is mapped to a new character using index-based substitution

Decryption reverses the process using the same key

🛠️ Requirements

Python 3.x
(No external libraries required)

▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/message-encryptor.git


Navigate to the project folder:

cd message-encryptor


Run the script:

python encryptor.py

📌 Code
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# Encrypt
plain_text = input("Enter the message: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decrypt
cipher_text = input("Enter the encrypted message: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Decrypted message: {plain_text}")

📚 What I Learned

Working with strings and lists

Index-based character mapping

Using Python’s random and string modules

Understanding basic encryption concepts

🔮 Future Improvements

Save and load encryption keys

Password-based key generation

Convert into a CLI tool

Improve security using stronger encryption methods

⚠️ Disclaimer

This project is for learning purposes only and should not be used for real-world secure communication.
