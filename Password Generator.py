import secrets
import string

length = int(input("Enter the desired password length : "))

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_chars = lowercase + uppercase + digits + symbols

password = ''.join(secrets.choice(all_chars) for _ in range(length))

print("Generated Password : ", password)