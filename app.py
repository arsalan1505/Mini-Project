import sys

print('_____________________________________________')
print(' ') # spacers
print('Welcome to the app!')
print(' ')
print('0: Close App   1: Show Products')

# the list of the products. wont be visible unless the option to show them is selected
products = ['Coke', '7up', 'Latte', 'Espresso']


while True:
    print(' ')
    value = int(input("Select a menu option:    "))
    if value == 0:
        sys.exit(0)
    
    elif value == 1:

        print(' ')
        print('Products:  ')
        for n in products:
            print('- ' + n)
        print('  ')
        
        editpro = int(input('2: Enter New Product   3: Update Product   4: Delete Product       '))
        
        if editpro == 2: # new product
            print(' ')
            newpro = input('New Product:   ')
            print(' ')
            products.append(newpro)
            print(products)
            print(' ')
        
        elif editpro == 3: # update product
            
            listindex = int(input((f'1. {products[0]}, 2. {products[1]}, 3. {products[2]}, 4. {products[3]}:     ')))
            newname = input('Enter the new name: ')
            products[listindex - 1] = newname
            print(products)

        elif editpro == 4:
            
            listindex = int(input((f'1. {products[0]}, 2. {products[1]}, 3. {products[2]}, 4. {products[3]}:     ')))
            products.pop(listindex - 1)
            print(products)