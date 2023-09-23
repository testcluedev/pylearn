# Write a function that takes two integers and returns their greatest common divisor (GCD).

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Test the function
x = 56
y = 98
print(f"The GCD of {x} and {y} is: {gcd(x, y)}")  # Output: The GCD of 56 and 98 is: 14
