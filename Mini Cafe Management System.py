

# Completed
#  cafe mgmt system to order food based on your taste.


menu = {
    "pizza": 149,
    "burger": 99,
    "coffee": 40,
    "tea" : 15,
    "sandwich" : 70,
    "pasta" : 120,
}

print("\n\t\t\t---Welcome To Ayush Cafe---")
print("Choose item From the Menu :-")
user_choice = input("\npizza : 149\nburger : 99\ncoffee : 40\ntea : 15\nsandwich : 70\npasta : 120\n\nChoose :-")

if user_choice in menu:
    quantity1 = int(input("Enter Quantity: "))
    print (f"Your order {user_choice} - {menu[user_choice]} will be added")
    print("Want to add another item in list: yes/no")
    choice = input()

    if choice == "yes":
        user_choice2 = input("Enter Item: ")

        if user_choice2 in menu:
            quantity2 = int(input("Enter Quantity: "))
            print(f"item {user_choice2} - {menu[user_choice]} will be added")
            total = (menu[user_choice] * quantity1) + (menu[user_choice2] * quantity2)
            print(f"Total amount you have to pay : {total}.00")
        else:
            print("Sorry we couldn't find any item related to ",user_choice)
    else:
        print("hmmmm...")
        one_order = menu[user_choice] * quantity1
        print(f"Total amount you have to pay : {one_order}.00")

else:
    print("Sorry we couldn't find any item related to ",user_choice)

print("\n--- Your Bill ---")
print(f"Total Amount: ₹{total}")
print("Thanks for visiting Ayush Cafe!")

print("Have a Beautiful Day... ")
