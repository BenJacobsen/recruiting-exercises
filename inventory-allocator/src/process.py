from order import Order
from warehouse import Warehouse
from typing import List

def process(order, warehouses):

    #format inputs to the Order and Warehouse objects
    remainingOrder = Order(order)
    warehouses = [Warehouse(x) for x in warehouses]

    resultSet = []

    for warehouse in warehouses:

        #separates the remainingOrder into what can and cannot be shipped from the current warehouse
        foundOrders, remainingOrder = warehouse.orderAllocate(remainingOrder)

        #if the found order is not empty it should go in the returned list
        if foundOrders.totalItems != 0:
            resultSet.append( { warehouse.name: foundOrders.orderItems } )
        
        #if we have found all the ordered items we should return the resultSet
        if remainingOrder.totalItems == 0:
            return resultSet

    #if we have not returned already then we haven't found all the items in the warehouses, so we should return an empty list
    return []

if __name__ == '__main__':
    print(process( { "apple": 2 }, [ { "name": "ben", "inventory": { "apple": 2 } } ] ))