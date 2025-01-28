import random 
import string 


chars = " " + string.punctuation + string.digits + string.ascii_letters


chars = list(chars)

key = chars.copy()

random.shuffle(key)



plain_Text = input("Enter a message to encrypt: ")

cipher_Test = ""

for letter in plain_Text:
    index = chars.index(letter)
    cipher_Test += key[index]


print(f"Orignal message: {plain_Text}")
print(f"Encrypted message: {cipher_Test}")



cipher_Text = input("Enter an encrypted message: ")

plain_Text = ""

for letter in cipher_Text:
    index = key.index(letter)
    plain_Text += chars[index]

print(f"Encrypted message: {cipher_Test}")
print(f"Orignal message: {plain_Text}")


