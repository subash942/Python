s = 0
while True:
    num = int(input('Enter a number (0 to stop): '))
    if num == 0:
        break  
    temp = num
    while num > 0:
        rem = num % 10
        s += rem       
        num //= 10     
print(f'The sum of the digits is: {s}')
