from prettytable import PrettyTable

class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability

inventory = []
sales_record = []
current_user = None

def add_snack():
    snack_id = input("Enter snack ID: ")
    name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    availability = input("Is the snack available? (yes/no): ")
    snack = Snack(snack_id, name, price, availability)
    inventory.append(snack)
    print("Snack added to inventory successfully.")

def remove_snack():
    snack_id = input("Enter snack ID to remove: ")
    for snack in inventory:
        if snack.snack_id == snack_id:
            inventory.remove(snack)
            print("Snack removed from inventory successfully.")
            return
    print("Snack not found in inventory.")

def update_availability():
    snack_id = input("Enter snack ID to update availability: ")
    availability = input("Is the snack available? (yes/no): ")
    for snack in inventory:
        if snack.snack_id == snack_id:
            snack.availability = availability
            print("Snack availability updated successfully.")
            return
    print("Snack not found in inventory.")

total_sale = 0.0

def make_sale():
    snack_id = input("Enter snack ID sold: ")
    for snack in inventory:
        if snack.snack_id == snack_id:
            if snack.availability == "yes":
                sales_record.append(snack)
                inventory.remove(snack)
                print("Sale recorded successfully.")
                global total_sale
                total_sale += snack.price  # Add the price of the sold snack to the total sale
                print("Total Sale: $", total_sale)
                return
            else:
                print("Snack is not available for sale.")
                return
    print("Snack not found in inventory.")


def display_inventory():
    table = PrettyTable()
    table.field_names = ["Snack ID", "Snack Name", "Price", "Availability"]
    for snack in inventory:
        table.add_row([snack.snack_id, snack.name, snack.price, snack.availability])
    print(table)

def display_sales_records():
    table = PrettyTable()
    table.field_names = ["Snack ID", "Snack Name", "Price"]
    for snack in sales_record:
        table.add_row([snack.snack_id, snack.name, snack.price])
    print(table)

def login():
    global current_user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Add your authentication logic here
    # Example: check against a predefined username and password
    if username == "admin" and password == "password":
        current_user = username
        print("Login successful.")
    else:
        print("Invalid credentials. Login failed.")

def logout():
    global current_user
    current_user = None
    print("Logged out successfully.")

def filter_by_price():
    min_price = float(input("Enter minimum price: "))
    max_price = float(input("Enter maximum price: "))

    filtered_snacks = [snack for snack in inventory if min_price <= snack.price <= max_price]
    if not filtered_snacks:
        print("No snacks found within the given price range.")
    else:
        table = PrettyTable()
        table.field_names = ["Snack ID", "Snack Name", "Price", "Availability"]
        for snack in filtered_snacks:
            table.add_row([snack.snack_id, snack.name, snack.price, snack.availability])
        print(table)

def show_menu():
    print("Mumbai Munchies Canteen Management System")
    print("1. Add Snack to Inventory")
    print("2. Remove Snack from Inventory")
    print("3. Update Snack Availability")
    print("4. product Sale")
    print("5. Display Snack Inventory")
    print("6. Display Sales Records")
    print("7. Login")
    print("8. Logout")
    print("9. Filter Snacks by Price")
    print("10. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            add_snack()
        elif choice == "2":
            remove_snack()
        elif choice == "3":
            update_availability()
        elif choice == "4":
            make_sale()
        elif choice == "5":
            display_inventory()
        elif choice == "6":
            display_sales_records()
        elif choice == "7":
            if current_user:
                print("Already logged in.")
            else:
                login()
        elif choice == "8":
            if current_user:
                logout()
            else:
                print("No user is currently logged in.")
        elif choice == "9":
            filter_by_price()
        elif choice == "10":
            print("Thank you for using Mumbai Munchies Canteen Management System.")
            break
        else:
            print("Invalid choice. Please try again with a valid option.")

if __name__ == "__main__":
    main()
