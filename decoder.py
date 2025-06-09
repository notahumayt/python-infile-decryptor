from cryptography.fernet import Fernet
import base64

print("PYTHON INFILE DE_CRYPTOGRAPHING v.0.1decode by HumaYT")

print("\nChoose mode of decoding:") #Выбор режима
print("1 - Custom key") #Ключ хранится в памяти пользователя
print("2 - Random file key") #Ключ хранится в отдельном файле
mode = int(input()) #Переменная режима

print("Name of file (with extension)")
f1 = input()

if mode == 2:
     print("Name of file 2 (key) (with extension)")
     f2 = input()

s = open(f1, errors="ignore").readlines()
encrypted = s[-1]
if mode == 2:
    s = open(f2, errors="ignore").readlines()
    key = s[-1]
else:
    print("Enter custom key:")
    key = base64.urlsafe_b64encode(str(input()).encode("utf-8").ljust(32)[:32])
fkey = Fernet(key)
# print(key)

decrypted = fkey.decrypt(encrypted).decode('utf-8')

with open('decrypted.txt', 'a+') as file:
    file.write(decrypted)

print('Succesfully decrypted result to decrypted.txt')
input()