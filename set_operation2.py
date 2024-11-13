
A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 10}


only_in_A = A - B
print("Elements only in A:", only_in_A)

only_in_B = B - A
print("Elements only in B:", only_in_B)

in_either_not_both = A^B
print("Elements in either A or B but not in both:", in_either_not_both)
