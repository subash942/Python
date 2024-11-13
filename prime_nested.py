'''#pattern
for i in range(1,6):
     for j in range(1,i+1):
       print("*",end=" ")
     print()
#1     
num=1
for i in range(1,5):
     for j in range(i):
       print(num,end=" ")
       num+=1
     print()

#2     
for i in range(5,0,-1):
     for j in range(i,0,-1):
      print(j,end=" ")
     print()

#3
n=5
for i in range(1,n+1):
     for j in range(i):
       print(chr(ord('a')+j), end='')
     print()


#4
n=5
for i in range(n):
       print(' ' * (n - i-1) + '*' * (2 * i + 1))'''

for i in range(1,11):
    if i==5 or i==7:
       # break
       continue
    print(i)
