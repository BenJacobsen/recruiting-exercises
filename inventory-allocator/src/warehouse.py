from order import Order

class Warehouse:

    #creates an Order instance from a dictionary and filters out pairs with values less than 1
    def __init__(self, name: str, inventory: dict):
        self.name = name
        self.inventory = {}
        for key, value in inventory.items():
            if value > 0:
                self.inventory[key] = value

    def orderAllocate(self, inputOrder: Order) -> (Order, Order):
        foundOrder = Order()
        leftoverOrder = Order()

        #iterate over the inputOrder key and value pairs to match against the inventory
        for inputOrderKey, inputOrderValue in inputOrder.orderItems.items():

            #if the item is in the inventory find the min between the requested 
            if inputOrderKey in self.inventory:

                #find the min of the items in inventory and the order amount to determine how many will be shipped from this warehouse
                itemsFound = min(self.inventory[inputOrderKey], inputOrder.orderItems[inputOrderKey])

                #add this min to the foundOrder and add how many of this item will still be needed to leftoverOrder
                foundOrder.addItem(inputOrderKey, itemsFound)
                leftoverOrder.addItem(inputOrderKey, inputOrder.orderItems[inputOrderKey] - itemsFound)

            #if it isn't found in inventory then add it to the order that still needs to be met
            else:
                leftoverOrder.addItem(inputOrderKey, inputOrderValue)

        return (foundOrder, leftoverOrder)