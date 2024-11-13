def div(x, y):
    if y == 0:
       return "Error: Cannot divide by zero."
    else:     
     return x / y
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
result = div(num1,num2)
print("Division of two numbers is:", result)
