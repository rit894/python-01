#MENU ---------------------  1. TV  2. Washing machine  3. Refrigerator  4. Computer  5. Laptop  6. ipod
# Dictionary of products with price and discount
products = {
    1: ("TV", 20000, 0.10),
    2: ("Washing Machine", 15000, 0.10),
    3: ("Refrigerator", 25000, 0.15),
    4: ("Computer", 30000, 0.15),
    5: ("Laptop", 40000, 0.20),
    6: ("iPod", 5000, 0.20)
}

price_list = []

def show_menu():
    print("\n--- Electronics Shop Menu ---")
    for key, (name, price, discount) in products.items():
        print(f"{key}. {name} (Price: {price}, Discount: {int(discount*100)}%)")
    print("7. Quit")

def calculate_cost(choice):
    name, price, discount = products[choice]
    final_price = price - (price * discount)
    price_list.append(final_price)
    print(f"{name} selected → Final Price after discount: {final_price}")

while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 7:
        break
    elif choice in products:
        calculate_cost(choice)
    else:
        print("Invalid choice, try again.")


total = sum(price_list)
print("\n--- Bill Summary ---")
print("Items purchased:", len(price_list))
print("Total amount to pay:", total)

