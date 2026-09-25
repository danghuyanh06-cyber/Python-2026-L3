def get_divisors(n):
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        return [i for i in range(1, n + 1) if n % i == 0]
number = int(input("Enter a number: "))
print("get_divisors", get_divisors(number))
