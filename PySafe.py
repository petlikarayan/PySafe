import os.path
import tkinter as tk
from cryptography.fernet import Fernet

def checkExistance():
    if os.path.exists("password.txt"):
        pass
    else:
        file = open("password.txt", "w")
        file.write("0\n")
        file.close()

def appendNew():
    file = open("password.txt", "a")

    website = input("Enter the website name: ")
    password = input("Enter the password: ")

    web = website + "\n"
    passwrd = "Password: " + password + "\n"

    file.write("---------------------------\n")
    file.write(web.lower())
    file.write(passwrd)
    file.close()

def readpasswords():
    file = open("password.txt", "r")
    print(file.read())
    file.close()

def readpassword(string):
    file = open("password.txt", "r")
    lineCount = 0
    for line in file:
        lineCount += 1
        if string.lower() == line.rstrip():
            print(str(file.readlines(lineCount + 1)).replace(r"\n", ""))
            break

def program():
    checkExistance()
    passwordLimit = 100
    Input = input("What would you like to do. 1 = Add Password 2 = Read All Passwords 3 = Read Specific Password: ")
    if Input == "1":
        file = open("password.txt", "r")
        f = file.readlines()
        passnum = f[0]
        file.close()
        for passnum in range(passwordLimit):
            passnum += 1
            with open("password.txt") as f:
                lines = f.readlines()
            lines[0] = str(passnum) + "\n"
            with open("password.txt", "w") as f:
                f.writelines(lines)
            appendNew()
            another = input("Would you like to add another password, type yes or no: ")
            if another.lower() == "no":
                break
    elif Input == "2":
        readpasswords()
    elif Input == "3":
        find = input("Name the application")
        readpassword(find)

def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def loadKey():
    return open("key.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encryptedData = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encryptedData)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encryptedData = file.read()
    decryptedData = f.decrypt(encryptedData)
    with open(filename, "wb") as file:
        file.write(decryptedData)

def runProgram(true):
    while true:
        program()
        close = input("Would you like to exit the program, type yes or no: ")
        if close.lower() == "yes":
            encrypt("password.txt", key)
            break

if __name__ == '__main__':
    
    master = "12345678"
    if master == input("Enter master password: "):
        run = True
        if os.path.exists("key.txt"):
            pass
        else:
            ke = open("key.txt", "w")
            ke.write("0")
            ke.close()
        ke = open("key.txt", "r")
        k = ke.readlines()
        ke.close()
        if k[0] == "0":
            writeKey()
            ke = open("key.txt", "w")
            ke.writelines("1")
            key = loadKey()
            runProgram(run)
        else:
            key = loadKey()
            decrypt("password.txt", key)
            runProgram(run)
    else:
        exit()
