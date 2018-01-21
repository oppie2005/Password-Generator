import string
from random import *

numbers = string.digits
upper = string.ascii_uppercase
lower = string.ascii_lowercase
characters = "!@#$%^&*()_+"
print("""\n***************************\n
*Password Recommendations:*\n
***************************\n
1. Minimum of 14 Characters\n
2. AT LEAST 2 of the following:\n
\tNumbers\n\tUppercase Letters\n\tLowercase Letters\n\n""")

def selchar(numchars, charlist, randlist):
    for x in range(numchars):
        randchar = choice(charlist)
        randlist.append(randchar)

isgood = True
while isgood == True:
    numpasschar = int(input('How long should your password be?\n>>>'))
    numnum = int(input('How many numbers should be included?\n>>>'))
    numuplet = int(input('How many uppercase letters?\n>>>'))
    numchar = int(input('How many special characters?\n>>>'))

    numtot = numnum + numuplet + numchar
    if numtot <= numpasschar:
        numlowlet = numpasschar - numnum - numuplet - numchar

        password = []
        randpass = []
        finpass = ""

        selchar(numnum, numbers, password)
        selchar(numuplet, upper, password)
        selchar(numchar, characters, password)
        selchar(numlowlet, lower, password)

        while len(password) > 0:
            numforrandint = randint(0, len(password))
            passchoi = choice(password)
            randpass.append(passchoi)
            password.remove(passchoi)


        for x in randpass:
            finpass = finpass + x

        print ("Here is your NEW password: " + finpass)
        tryagain = input('Would you like to try again? y/n \n>>>')
        if tryagain != "y":
            isgood = False
        else:
            pass
    else:
        print ("\nPlease try again. Your numbers do not add up.\n")
