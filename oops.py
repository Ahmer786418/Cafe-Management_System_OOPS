class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cafe:
    def __init__(self):
        self.menu = []
        self.order = []

    def add_item_to_menu(self, name, price):
        item = MenuItem(name, price)
        self.menu.append(item)

    def display_menu(self):
        print("\n----- Menu -----")
        for index, item in enumerate(self.menu, start=1):
            print(f"{index}. {item.name} - Rs. {item.price}")
        print("----------------\n")

    def take_order(self):
        while True:
            self.display_menu()
            choice = input("Enter item number to order (or 'done' to finish): ")

            if choice.lower() == 'done':
                self.generate_bill() # Bill show hota hai jab order complete ho jaye
                self.total_billing() # Show total bill with tax after bill
                break

            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(self.menu):
                    self.order.append(self.menu[index])
                    print(f"{self.menu[index].name} added to your order.")
                else:
                    print("Invalid choice.")
            else:
                print("Please enter a valid number.")

    def generate_bill(self):
        print("\n----- Bill -----")
        total = 0
        for item in self.order:
            print(f"{item.name} - Rs. {item.price}")
            total += item.price
        print(f"Total: Rs. {total}")
        print("----------------")

    def total_billing(self):
        if not self.order:
            print("\nNo items ordered!")
            return
        total = sum(item.price for item in self.order)
        tax = total * 0.05
        final_total = total + tax
        print("\n----- Total Bill (with Tax) -----")
        print(f"Subtotal: Rs. {total}")
        print(f"Tax (5%): Rs. {tax:.2f}")
        print(f"Final Total: Rs. {final_total:.2f}")
        print("---------------------------------")


# --- Run the Program ---
cafe = Cafe()
cafe.add_item_to_menu("Tea", 30)
cafe.add_item_to_menu("Coffee", 50)
cafe.add_item_to_menu("Burger", 120)
cafe.add_item_to_menu("Sandwich", 80)

# Start taking orders
print("\nWelcome to the Cafe!")
print("Please place your order:")
cafe.take_order()
