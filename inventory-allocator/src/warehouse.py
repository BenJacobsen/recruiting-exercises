from order import Order

#this class holds the name of the warehouse and a dictionary for it's inventory
class Warehouse:

    #creates an Order instance from a dictionary and filters out pairs with values less than 1
    def __init__(self, inputDict: dict):
        self.name = inputDict["name"]
        self.inventory = {key: value for key, value in inputDict["inventory"].items() if value > 0}

    #determine equivalence by equal inventory dictionaries and equal names
    def __eq__(self, other):
        return self.name == other.name and self.inventory == other.inventory
    
    #split the inputOrder between what can and cannot be found in inventory, returns (foundOrder, notFoundOrder)
    def orderAllocate(self, inputOrder: Order) -> (Order, Order):
        foundOrder = Order()
        notFoundOrder = Order()

        #iterate over the inputOrder key and value pairs to match against the inventory
        for inputOrderKey, inputOrderValue in inputOrder.orderItems.items():

            #if the item is in the inventory find the min between the requested 
            if inputOrderKey in self.inventory:

                #find the min of the items in inventory and the order amount to determine how many will be shipped from this warehouse
                itemsFound = min(self.inventory[inputOrderKey], inputOrder.orderItems[inputOrderKey])

                #add this min to the foundOrder and add how many of this item will still be needed to notFoundOrder
                foundOrder.addItem(inputOrderKey, itemsFound)
                notFoundOrder.addItem(inputOrderKey, inputOrder.orderItems[inputOrderKey] - itemsFound)

            #if it isn't found in inventory then add it to the order that still needs to be met
            else:
                notFoundOrder.addItem(inputOrderKey, inputOrderValue)

        return (foundOrder, notFoundOrder)