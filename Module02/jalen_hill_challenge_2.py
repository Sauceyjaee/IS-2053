prompt1 = 'What is your name?' 
prompt2 = 'What is your birth year?'

name = input(prompt1)           #input for user name
birth_year = input(prompt2)         #input for user birth year
current_age = 2022 - int(birth_year)        #calculates user age by subtracting birth year from current year
print('Your name is',name, 'and you are', current_age, 'years old')