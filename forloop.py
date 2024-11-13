'''# n to 1
n=int(input('enter a value'))
for i in range(n,0,-1): # revers (n,0,-1)
   # for i in range(1,n+1): 
  print(i,end=" ")


# program to display the multiples for 5 from 100 to 5
n = int(input("Enter number: "))
for i in range(n,0,-5):
    print(i)

#program to find the factorial of a number using for loop

n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")


#table
num = int(input("Enter a number to display its multiplication table: "))

for i in range(1, 11):  
    result = num * i  
    print(f"{i} * {num} = {result}")

# convert decimal to binary
n=int(input('Enter the number'))
binary=0
p=10
while n>0:
    r=n%2
    n=n//2
    binary=binary+(r*p)
    p=p*10

print(f'The binary representation is {binary}')'''

#fibonacci series 0 1 1 2 3 5 8
n=int(input('Enter the limit'))
a=0
b=1
c=a+b
print(f'{a} {b} {c}',end=" ")
for i in range(n):
    a=b
    b=c
    c=a+b
    print(f'{c}',end=" ")
