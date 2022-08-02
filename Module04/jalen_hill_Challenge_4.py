
from tkinter.messagebox import YES


CORRECT_VALUE = 30
userAns = input('Hello, would you like to play a game?')

if userAns == 'yes':
    correct = False
    userNum = 0
    attempts = 0
    userNum = int(input('Please enter a number betwen 1-50:'))
    while correct != True:
        attempts += 1
        if userNum == CORRECT_VALUE:
            print(f'You guessed the correct number. Congratulations!\n' + f'It took you exactly {attempts} attempts to guess correctly.')
            correct = True
        elif userNum >=25 and userNum <=35:
            print('Your guess is within 5 digits of the correct number.')
            userNum = int(input('Please choose again:'))
        elif userNum < 1 or userNum > 50:
            print('Please enter a number between 1 and 50 only')
            userNum = int(input('Please choose again:'))
        else:
            print('This is not the correct number.')
            userNum = int(input('Please choose again:'))
    
else:
    print('Goodbye')