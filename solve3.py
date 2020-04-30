#!/usr/bin/env python3

m = list(range(1,101))

def sol3(num):
	a = 0
	r = "" 
	if num % 3 == 0:
		r = "Fizz"
		a = 1
	if num % 5 == 0:
		r = r + "Buzz"
		a = 1
	if a == 0:
		r = str(num)
	
	return r

def add(num):
	global m
	
	m[num - 1] = sol3(num)
	if num < 100:
		add(num+1)



add(1)
print(*m, sep = "\n")