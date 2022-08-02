# -*- coding: utf-8 -*-

"Lesson 2.2 - Introduction to User Input, Processing, and Output"
'''

'''
print("Hello, please enter your name.")
userName = input()
userNumber = 0

print("Hello " + userName + ", it's nice to meet you.\n")

print("Please enter a number from 1-10")
userNumber = input()
print("You chose " + userNumber + " " + userName + ".")

# We can also do it like this:
userLastName = input("Please enter your last name: ")

print("Hello " + userName + " " + userLastName + ".  Let's continue...")



"-----------------------------------------------------------------------------"
#storing strings

studentOne = "Kelly"
studentTwo = "John"

print(studentOne, studentTwo)

print('You must make a "concerted" effort to learn programming')

order = (4 * 5) + (6 - 4)

#inputing integer and floating point values

myNumber = int(input("Please enter a nmber from 11-20: "))

print(myNumber, "\n")    

newNumber = int(userNumber) + myNumber

print(newNumber)

newNumber = newNumber + 1

print(newNumber)

result = newNumber / 3
print(result)

newResult = newNumber % 5
print(newResult)

lastResult = newNumber // 3
print(lastResult)

#formatting 
print("C:\\directory")

print(r'C:\\directory\\directory')

print("Otherwise we have to do C:\\\\directory\\\\directory")

print(f"This is a way to format numbers like {myNumber} and {newNumber} in the same line as string literals")

