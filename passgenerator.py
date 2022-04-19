from contextlib import nullcontext
import string
import random
 
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
special = string.punctuation

passLength = int(input("Enter length of password?: "))
useSpecial = input("Would you like special characters? (" + special + ")?: ")
useNumbers = input("Would you like to use numbers?: ")
useUpper = input("Would you like to use uppercase letters?: ")
useLower = input("Would you like to use lowercase letters?: ")

all = ""

if useSpecial.lower() == "true":
    all += special
if useNumbers.lower() == "true":
    all += num
if useUpper.lower() == "true":
    all += upper
if useLower.lower() == "true":
    all += lower

password = ""

for x in range(passLength):
    password += random.choice(all)

print(password)
    

