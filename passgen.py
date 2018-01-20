import string
from random import *

numbers = string.digits
upper = string.ascii_uppercase
lower = string.ascii_lowercase
characters = "!@#$%^&*()_+"
print"""\n***************************"""
print"""*Password Recommendations:*"""
print"""***************************"""
print"""1. Minimum of 14 Characters"""
print"""2. AT LEAST 2 of the following:\n
\tNumbers\n
\tUppercase Letters\n
\tLowercase Letters\n\n"""

isgood = True
while isgood == True:
    numpasschar = int(raw_input('How long should your password be?\n>>>'))
    numnum = int(raw_input('How many numbers should be included?\n>>>'))
    numuplet = int(raw_input('How many uppercase letters?\n>>>'))
    numchar = int(raw_input('How many special characters?\n>>>'))

    numtot = numnum + numuplet + numchar
    if numtot <= numpasschar:
        numlowlet = numpasschar - numnum - numuplet - numchar

        password = []
        randpass = []
        finpass = ""
        for x in range(numnum):
            randnum = choice(numbers)
            password.append(randnum)

        for x in range(numuplet):
            randup = choice(upper)
            password.append(randup)

        for x in range(numchar):
            randchar = choice(characters)
            password.append(randchar)

        for x in range(numlowlet):
            randlow = choice(lower)
            password.append(randlow)

        while len(password) > 0:
            numforrandint = randint(0, len(password))
            passchoi = choice(password)
            randpass.append(passchoi)
            password.remove(passchoi)


        for x in randpass:
            finpass = finpass + x

        print "Here is your NEW password: ", finpass
        tryagain = raw_input("Would you like to try again? y/n\n>>>")
        if tryagain != "y":
            isgood = False
        else:
            pass
    else:
        print "\nPlease try again. Your numbers do not add up.\n"
