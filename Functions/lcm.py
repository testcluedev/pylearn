# Write a function that takes two integers and returns their least common multiple (LCM).

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a,b):
    return abs(a*b) // gcd(a,b)

x = int(input("Please enter first integer: "))
y = int(input("Please enter second integer: "))

print(f"The LCM of {x} and {y} is: {lcm(x, y)}")