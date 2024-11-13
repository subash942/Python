
s = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

upper = 0
lower = 0
number = 0
special_symbols = 0

for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        number += 1
    elif not i.isspace():
        special_symbols += 1

print(f"Uppercase : {upper}")
print(f"Lowercase : {lower}")
print(f"Special Symbols : {special_symbols}")
print(f"Number Case : {number}")
