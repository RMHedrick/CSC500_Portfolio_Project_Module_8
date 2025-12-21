#Item to purchase class with print item cost method

## FIX ME will not be able to update properly - define in the init
class ItemToPurchase:
    def __init__(self):
        self.total_cost = 0.0 #float
        self.item_name = "none" #string
        self.item_price = 0.0 #float
        self.item_quantity = 0 #integer

    def print_item_cost(self):
        self.total_cost = self.item_price * self.item_quantity
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, self.item_quantity, self.item_price, self.total_cost))

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

                if item_to_modify.item_name != "none":
                    item.item_name = item_to_modify.item_name

                if item_to_modify.item_price != 0.0:
                    item.item_price = item_to_modify.item_price

                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity

                return
        else:
            print("Item not found in cart. Nothing Modified.")



    def get_num_items_in_cart(self):

    def get_cost_of_cart(self):

    def print_total(self):

    def print_descriptions(self):

