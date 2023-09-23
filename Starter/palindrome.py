# Write a program that checks whether a given word or phrase is a palindrome.
# A palindrome is a word or phrase that reads the same backward as forward.

# How to solve this? 
# step 1 - An example palindrome is 'Civic', first we convert the string into lowercase.
# step 2 - then we reverse the string
# step 3 - then we compare original string with reversed string, if they are equal then original
# string is a 'Palindrome' otherwise it is not.

userstr = input("Please enter a string: ")
lowcasestr = userstr.lower()
revstring = lowcasestr[::-1]

if revstring == lowcasestr:
    print(f"The word {userstr} is a Palindrome")
else:
    print(f"The word {userstr} is not a Palindrome")
