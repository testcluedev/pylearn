# Write a function that takes an integer n and prints the multiplication table of that number up to 10.

def multiply(n):
    for i in range(1,11):
        print(f"{n} times {i} is: {n*i}")

userint = int(input("Please enter an integer: "))
multiply(userint)