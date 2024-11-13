
numbers = [1, 2,4,8,6,11,33,77]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")
