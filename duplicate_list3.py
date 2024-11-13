
numbers = [10,20,30,40,10,20,30,50]

duplicates = []
seen = set()

for num in numbers:

    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.add(num)
print("Duplicate values in the list are:", duplicates)
