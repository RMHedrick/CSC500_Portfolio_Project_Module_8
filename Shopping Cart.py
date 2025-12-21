#Item to purchase class with print item cost method

## FIX ME will not be able to update properly - define in the init
class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description
        #self.total_cost = 0.0 #not needed in larger program

#  def print_item_cost(self):  #not needed in larger program
#      self.total_cost = self.item_price * self.item_quantity
#     print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, self.item_quantity, self.item_price, self.total_cost))

#Shopping cart class - Add, remove, modify, quantity, cost, total, unique objects, full description
class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"): #initialize customer name to "none" and current date to "January 1, 2020
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = [] #list for shopping cart items

    def add_item(self, item):
        self.cart_items.append(item)


    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        else:
            print("Item not found in cart. Nothing Removed.")


    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:

                if item_to_modify.item_price != 0.0:
                    item.item_price = item_to_modify.item_price

                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity

                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description

                return
        else:
            print("Item not found in cart. Nothing Modified.")


    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            quantity = item.item_quantity
            total_items += quantity
        return total_items

    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            item_total = item.item_quantity * item.item_price
            total_cost += item_total
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()

        if len(self.cart_items) == 0:
            print("Shopping Cart Is Empty")
        else:
            print("Number of items:", len(self.cart_items))

            for item in self.cart_items:
                total_cost = item.item_quantity * item.item_price
                print("{} {} @ ${:.2f} = ${:.2f}".format(item.item_name, item.item_quantity, item.item_price, total_cost))
            print("Total: ${:.2f}".format(self.get_cost_of_cart()))


    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print("{}: {}".format(item.item_name, item.item_description))

def print_menu(cart):
    user_input = ""

    while user_input != "q":
        print()
        print("Menu")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        user_input = input("Choose an option: ").lower()

        if user_input == "a":
            print("Add item to cart")
            print()
            name = str(input("Enter item name: "))
            description = str(input("Enter item description: "))
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            cart.add_item(ItemToPurchase(item_name = name, item_price = price, item_quantity = quantity, item_description = description))

        elif user_input == "r":
            print("Remove item from cart")
            name = str(input("Enter item name: "))
            cart.remove_item(item_name = name)

        elif user_input == "c":
            print("Modify Item in Cart")
            name = str(input("Enter item name: "))
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            description = str(input("Enter item description: "))
            cart.modify_item(ItemToPurchase(item_name = name, item_price = price, item_quantity = quantity, item_description=description))

        elif user_input == "i":
            print("Output Items' Descriptions")
            print()
            cart.print_descriptions()

        elif user_input == "o":
            print("Output Shopping Cart")
            print()
            cart.print_total()

print("Welcome to our store, let's get started.")
customer_name = input("Enter customer name: ")
current_date = input("Enter current date: ")

print(f"Customer Name: {customer_name}")
print(f"Current Date: {current_date}")

cart = ShoppingCart(customer_name, current_date)
print_menu(cart)













