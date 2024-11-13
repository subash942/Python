x = int(input("enter first number"))
y = int(input("enter second number"))
z = int(input("enter third number"))
if x>y and x>z:
   print(f"  first number {x} is the largest number")
elif y>x and y>z:
   print(f"second number {y} is the largest number")
else:
   print(f"third number {z} is the largest number")
