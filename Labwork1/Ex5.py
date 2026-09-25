colors = ["Blue", "Red", "Green", "Orange", "White"]
c = input("What is your favorite color?: ")
if c in colors:
    a = colors.index(c)
    print("Your color is at index", a, "in my list")
else:
    print("Sorry, I could not find your color")