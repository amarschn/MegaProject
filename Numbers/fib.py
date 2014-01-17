# Author: Drew Marschner
# Date: 1/16/2014

# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

'''
Returns fibonacci sequence in list form to a specified number
'''
def fibonacci(end):
	numbers = [0, 1]
	while len(numbers) < end:
		numbers.append(numbers[-1] + numbers[-2])
	return numbers


'''
Standard recursive algorithm that returns fibonacci number at the Nth spot
'''
def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


