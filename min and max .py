
def get_numbers(count):
    return [float(input(f"Enter number {i + 1}: ")) for i in range(count)]
def display_results(numbers):
    print("The numbers are:", numbers)
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
numbers = get_numbers(5)
display_results(numbers)
