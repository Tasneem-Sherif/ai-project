import random  # For generating a verification code
from prettytable import PrettyTable  # Importing PrettyTable to display tables in the store


# Class to manage user data and authentication
class UserDatabase:
    def __init__(self):
        self.users = {}  # Dictionary to store usernames and passwords

    def check_username(self, username):
        """Checks if the username is unique (not already taken)."""
        return username not in self.users

    def validate_password(self, password):
        """Validates password: Must be at least 10 characters long, 
        contain lowercase, uppercase, and at least one digit."""
        if len(password) < 10:
            return False

        lowercase = uppercase = digit = False

        # Check each character in the password
        for char in password:
            if char.islower():
                lowercase = True
            elif char.isupper():
                uppercase = True
            elif char.isdigit():
                digit = True

        return lowercase and uppercase and digit

    def sign_up(self):
        """Handles user sign-up, ensuring unique username and valid password."""
        while True:
            Fname = input("\nEnter first name: ")
            Lname = input("\nEnter last name: ")
            username = input("\nEnter username: ")
            password = input("\nEnter password: ")

            if self.check_username(username) and self.validate_password(password):
                print("\t\t < Sign-up successful! >")
                self.users[username] = {'password': password, 'Fname': Fname, 'Lname': Lname}
                return username, Fname, Lname
            else:
                print("""\nUsername or password is invalid.
Username should be unique, and password must be at least 10 characters long,
contain both lowercase and uppercase letters, and include digits.""")

    def log_in(self):
        """Handles user login with a two-step authentication using a verification code."""
        while True:
            username = input("\nEnter your username: ")
            if username in self.users:
                password = input("\nEnter your password: ")
                if password == self.users[username]['password']:  # Fixed error
                    verification_code = random.randint(100, 999)  # random 3-digit code
                    print(f"\nVerification code is: {verification_code}")

                    while True:
                        try:
                            entered_code = int(input("\nEnter the verification code: "))
                            if entered_code == verification_code:
                                print("\n\t\t\tWelcome to our application!")
                                user_info = self.users[username]
                                return username, user_info['Fname'], user_info['Lname']
                            else:
                                print("\t\t<Incorrect verification code. Try again>")
                        except ValueError:
                            print("\t\t<Invalid input. Enter a numeric code>")
                else:
                    print("\t\t<Incorrect password. Try again>")
            else:
                print("\t\t<Incorrect username. Try again>")


# Class to manage store functionality
class Store:
    def __init__(self):
        """Initializes store inventory with products, prices, and quantities."""
        self.products = [
            {'name': "water", 'price': 88.0, 'quantity': 2000},
            {'name': "soda", 'price': 160.0, 'quantity': 1200},
            {'name': "chips", 'price': 70.0, 'quantity': 1200},
            {'name': "bread", 'price': 45.0, 'quantity': 1200},
            {'name': "eggs", 'price': 200.0, 'quantity': 1200},
        ]

    def display_products(self):
        """Displays available products in a formatted table."""
        table = PrettyTable()
        table.field_names = ["Name", "Price", "Quantity"]
        for product in self.products:
            table.add_row([product['name'], product['price'], product['quantity']])
        print(table)

    def shopping(self, username, Fname, Lname):
        """Handles shopping process: selecting items, checking stock, applying discount, and finalizing purchase."""
        total_discount_price = 0  
        purchased_items = []  

        while True:
            product_name = input("\nEnter product name (or 'exit' to finish): ").lower()
            if product_name == "exit":
                break  

            matching_products = [p for p in self.products if p['name'].lower() == product_name]
            if not matching_products:
                print("\nProduct not found. Please enter a valid product.")
                continue

            product = matching_products[0]

            try:
                quantity_required = int(input("\nEnter the quantity: "))
                if quantity_required <= 0:
                    print("\nQuantity must be greater than zero.")
                    continue
            except ValueError:
                print("\nInvalid input. Please enter a numeric value.")
                continue

            if quantity_required > product['quantity']:
                print("\nInsufficient quantity. Please enter a lower quantity.")
                continue

            discount = 0.05  
            total_price = product["price"] * quantity_required * (1 - discount)
            total_discount_price += total_price

            product['quantity'] -= quantity_required

            purchased_items.append({
                'name': product['name'],
                'quantity': quantity_required,
                'total_price': total_price  
            })

            print(f"\nTotal price for {quantity_required} {product['name']}(s): {total_price:.2f} LE")
            print("\n<Product added to cart>\n")

        print(f"\nFinal amount to be paid: {total_discount_price:.2f} LE")
        print("\n \t < Thank you for shopping with us! > \t")

        with open("shopping_result.txt", "w") as file:
            file.write("=== Shopping Result ===\n")
            file.write(f"Buyer Name: {Fname} {Lname}\n")
            file.write(f"Total price to be paid: {total_discount_price:.2f} LE\n\n")
            file.write("Purchased Items:\n")
            for item in purchased_items:
                file.write(f"{item['name']} - Quantity: {item['quantity']} - Total price: {item['total_price']:.2f} LE\n")
            
            file.write("\n\t < Remaining Product Quantities >\t\n")
            table = PrettyTable()
            table.field_names = ["Name", "Quantity"]
            for product in self.products:
                table.add_row([product['name'], product['quantity']])
            file.write(str(table))


# Main function to run the program
def main():
    user_db = UserDatabase()
    store = Store()
    print('\t\t\t< Welcome To Play Store Program > ')

    while True:
        print("""
1. Sign up
2. Login
3. Exit
        """)

        user_choice = input("\nSelect the operation you want to perform (1/2/3): ")
        print("\t\t\t========================================")

        if not user_choice.isdigit():
            print("\n<Invalid input, please select the operation correctly>")
            continue

        user_choice = int(user_choice)

        if user_choice == 1:
            print("\n<\t Sign Up \t>")
            user_info = user_db.sign_up()
            if user_info:  
                username, Fname, Lname = user_info 

        elif user_choice == 2:
            print("\n<\t Login  \t>")
            login_result = user_db.log_in()
            if login_result:
                username, Fname, Lname = login_result
                store.display_products()
                store.shopping(username, Fname, Lname)

        elif user_choice == 3:
            print("\n \t < Exiting, Goodbye! \t >")
            break

        else:
            print("\n <Invalid choice, please try again>")


# Entry point of the script
if __name__ == "__main__":
    main()
