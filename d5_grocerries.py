# Grocery List Manager
# Create empty list groceries
# Add 3 items
# Remove the second item

grocerries = []
item_limit = int(input("How many items you want to order: "))
while True:
    x = 0
    while x < item_limit:
        item = input("Please enter item: ")
        grocerries.append(item)
        print(f'{item} has been added to your cart.')
        x+=1
    else:
        print("All of your items have been added to the cart successfully!")
        x = int(input("Enter 1 to add more items, 2 to proceed further: "))
        if x == 2:
            break
        elif x == 1:
            x = 0
            item_limit = int(input("How many more items you want to add: "))
        else:
            ("Invalid Response!")
while True:
    x = int(input("Press 1 to remove any item from the list or 2 to place final order: "))
    
    if x == 1:
        item = input("Please enter the item you want to remove: ")
        grocerries.remove(item)
        print(f"{item} has been removed from the list. Your new list is: ")
        for item in grocerries:
            print(item)


    elif x == 2:
        print("Your order has been placed. Thanks! \n Your order: ")
        for item in grocerries:
            print(item)
        break

