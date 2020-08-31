
## Solution

For this problem I use the process() found in process.py to preform the inventory distribution. I also created the Order and Warehouse classes to internally represent the data structures passed as arguments. These classes were used to abstract away corner cases from process() (ex. recieving an empty order) and to better organize functionality by using class methods (ex. Warehouse.orderAllocate()).

At a high level, process() solves this problem by iterating through the warehouses inventories starting from the least expensive and returning order items that the warehouse can supply while removing these items from the order itself. It terminates when it either runs out of order items or runs out of warehouses, returning the warehouse orders or an empty list respectively.

## Testing

Tests for process() can be found in test.py . Before running be sure that python3 and the unittest library is installed. 
Run:
`cd ../recruiting-exercises/inventory-allocator/src`
`py test.py -v`

Test cases are parameterized and stored in  `paramsList` in test.py, and each one runs as a subTest to test_process(). This means that a successful run will appear as:
`test_process (__main__.TestCollection) ... ok`
If an error occurs in the run it will appear as:
`FAIL: test_process (__main__.TestCollection) [TestName]`
where TestName is the first argument in each parameter set in paramList.  

## Problem

The problem is compute the best way an order can be shipped (called shipments) given inventory across a set of warehouses (called inventory distribution). 

Your task is to implement a function that will to produce the cheapest shipment.

The first input will be an order: a map of items that are being ordered and how many of them are ordered. For example an order of apples, bananas and oranges of 5 units each will be 

`{ apple: 5, banana: 5, orange: 5 }`

The second input will be a list of object with warehouse name and inventory amounts (inventory distribution) for these items. For example, the inventory across two warehouses called owd and dm for apples, bananas and oranges could look like

`[ 
    {
    	name: owd,
    	inventory: { apple: 5, orange: 10 }
    }, 
    {
    	name: dm:,
    	inventory: { banana: 5, orange: 10 } 
    }
]`

You can assume that the list of warehouses is pre-sorted based on cost. The first warehouse will be less expensive to ship from than the second warehouse.

You can use any language of your choice to write the solution (internally we use Typescript/Javascript, Python, and some Java). Please write unit tests with your code, a few are mentioned below, but these are not comprehensive. Fork the repository and put your solution inside of the src directory and include a way to run your tests!

## Examples

### Order can be shipped using one warehouse

Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]`  
Output: `[{ owd: { apple: 1 } }]`

### Order can be shipped using multiple warehouses

Input: `{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]`  
Output: `[{ dm: { apple: 5 }}, { owd: { apple: 5 } }]`

### Order cannot be shipped because there is not enough inventory

Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]`  
Output: `[]`

Input: `{ apple: 2 }, [{ name: owd, inventory: { apple: 1 } }]`  
Output: `[]`

## FAQs
**If an order can be completely shipped from one warehouse or shipped from multiple warehouses, which option is cheaper?**
  We can assume that shipping out of one warehouse is cheaper than shipping from multiple warehouses.

## What are we looking for

We'll evaluate your code via the following guidelines in no particular order:

1. **Readability**: naming, spacing, consistency
2. **Correctness**: is the solution correct and does it solve the problem
1. **Test Code Quality**: Is the test code comperehensive and covering all cases.
1. **Tool/Language mastery**: is the code using up to date syntax and techniques. 
