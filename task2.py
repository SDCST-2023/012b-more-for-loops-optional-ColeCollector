#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"

username = ""
password = ""
guesses = 0

for i in range (0,3):
    if username != expectedUsername or password != expectedPassword:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        
        if username != expectedUsername or password != expectedPassword:
            if guesses == 3:
                print("Too many failed attempts. Access denied.")
                break
            
            guesses = guesses + 1
            print("Acess denied")

        if username == expectedUsername and password == expectedPassword:
            print("Acess granted!")
                
