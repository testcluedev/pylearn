# Write a program that asks the user for a number and then prints whether the number is odd or even.

usernum = int(input("Please enter a Number: "))

# Odd or Even
if usernum % 2 == 0:
    print(f"{usernum} is an Even Number")
else:
    print(f"{usernum} is an Odd Number")