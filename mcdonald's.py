import time

# Welcome message
print("Hello, Welcome to McDonald's...!")
time.sleep(1)
print("--" * 30)
print("Browse our menu and let us know what delicious treat you'd like to order today!")
print("--" * 30)

# Food menu 
food_menu = {
    1: {"category": "Burger", "items": {1: ("Big Mac", 99), 2: ("McDouble", 199), 3: ("Cheeseburger", 149), 
                                        4: ("Double Cheeseburger", 199), 5: ("Hamburger", 249)}},
    2: {"category": "Beverages", "items": {1: ("Coca-Cola", 99), 2: ("Sprite", 99), 3: ("Fanta", 79), 
                                           4: ("Dr Pepper", 109), 5: ("Diet Coke", 129)}},
    3: {"category": "Chicken & Sandwiches", "items": {1: ("Crispy Chicken Sandwich", 149), 2: ("Spicy CCS", 199), 
                                                      3: ("Deluxe CCS", 249), 4: ("Chicken McNuggets", 399)}},
    4: {"category": "Breakfast", "items": {1: ("Egg McMuffin", 99), 2: ("Sausage McMuffin", 119), 
                                           3: ("Sausage McGriddles", 149), 4: ("Big Breakfast", 199)}},
    5: {"category": "Desserts & Shakes", "items": {1: ("Hot Fudge Sundae", 99), 2: ("McFlurry with M&Ms", 119), 
                                                   3: ("Kiddie Cone", 149), 4: ("Hot Caramel Sundae", 199)}},
    0: {"category": "Exit", "items": {}}
}

order_list = []  # Stores selected items
total_bill = 0   # Stores total bill amount

# Display main menu
def display_menu():
    print("\nChoose a category:")
    for key, value in food_menu.items():
        print(f"Enter {key} for {value['category']}")
    print("--" * 30)

# To take order from user
def take_order():
    global total_bill
    while True:
        display_menu()
        try:
            choice = int(input("Please type the category number you want to order from: "))
            if choice == 0:
                print("\nThank you for visiting McDonald's!")
                break  # Exit the ordering system

            if choice not in food_menu:
                print("Invalid choice! Please select a valid category.")
                continue

            category = food_menu[choice]
            print(f"\nYou selected: {category['category']}")
            print("--" * 30)

            # Display items from the selected category
            for item_num, (item_name, item_price) in category["items"].items():
                print(f"Enter {item_num} for {item_name} - ₹{item_price}")
            print("Enter 0 to go back")
            print("--" * 30)

            while True:
                item_choice = int(input("Select an item: "))
                if item_choice == 0:
                    break  # Go back to category menu

                if item_choice not in category["items"]:
                    print("Invalid item! Please try again.")
                    continue

                item_name, item_price = category["items"][item_choice]
                quantity = int(input(f"How many {item_name}s would you like to order? "))

                # Add item to order list
                order_list.append((item_name, item_price, quantity))
                total_bill += item_price * quantity

                print(f"{quantity}x {item_name} added to your order!")
                print("--" * 30)

                more_items = input("Do you want to add more items from this category? (y/n): ").lower()
                if more_items != 'y':
                    break

        except ValueError:
            print("Invalid input! Please enter a number.")

# Displays final bill
def display_bill():
    if not order_list:
        print("\nYou did not place any order. Thank you for visiting McDonald's!")
        return

    print("\nYour Order Summary:")
    print("--" * 30)
    print("{:<25} {:<10} {:<10} {:<10}".format("Item", "Price", "Qty", "Total"))
    print("--" * 30)

    for item, price, qty in order_list:
        print(f"{item:<25} ₹{price:<10} {qty:<10} ₹{price * qty:<10}")

    print("--" * 30)
    print(f"Total Bill: ₹{total_bill}")
    print("--" * 30)
    print("Thank you for ordering at McDonald's! Enjoy your meal!")

# Run the ordering system
take_order()
display_bill()
