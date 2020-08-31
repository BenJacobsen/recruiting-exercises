import unittest
import ddt
from parameterized import parameterized

from process import process

#returns true if the warehouse order list has the same warehouses to order from with the same orders, otherwise false

def compareResults(actual, expected):
    if len(actual) != len(expected):
        return False
    
    if len(actual) == 0:
        return True
        
    actual.sort(key= lambda x: list(x.keys())[0])
    expected.sort(key= lambda x: list(x.keys())[0])
    #ignore order of list, so sort based lists on warehouse name and iterate in parallel to compare
    for actualItem, expectedItem in zip(actual, expected):
        
        #this must fit the structure of the result by having one key value pair
        if len(actualItem.items()) != 1 or len(expectedItem.items()) != 1:
            return False

        actualKey = list(actualItem.keys())[0]
        #confirm that the keys and values are matching
        if actualKey not in expectedItem or actualItem[actualKey] != expectedItem[actualKey]:
            return False
    
    return True

paramsList = [
    (
        { "apple": 1 },
        [ { "name": "owd", "inventory": { "apple": 1 } } ],
        [ { "owd": { "apple": 1 } } ]
    ),
    (
        { "apple": 1 },
        [ { "name": "owd", "inventory": { "apple": 0 } } ],
        []
    )
]

class TestCollection(unittest.TestCase):

    def runTest(self):
        for params in paramsList:
            order, warehouses, expected = params
            actual = process(order, warehouses)

            self.assertTrue(compareResults(actual, expected))
"""
class TestCollection(unittest.TestCase):



    def testProcessEmptyWarehouse(self):
        print(process({"apple" : 1}, [{"name": "ben", "inventory": {"apple" : 0}}]))

    def testProcessTwoWarehouses(self):
        print(process({"apple" : 10}, [{"name": "ben", "inventory": {"apple" : 5}}, {"name": "dan", "inventory": {"apple" : 5}}]))
    
    def testProcessTwoWarehousesNotEnough(self):
        print(process({"apple" : 10, "banana" : 1}, [{"name": "ben", "inventory": {"apple" : 5}}, {"name": "dan", "inventory": {"apple" : 5}}]))
"""
