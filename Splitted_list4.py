
list = [1, 1, 2, 3, 4, 4, 5, 1]

length_of_first_part = 3

first_part = list[:length_of_first_part]  
second_part = list[length_of_first_part:]  

print("Original list:", list)
print("Length of the first part of the list:", length_of_first_part)
print("Splitted the said list into two parts:", (first_part, second_part))
