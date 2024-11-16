from login import user_login
from discount import discount
user_login()
products = [
    {"Name": "Water", "Price": 80.0, "Quantity": 1200},
    {"Name": "Soda", "Price": 130.0, "Quantity": 1200},
    {"Name": "Chips", "Price": 75.0, "Quantity": 1200},
    {"Name": "Bread", "Price": 45.0, "Quantity": 1200},
    {"Name": "Eggs", "Price": 65.0, "Quantity": 1200}
]

table = PrettyTable()
table.field_names = ["Name", "Price", "Quantity"]
for product in products:
    table.add_row([product["Name"], product["Price"], product["Quantity"]])
print(table)
discount()