distance = float(input("Enter the distance traveled (in km): "))  
if distance <= 50:
    fare = distance * 8
elif distance <= 100:
    fare = distance * 10  
else:
    fare = distance * 12  
print("Total fare is: Rs.", fare)
