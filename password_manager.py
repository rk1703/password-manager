from cryptography.fernet import Fernet

pwd = input("Enter your master password: ")

'''
run this code to generate a key and save it in a file called key.key
run this code only once

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

generate_key() '''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()

    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            site,user, passw = data.split(" | ")
            print(f"Site: {site}, User: {user}, Password: {fer.decrypt(passw.encode()).decode()}")

def add():
    site = input("Enter the site name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open("passwords.txt", "a") as file:
        file.write(f"{site} | {username} | {fer.encrypt(password.encode()).decode()}\n")       

while True:
    mode = input("Do you want to add a new password or retrieve an existing one or quit? Type 'a' or 'v' or 'q': ").lower()

    if mode == 'q':
        break


    if mode == 'v':
        view()
        
    if mode == 'a':
       add()