def extract_even(n):
    return [x for x in n if x % 2 == 0]

numbers = [1, 4, 5, -1, 10]
print("extract_even", extract_even(numbers))