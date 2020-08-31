#this class holds a dictionary for orders and a count for the total items requested
class Order:

    #creates an Order instance from a dictionary and filters out pairs with values less than 1
    def __init__(self, orderItems={}):
        self.orderItems = {key: value for key, value in orderItems.items() if value > 0}
        self.totalItems = sum(self.orderItems.values())

    #determine equivalence by equal item dictionaries and equal totalItems
    def __eq__(self, other):
        return self.totalItems == other.totalItems and self.orderItems == other.orderItems

    #creates a new key value pair or adds to an existing one if the itemValue is greater than one
    def addItem(self, itemKey: str, itemValue: int):
        if itemValue < 1:
            return
        if itemKey in self.orderItems:
            self.orderItems[itemKey] += itemValue
        else:
            self.orderItems[itemKey] = itemValue
        self.totalItems += itemValue