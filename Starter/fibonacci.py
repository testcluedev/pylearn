# Write a program that prints the first n numbers in the Fibonacci series.

n = int(input("Please enter a number: "))
def fibonacci(n):
    fib_sequence = [0,1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
print(f"The first {n} numbers in the Fibonacci Series are {fibonacci(n)}")