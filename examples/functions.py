def add(a, b):
    return a + b

def findAThird(a):
    return a / 3

def larger(a, b):
    if a > b:
        return a
    else:
        return b

def tryExcept(a, b):
    try:
        return a / b
    except:
        raise Exception("Error: Division by zero")

def largestElement(listOfNumbers):
    return max(listOfNumbers)

def lastElement(listOfNumbers):
    return listOfNumbers[-1]

def indexOfElement(listOfNumbers, element):
    return listOfNumbers.index(element)

def multipleReturns(a, b):
    return a, b


# print all functions
print(add(1, 2))
print(findAThird(3))
print(larger(1, 2))
print(tryExcept(1, 2))
print(largestElement([1, 2, 3, 4, 5]))
print(lastElement([1, 2, 3, 4, 5]))
print(indexOfElement([1, 2, 3, 4, 5], 3))
print(multipleReturns(1, 2))