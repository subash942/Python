
s = "String and String Function"

splitting_s = s.split()

result = ""

for word in splitting_s:
    
    if word not in result:
        result += word + " "

print(result.strip())
