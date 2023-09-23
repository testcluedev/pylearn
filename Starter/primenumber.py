# Write a program that prints all prime numbers in a given range.

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Get the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Print prime numbers in the range
print(f"Prime numbers from {start} to {end} are:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number)

# Efficient Method using square root, better for long range

# def is_prime(num):
#     """Check if a number is prime."""
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# # Get the range from the user
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# # Print prime numbers in the range
# print(f"Prime numbers from {start} to {end} are:")
# for number in range(start, end + 1):
#     if is_prime(number):
#         print(number)
