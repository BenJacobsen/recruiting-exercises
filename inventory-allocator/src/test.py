import unittest

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
        "BasicOneItemGet",
        { "apple": 1 },
        [ { "name": "owd", "inventory": { "apple": 1 } } ],
        [ { "owd": { "apple": 1 } } ]
    ),
    (
        "BasicMissingItem",
        { "apple": 1 },
        [ { "name": "owd", "inventory": { "apple": 0 } } ],
        []
    ),
    (
        "GetItemsWithMultipleWarehouses",
        { "apple": 10 },
        [ { "name": "owd", "inventory": { "apple": 5 } }, { "name": "dm", "inventory": { "apple": 5 } } ],
        [ { "owd": { "apple": 5 } }, { "dm": { "apple": 5 } } ]
    ),
    (
        "GetItemsFromCheaperWarehouseOnly",
        { "apple": 4 },
        [ { "name": "owd", "inventory": { "apple": 4 } }, { "name": "dm", "inventory": { "apple": 4 } } ],
        [ { "owd": { "apple": 4 } } ]
    ),
    (
        "EmptyOrderShouldReturnEmptyList",
        { "apple": 0 },
        [ { "name": "owd", "inventory": { "apple": 5 } } ],
        [{}]
    ),
    (
        "GetMultipleTypesofItemsFromWarehouses",
        { "apple": 4, "orange": 4 },
        [ { "name": "owd", "inventory": { "apple": 3 } }, { "name": "dm", "inventory": { "orange": 4, "apple": 1 } } ],
        [ { "owd": { "apple": 3 } }, { "dm": { "orange": 4, "apple": 1 } } ]
    ),
    (
        "SkipEmptyWarehouses",
        { "apple": 1 },
        [ { "name": "owd", "inventory": { "apple": 0 } }, { "name": "dm", "inventory": { "apple": 1 } } ],
        [ { "dm": { "apple": 1 } } ]
    ),
]

class TestCollection(unittest.TestCase):
    def run_tests(self):
        for name, order, warehouses, expected in paramsList:
            with self.subTest(msg=name):
                self.assertTrue(compareResults(process(order, warehouses), expected))

if __name__ == '__main__':
    unittest.main()