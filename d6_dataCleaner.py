# Write function to remove duplicates from list while preserving order:
# ["apple", "banana", "apple"] to ["apple", "banana"]

# ANS: Cannot use sets as they cannot preserve order

fruits = ["apple", "banana", "apple"]
filtered_fruits = list()
for fruit in fruits:
    if fruit not in filtered_fruits:
        filtered_fruits.append(fruit)

for x in filtered_fruits:
    print(x)