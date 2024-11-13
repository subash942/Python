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
       print(f"{num} is not a palindrome number")

