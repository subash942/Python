num=int(input('enter a value'))
rev_num = 0
while num!= 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10
    print('Reversed number:' +str(rev_num))


