# Use list comprehension to create a new list from a given list. 
# For example, create a new list of squares of numbers from a list of numbers.

listinit = []
userint = input("Please input series of numbers to create list: ")

for i in userint.split():
    i = int(i)**2
    listinit.append(i)

print(listinit)