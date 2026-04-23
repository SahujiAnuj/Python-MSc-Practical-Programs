# Program 20: Manual Implementation of Map, Filter, and Reduce

def my_map(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result

def my_filter(func, data):
    result = []
    for item in data:
        if func(item):
            result.append(item)
    return result

def my_reduce(func, data):
    accumulator = data[0]
    for item in data[1:]:
        accumulator = func(accumulator, item)
    return accumulator

# Demonstration
nums = [1, 2, 3, 4, 5]

# Using the functions
squared = my_map(lambda x: x**2, nums)
evens   = my_filter(lambda x: x % 2 == 0, nums)
total   = my_reduce(lambda a, b: a + b, nums)

print("Original List :", nums)
print("Map (Square)  :", squared)
print("Filter (Even) :", evens)
print("Reduce (Sum)  :", total)
