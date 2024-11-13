
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
total = 0
for i in test_dict.values():
 total+=i
print(total/len(test_dict))
