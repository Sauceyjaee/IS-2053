def introMessage(name):
    print(f'Hello {name}, welcome to the Python Pizza Chooser.')

def takeOrder():
    pizza = input('Which pizza would you like to order? ')
    print(f'One {pizza} pizza coming up!')

def orderAgain():
    userChoice = input('Would you like to order another? ')
    if userChoice == 'yes' or userChoice == 'Yes' or userChoice == 'YES':
        return True
    else:
        return False

def exitMessage(pizzas):
    print(f'Thank you for using my pizza ordering tool.\n' + f'You ordered {pizzas} pizza(s) Thank you for your order')

def main():
    num_of_pizzas = 0
    userName = input('Please enter your name: ')
    introMessage(userName)
    print("\n" + 'You may choose to order a pizza with the following options: ' + 
        '\nCheese, Pepperoni, or Supreme')
    takeOrder()
    num_of_pizzas += 1
    status = orderAgain()
    while status != False:
            num_of_pizzas += 1
            takeOrder()
            status = orderAgain()
    exitMessage(num_of_pizzas)

main()