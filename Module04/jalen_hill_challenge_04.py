CORRECT_VALUE = 41
userAns = input('Hello, would you like to play a game? \n')

if userAns == 'yes':
    correct = False
    userNum = 0
    attempts = 0
    userNum = int(input(f'Please enter a number between 1 - 50: \n'))
    while correct != True:
        attempts += 1
        if userNum == CORRECT_VALUE:
            print(f'you guessed the correct number.  Congratulations!\n' + f'It took you exactly {attempts} attempts to guess correctly.')
            correct = True
        elif userNum >=37 and userNum <=46:
            print('Your guess was within 5 digits of the correct number.')
            userNum = int(input('Please choose again: \n'))
        elif userNum < 1 or userNum > 50:
            print('Please enter a number between 1 and 50 only')
            userNum = int(input('Please choose again: \n'))
        else:
            print('That is not the correct number.')
            userNum = int(input('Please choose again: \n'))
    
else:
    print('Goodbye')