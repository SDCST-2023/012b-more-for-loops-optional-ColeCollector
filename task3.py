#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]



user = input("Enter a username: ")

for i in users:
    if i == user: 
        passnum = users.index(user)
        password = input("Enter a password: ")

        if password == passwords[passnum]:
            print("Acess granted!")
            exit()

        else:
            print("Acess denied")
            exit()

    if i != user:
        print("Acess denied")
        exit()



