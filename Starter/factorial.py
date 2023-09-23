# Write a function that calculates the factorial of a number. 
# The factorial of a number n is the product of all positive integers less than or equal to n.

usernum = int(input("Please enter a number: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"The Factorial of {usernum} is: {factorial(usernum)}")