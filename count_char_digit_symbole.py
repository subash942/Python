s = "P@#yn26at^&i5ve"
digits = 0
chars = 0
symbols = 0

for i in s:
    if i.isalpha():
        chars += 1
    elif i.isdigit():
        digits += 1
    elif not i.isspace():
        symbols += 1

print(f"Chars : {chars}")
print(f"Digits : {digits}")
print(f"Symbols : {symbols}")
