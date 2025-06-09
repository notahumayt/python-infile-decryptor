from cryptography.fernet import Fernet
import base64

print("PYTHON INFILE DE_CRYPTOGRAPHING v.0.1decode by HumaYT")

print("Name of file (with extension)")
f1 = input()

s = open(f1, errors="ignore").readlines()
encrypted = s[-1]
# print(encrypted)

print("Enter custom key:")
key = base64.urlsafe_b64encode(str(input()).encode("utf-8").ljust(32)[:32])
fkey = Fernet(key)
# print(key)

decrypted = fkey.decrypt(encrypted).decode('utf-8')

with open('decrypted.txt', 'a+') as file:
    file.write(decrypted)

print('Succesfully decrypted result to decrypted.txt')
input()