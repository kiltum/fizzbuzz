#!/usr/bin/env python3

def sol1(num):
	a = 0 
	if num % 3 == 0:
		print("Fizz", end ="")
		a = 1
	if num % 5 == 0:
		print("Buzz", end ="")
		a = 1
	if a == 0:
		print(num)
	else:
		print("")


for x in range(1, 101):
	sol1(x)
