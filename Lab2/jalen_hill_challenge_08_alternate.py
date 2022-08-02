
MIN_PASS_LEN = 8
#Get user name and password, then pass the password to the checkPassword function
def getUserPass():
    userName = input('Create your username: ')
    userPass = input('Create a unique password: ')
    
    checkPassword(userPass)
    
#check passwords for uppercase,lowercase,digit,length, special, and restricted characters
def checkPassword(checkPass):
    #Lists of Passwords
    password_list = ['welcome','qwert','abc123','password','password1','iloveyou','princess','123456','Loser','Capper',
    '12345','123456789','Password123','12345678','696969','111111','F*****','6969','Iwantyou','Babygirl',
    '654321','A******','666666','121212','ZZZZZZ','Ferrari','S*****','H*******','Maddog','Booboo',
    'B*****','Hooters','Tomcat','Badboy','Booger','Matrix','Bigdaddy','P******','232323','4444',
    '00000','Booty','112233','Rosebud','Blonde','Tester','123123','Mustang','Cowboy','changeme']
    #Special and Restricted characters as specified in the instructions
    specialChar = ('@','!', '%', '(',')', '*', '&', '^')
    restrictedChar = ('#','$','_','-','+','=')
    #Initialized boolean variables for requirement statuses
    hasUpper = False
    hasLower = False
    hasDigit = False
    hasSpecialChar = False
    hasRestrictedChar = True
    hasMinLen = False

    allClear = 'n'
    while allClear != 'y':
        #This if/elif structure checks to see if a pw is in the list. If so, continually asks user to create an unused pw.
        #If not begins to see if it is a valid new password.
        if checkPass in password_list:
            print(f'Your password is too common.  Found at index[{password_list.index(checkPass)}]')
            checkPass = input('Choose Again: ')
        elif checkPass not in password_list:
            #This loop uses if statements to iterate through the password's characters, and checks each character to see of it meets a requirement
            for char in checkPass:
                if len(checkPass) >= MIN_PASS_LEN:
                    hasMinLen = True
                if char.isupper() == True:
                    hasUpper = True
                if char.islower() == True:
                    hasLower = True
                if char.isdigit() == True:
                    hasDigit = True

                if char in specialChar:
                        hasSpecialChar = True
                if char in restrictedChar:
                    hasRestrictedChar = False
                
            
            #This statement checks to see if all requirements are met. Is so, stores the password in the password list and lets the user know its strong, if not runs getUserPass again, causing program to run again until a strong password is generated
            if hasUpper & hasLower & hasDigit & hasSpecialChar & hasRestrictedChar & hasMinLen:
                print('That is a strong Password')
                password_list.append(checkPass)
                print(password_list)
            else:
                print(f'This is not a strong password.\n' + f'Passwords must: \n' + 'Be 8 or more characters long with an upper or lowercase letter \n' + f'Contain a special character:\n{specialChar}\n' + f'Restricted characters: {restrictedChar}')
                getUserPass()

            allClear = 'y'
            

if __name__ == '__main__':
    getUserPass()
