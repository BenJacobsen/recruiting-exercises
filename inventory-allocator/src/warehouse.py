from order import Order
class Warehouse:

    name = ""
    inventory = {} #make private?

    def __init__(self, name: str, inventory: dict):
        #check inventory input ex. not less then 0
        self.name = name
        self.inventory = inventory

    def orderAllocate(inputOrder: Order) -> (Order, Order):
        foundOrder = leftoverOrder = Order() # get better name for foundOrder
        for inputOrderKey, inputOrderValue in inputOrder.items():
            if inputOrderKey in self.inventory: #and inventory[inputOrderKey] != 0:
                itemsFound = min(self.inventory[inputOrderKey], inputOrder[inputOrderKey])
                foundOrder.addItem(inputOrderKey, itemsFound)
                leftoverOrder.addItem(inputOrderKey, inputOrder.orderItems[inputOrderKey] - itemsFound)
            else:
                leftoverOrder.addItem(inputOrderKey, inputOrderValue)
        return (foundOrder, leftoverOrder)