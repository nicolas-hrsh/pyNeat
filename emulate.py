# A good function to traverse any iterable and return a:
#              -Tuple in format (index, value)
#              -The iterable can be a list, set, dict, tuple, String, etc.


fruits = ['apple', 'banana', 'cherry']

for index, value in enumerate(fruits):
    print(f"The index of the fruit {value} is {index}")