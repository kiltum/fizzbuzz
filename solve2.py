#!/usr/bin/env python3

def switch3(argument , n):
    switcher = {
        0: "Fizz"
    }
    switcher2 = {
        0: "FizzBuzz"
    }

    try:
    	return switcher.get( argument % 3 , argument)
    except:
    	return switcher2.get( n % 3 , argument)


def switch5(argument):
    switcher = {
        0: "Buzz"
    }
    return switcher.get( argument % 5 , argument)


for x in range(1, 101):
	print(switch3(switch5(x) , x))
