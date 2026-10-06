"""
Central perk management system
This program allows users to view a cafe menu, search for items, place order, calculate bill
with discounts, and generate receipts.
It demonstrates the use functions, dictionaries, loops, conditional statement, and
docstrings.
"""
MENU = {
    "Coffee"        : 250,
    "Sandwich"      : 450,
    "Pastry"        : 300,
    "Juice"         : 350,
}

def display_menu(sorted_by=None):
    """
    Displays menu options.
    parameter:
    sorted_by: sort by price or name
    Return:
        None
    """
    items = list(MENU.items())

    if sorted_by == "name":
        items.sort()
    elif sorted_by == "price":
        items.sort(key=lambda x: x[1])

    print("\n--- Central Perk Menu ---")
    for item, price in items:
        print(f"{item:15} : LKR {price}")
    print("------------------------")


def search_item():
    """
    Displays menu options, search for items.
    parameter:
    none
    return:
    None
    """
    query = input("Enter item name to search: ").capitalize()
    if query in MENU:
        print(f"Item Found: {query} costs LKR {MENU[query]}")
    else:
        print("Sorry, that item is not available.")


def calculate_bill(order_list):
    """
    Calculates total and discount for each item in order_list
    parameter:
    order_list: list of orders
    return:
    None
    """
    subtotal = sum(item['price'] * item['qty'] for item in order_list)
    discount = 0

    if subtotal > 2000:
        discount = subtotal * 0.10

    final_total = subtotal - discount
    return subtotal, discount, final_total


def generate_receipt(order_list, subtotal, discount, total):
    """
    Generates a receipt with subtotal, discount, and total for each item in order_list
    param order_list:
    param subtotal:
    param discount:
    param total:
    return:
    None
    """
    print("\n========= RECEIPT =========")
    for item in order_list:
        line = f"{item['name']:10} x{item['qty']} @ {item['price']}"
        print(f"{line:<20} LKR {item['price'] * item['qty']}")
    print("-" * 27)
    print(f"Subtotal:       LKR {subtotal}")
    print(f"Discount (10%): LKR {discount}")
    print(f"TOTAL PAYABLE:  LKR {total}")
    print("===========================")


def take_order():
    """
    Allows the user to place an order.
    User can select items from the menu, enter quantities, and finish order.
    return:
    None
    """
    order_list = []
    while True:
        display_menu()
        choice = input("Enter item name to order (or 'done' to finish): ").capitalize()

        if choice == 'Done':
            break

        if choice in MENU:
            try:
                qty = int(input(f"Enter quantity for {choice}: "))
                if qty <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                order_list.append({
                    "name": choice,
                    "price": MENU[choice],
                    "qty": qty
                })
                print(f"{choice} x{qty} added successfully to the order.")
            except ValueError:
                print("Invalid input! Please enter a numerical quantity.")
        else:
            print("Item not found in menu. Please try again.")

    if order_list:
        sub, disc, tot = calculate_bill(order_list)
        generate_receipt(order_list, sub, disc, tot)


def main():
    """
    Main function of the Smart Cafe.
    Displays the main menu and handles user input.
    return:
    None
    """
    while True:
        print("\n--- Smart Cafe Management System ---")
        print("1. View Menu (Normal)")
        print("2. View Menu (Sorted by Price)")
        print("3. Search Item")
        print("4. Place Order")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            display_menu()
        elif choice == '2':
            display_menu(sorted_by="price")
        elif choice == '3':
            search_item()
        elif choice == '4':
            take_order()
        elif choice == '5':
            print("System exiting safely. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
        main()