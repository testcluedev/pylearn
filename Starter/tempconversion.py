# Write a program that converts temperature from Celsius to Fahrenheit and vice versa.

tempcelsius = float(input("Please input temperature in Celsius: "))
tempfahrenheit = float(input("Please input temperature in Fahrenheit: "))

def celtofahr(c):
    f = c*1.8 + 32
    return f
def fahrtocel(f):
    c = (f-32)/1.8
    return c

print(f"{tempcelsius} in Fahrenheit is: {round(celtofahr(tempcelsius), 2)}")
print(f"{tempfahrenheit} in Celsius is: {round(fahrtocel(tempfahrenheit), 2)}")