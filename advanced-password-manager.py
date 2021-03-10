import random
import array
import os

clear = lambda: os.system('cls')
pause = lambda: os.system('pause')

MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPCASE_CHARACHTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ';', ':', ',', '<', '.', '>', '/', '?']

COMBINED_LIST = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACHTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACHTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbole = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbole

for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
    password = password + x
    
def Generated_pswd():  
    file = open("passwords.txt", 'a')

    print()
    print()
    userName = input("Please enter your username: ")
    email = input("Please enter the email used for the account: ")
    website = input("Please enter the web address here: ")
    print()
    Password = print(f'Your password for {website} under the username {userName} using the email {email} will be "{password}"')
    print()
    print("Information saved under Passwords.txt")
    
    print()
    print()
    
    usrnm = "UserName: " + userName + "\n"
    mail = "Email: " + email + "\n"
    web = "Website: " + website + "\n"
    pwd = "Password: " + password + "\n"
    
    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(mail)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close

def User_pswd():
    file = open("passwords.txt", 'a')
    
    print()
    print()
    UserName = input("Please enter your username: ")
    eMail = input("Please enter the email used for the account: ")
    PaSSword = input("Please enter your password: ")
    Website = input("Please enter the web address here: ")
    
    print()
    print("Information saved under Passwords.txt")
    
    usern = "Username: " + UserName + "\n"
    Email = "Email: " + eMail + "\n"
    pswd = "Password: " + PaSSword + "\n"
    webURL = "Website: " + Website + "\n"
    
    file.write("---------------------------------\n")
    file.write(usern)
    file.write(Email)
    file.write(pswd)
    file.write(webURL)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close

print()
print()

def choice():
    print()
    print()
    option = input('Would you like a "Generated" password or your own "My own" password? ')
    if option == ("Generated"):
        clear()
        print()
        print()
        Generated_pswd()
        print()
        pause()
        clear()
        exit()
    if option == ("generated"): 
        clear()
        print()
        print()
        Generated_pswd()
        print()
        pause()
        clear()
        exit()
    if option == ("My own"):
        clear()
        print()
        print()
        User_pswd()
        print()
        pause()
        clear()
        exit()
    if option == ("my own"):
        clear()
        print()
        print()
        User_pswd()
        print()
        pause()
        clear()
        exit()
    if option == ("My Own"):
        clear()
        print()
        print()
        User_pswd()
        print()
        pause()
        clear()
        exit()
    else:
        print()
        print("Invalid Input.")
        print()
        pause()
        clear()
        choice()

clear()
choice()