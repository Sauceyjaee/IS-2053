import EmployeeDatabase
def menu():

    employeeName = input('Enter Employee Name: ')
    desiredField = input('Enter Desired Field: ')

    try:
        ans = EmployeeDatabase.companyRegistry(employeeName, desiredField)
        print(ans)
    except KeyError:
        print ('Employee Name or desired criteria not found')
        ans2 = input('Would you like to try again?: ')
        if ans2.lower() == 'yes' or ans2.lower() == 'y':
            menu()
        else:
            print('Bye')
            quit()

if __name__ == "__main__":
    
    print('Welcome to the employee database. Enter employee name and desired info. \n***CASE SENSITIVE***')
    menu()