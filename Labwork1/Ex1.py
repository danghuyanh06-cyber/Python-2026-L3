#ex1
import math
radius = float(input("Enter circle radius: "))
circle_area = math.pi * radius ** 2
print("Circle area:", circle_area);
#ex2
Celsius = float(input("Enter temperature in Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32
print(f"{int(Celsius)} (C) =  {Fahrenheit} (F)"); 
#ex3
n = int(input("Enter a number: "))
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
if prime(n):
    print(n, "is a prime number")
else:
    print(n,"is Not a prime number")





