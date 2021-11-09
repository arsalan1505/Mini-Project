import sys
import os
from functs import option_1 , option_2 , option_3, option_4

def clear():
    os.system('cls')

clear()
print('_____________________________________________')
print(' ') # spacers
print('Welcome to the app!')
print(' ')

# the list of the products. wont be visible unless the option to show them is selected
products = ['Coke', '7up', 'Latte', 'Espresso']


while True:
    print(' ')
    print('Select a menu option:    ')
    print('0: Close App   1: Show Products   2: Show Couriers')
    value = int(input('-- '))
    if value == 0:
        sys.exit(0)
    
    elif value == 1: # done
        clear()
        print('_____________')
        print('Products:  \n')
        print(option_1())
        print('_____________')
        print('\n2: New Product \n3: Update Product \n4: Delete Product \n')
        editpro = int(input('-- '))
        
        # done
        if editpro == 2: # new product
            clear() 
            print(option_2())
            print(input('\nPress Enter'))

        elif editpro == 3: # update product
            clear()
            print(option_3())
            print(input('\nPress Enter'))

        elif editpro == 4:
            clear()
            print(option_4())
            print(input('\nPress Enter'))
    
    # elif value == 2:
