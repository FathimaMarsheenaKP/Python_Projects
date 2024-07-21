menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80,
}

print('Welcome to Python Restaurant')
print()

# Print the menu
for item, price in menu.items():
    print(f'{item.capitalize()}: Rs{price}')

print()

order_total = 0

while True:
    item = input('Enter the name of the item you want to order: ').lower()

    if item in menu:
        order_total += menu[item]
        print(f'Your item {item} has been added to your order.')
    else:
        print(f'Ordered item {item} is not available yet!')

    print()
    another_order = input('Do you want to add another item (Yes/No)? ').lower()
    if another_order != 'yes':
        break

print(f'The total amount to pay is Rs{order_total}.')
