

'''        
#first N even numbers
n = int(input("Enter a number: "))
i = 1
while i<=n:
    print(i*2)
    i+=1
        

#Sum and Average of first N natural numbers
n = int(input("Enter a number: "))
sum = 0
i=1
while i<=n:
    sum += i 
    i+=1
print("Sum is ",sum)
print("Average is ",sum/n)

# program to find the sum of digits of a number

num=int(input('enter a number'))
s=0
temp = num
while num >0:
    rem=num%10
    s=s+rem
    num//=10
    print(f'the sum of {temp} is {s}')


#check whether the given number is a Armstrong or not. ex:153.

n=int(input("Enter any integer value:"))
temp=n
s=0
while(n>0):

    rem=n%10
    s=s+(rem**3)
    n=n//10
if temp==s:
  print(f"The given number  is {temp} a Armstrong number")
else:
  print(f"The given number  is {temp} not a Armstrong number")'''
        

#program to check whether the given number is palindrome
num=int(input('enter the number'))
rev=0
temp=num
while temp>0:
    rem=temp>0
    rev=temp%10
    temp=temp//10
    print(f"The reverse of {num} is {rev}")
    if num==rev:
       print(f"{num} is palindrome number")
    else:
       print(f"[num} is not a palindrome number")

