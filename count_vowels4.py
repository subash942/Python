
s = "Welcome to Python Assignment"

count = 0

vowels = ["a", "e", "i", "o", "u"]

lower_s = s.lower()

for i in lower_s:
    if i in vowels:
        count += 1

print(f"The vowels count is {count}")
