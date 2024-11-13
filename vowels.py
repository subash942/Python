string = "Welcome to python Training"
lower_string = string.lower()
count = 0
vowels = ["a","e","i","o","u"]
vowel_counts = {vowel: 0 for vowel in vowels}
for i in lower_string:
    if i in vowels:
        count +=1
        vowel_counts[i] += 1
print(f"The vowels count is {count}")
print("Vowel counts:")
for vowel, num in vowel_counts.items():
    if num > 0:
        print(f"{vowel}: {num}")
