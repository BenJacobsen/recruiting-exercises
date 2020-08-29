class Order:

    orderItems = {} #make private?
    totalItems = 0

    def __init__(self, orderItems: dict):
         #check inventory input ex. not less then 0
        self.orderItems = orderItems
        for key, value in orderItems.items():
            self.totalItems += value

    def addItem(itemKey: str, itemValue: int):
        if itemValue < 1:
            return
        if itemKey in orderItems:
            orderItems[itemKey] += itemValue
        else:
            orderItems[itemKey] = itemValue
        totalItems += itemValue