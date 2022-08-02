
from tkinter.messagebox import YES


CORRECT_VALUE = 30
userAns = input('Would you like to play a game? ')

if userAns == 'yes':
    userNum = 0
    accumulator = 0
    attempts = 0
    
    while userNum != CORRECT_VALUE:
        attempts += 1
        userNum = int(input('Guess a number between 1 and 50: '))

        if userNum == CORRECT_VALUE:
            print(f'You won!\n' + f'Attempts:{attempts}')
        elif userNum >=25 and userNum <=35:
            print(f'Close\n' + f'Attempts:{attempts}')
        elif userNum < 1 or userNum > 50:
            print(f'Choose a number between 1 and 50 only\n'+ f'Attempts: {attempts}')
    
else:
    print('Goodbye')