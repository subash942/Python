
original_list = ['red', 'green', 'white', 'black']

reversed_elements = [original_list[i] for i in range(len(original_list) - 1, -1, -1)]
print("Traversing the said list in reverse order:", ' '.join(reversed_elements))
