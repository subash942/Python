string = "To change the overall look of your document. To change the look available in the gallery"
splitting_string = string.split()
unique_words = []
for i in splitting_string:
    if i not in unique_words:
        unique_words.append(i)     
for i in unique_words:
    print(f"{i}: {splitting_string.count(i)}")
