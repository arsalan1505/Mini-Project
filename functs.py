import os

products = ['Coke', '7up', 'Latte', 'Espresso']

#Unix/MacOS
def clear():
    os.system( 'clear' )

def option_1():
    with open('products.txt') as prods:
        for i, line in enumerate(prods):
            print('{0}. {1}'.format(i+1, line))

def option_2():
    print('New Product:')
    newpro = input('-- ')
    products.append(newpro)
    return 

def option_3():
    print(num_list())
    listindex = int(input(('-- ')))
    print('\nEnter the new name:')
    newname = input('-- ')
    products[listindex - 1] = newname
    return

def option_4():
    print(num_list())
    listindex = int(input(('-- ')))
    products.pop(listindex)
    return 

def num_list():
    for number, letter in enumerate(products):
        print(number, letter)
    return

#----------------------------------------------------------------------------------------------------
