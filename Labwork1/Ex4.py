n = int(input("Enter a number: "))
def perfect(n):
    if n < 1:
        return False
    divisor_sum = 0 
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == sum
if perfect(n):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")