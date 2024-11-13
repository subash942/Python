import sys
print("Enter your choice")
print("1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Exit")
choice=int(input())
if choice==1:
    print('Enter two numbers')
    a=int(input())
    b=int(input())
    print(f'The sum is {a+b}')

elif choice==2:
    print('Enter two numbers')
    a=int(input())
    b=int(input())
    print(f'The difference is {a-b}')

elif choice==3:
    print('Enter two numbers')
    a=int(input())
    b=int(input())
    print(f'The product is {a*b}')

elif choice==4:
    print('Enter two numbers')
    a=int(input())
    b=int(input())
    print(f'The qoutient is {a/b}')

elif choice==5:
    sys.exit(0)

else:
    print("Invalid choice!!!!")
