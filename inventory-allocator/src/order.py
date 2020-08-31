#this class holds a dictionary for orders and a count for the total items requested
class Order:

    #creates an Order instance from a dictionary and filters out pairs with values less than 1
    def __init__(self, orderItems={}):
        self.orderItems = {}
        self.totalItems = 0
        for key, value in orderItems.items():
            if value > 0:
                self.orderItems[key] = value
                self.totalItems += value

    #creates a new key value pair or adds to an existing one if the itemValue is greater than one
    def addItem(self, itemKey: str, itemValue: int):
        if itemValue < 1:
            return
        if itemKey in self.orderItems:
            self.orderItems[itemKey] += itemValue
        else:
            self.orderItems[itemKey] = itemValue
        self.totalItems += itemValue