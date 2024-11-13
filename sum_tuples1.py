
tuples_list = [(1, 2), (3, 4), (5, 6)]

total_sum = sum(sum(t) for t in tuples_list)

print("The sum of the numbers in the given tuples is:", total_sum)
