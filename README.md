☕ Cafe Management System (Python OOP)
This is a simple Cafe Management System built using Python's Object-Oriented Programming (OOP) principles. It allows users to place orders from a menu, generates a detailed bill, and calculates the final amount including tax.

🚀 Features
📋 Add items to a menu dynamically

📜 Display the menu with item numbers and prices

🛒 Take multiple orders from the user

🧾 Generate a bill with item-wise cost

💰 Calculate total with 5% tax

🔁 Supports continuous ordering until user completes

🧱 Classes Overview
MenuItem
Represents a single menu item.

Attribute	Description
name	Name of the item
price	Price of the item (Rs.)

Cafe
Main class managing menu and orders.

Method	Description
add_item_to_menu()	Adds a MenuItem to the cafe's menu
display_menu()	Displays all available items with their prices
take_order()	Takes input from user to select items and adds them to the order list
generate_bill()	Prints a bill listing all ordered items and subtotal
total_billing()	Calculates and displays final bill including 5% tax

🧑‍💻 How It Works
Predefined menu items (Tea, Coffee, Burger, Sandwich) are added on startup.

User is shown a menu repeatedly until they type done.

Each valid input adds an item to their order.

After typing done, a detailed bill and a tax-inclusive total are shown.

🖼️ Sample Output
markdown
Copy
Edit
Welcome to the Cafe!
Please place your order:

----- Menu -----
1. Tea - Rs. 30
2. Coffee - Rs. 50
3. Burger - Rs. 120
4. Sandwich - Rs. 80
----------------

Enter item number to order (or 'done' to finish): 1
Tea added to your order.

...

----- Bill -----
Tea - Rs. 30
Burger - Rs. 120
Total: Rs. 150
----------------

----- Total Bill (with Tax) -----
Subtotal: Rs. 150
Tax (5%): Rs. 7.50
Final Total: Rs. 157.50
---------------------------------
🛠️ Technologies Used
Python 3.x

OOP Concepts (Classes, Objects, Encapsulation)

📂 How to Run
Ensure Python is installed.

Copy the code into a file named cafe.py.

Run the program:

bash
Copy
Edit
python cafe.py
📌 Notes
Only numeric input for item selection is accepted.

Typing 'done' finalizes the order and prints the bill.
