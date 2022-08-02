
def getUserPass():
    userName = input('Create your username: ')
    userPass = input('Create a unique password: ')

    StoredPasswords(userPass)

def StoredPasswords(checkPass):
    PASSWORD_LIST = ('welcome','qwert','abc123','password','password1','iloveyou','princess','123456',
    '12345','123456789','Password123','12345678','696969','111111','F*****','6969','Iwantyou','Babygirl',
    '654321','A******','666666','121212','ZZZZZZ','Ferrari','S*****','H*******','Maddog','Booboo',
    'B*****','Hooters','Tomcat','Badboy','Booger','Matrix','Bigdaddy','P******','232323','4444',
    '00000','Booty','112233','Rosebud','Blonde','Tester','123123','Mustang','Cowboy','changeme')
    
    allClear = 'n'
    while allClear != 'y':
        if checkPass in PASSWORD_LIST:
            print(f'Your password is too common.  Found at index[{PASSWORD_LIST.index(checkPass)}]')
            checkPass = input('Choose Again: ')
        elif checkPass not in PASSWORD_LIST:
            print('That is a strong Password')
            allClear = 'y'
    #if checkPass in PASSWORD_LIST:
     #   return PASSWORD_LIST.index(checkPass)
    #else:
    #    return False

if __name__ == '__main__':
    getUserPass()

