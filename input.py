#!/bin/python3

x = float(input("Give me a number: "))
o = input("Give me an operator: ")
y = float(input("Give me yet another number: "))

if o == "+":
	print(x + y)
elif o == "-":
	print(x - y)
elif o == "/":
	print(x / y)
elif o == "*":
	print(x * y)
elif o == "**" or o == "^":
	print(x ** y)
else:
	print("Unknown Operator.")



