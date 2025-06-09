from cryptography.fernet import Fernet
import base64

def addline(floc,s):
    with open(floc, 'a') as file:
        file.write('\n'+s)

print("PYTHON INFILE CRYPTOGRAPHING v.0.1 by HumaYT")

# print("\nChoose mode:") #Выбор режима
# print("1 - Custom key") #Ключ хранится в памяти пользователя
# print("2 - Random infile key") #Ключ хранится в отдельном файле
# mode = int(input()) #Переменная режима

mode = 1

print("Name of file (with extension)")
f1 = input()
# file1 = open(f1,'r+')
# file1_data = file1.read()
# if mode == 2:
#     print("Name of file 2 (key)")
#     f2 = input()
    # file2 = open(f2,'r+')
    # file2_data = file2.read()

# while mode != 1 and mode != 2: #Проверка правильности режима
#     print("Wrong mode number")
#     mode = int(input())

# if mode==1: #Ввод кастомного ключа
print("Enter custom key:")
key = base64.urlsafe_b64encode(str(input()).encode("utf-8").ljust(32)[:32])
# else: #Генерация случайного ключа
#     print("Generating key...")
#     key = Fernet.generate_key()
fkey = Fernet(key)
# print(key)
print("Write your text...") #Шифруемый текст
intext = str(input())

encrypted = fkey.encrypt(intext.encode()).decode('utf-8') #Зашифрованные текст

addline(f1,str(encrypted))
if mode == 2:
    addline(f2,str(fkey))



# print(fkey)
# print(encrypted)
# print(str(fkey.decrypt(encrypted)))
print('Succesfully encrypted!')
input()
