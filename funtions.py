Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from functools import reduce
>>> import operator
>>> reduce(operator.add, [1, 2, 3, 4, 5])
15
>>> numbers = [1, 2, 3, 4, 5]
>>> accumulator = operator.add(numbers[0], numbers[1])
>>> for item in numbers[2:]:
	accumulator = operator.add(accumulator, item)

	
>>> accumulator
15
>>> def mul(x,y):
	print('mul {} {}'.format(x,y))
	return x * y
reduce(mul, range(1, 10))
SyntaxError: invalid syntax
>>> reduce(mul, range(1, 10))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    reduce(mul, range(1, 10))
NameError: name 'mul' is not defined
>>> reduce(mul, range(1, 10))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    reduce(mul, range(1, 10))
NameError: name 'mul' is not defined
>>> reduce(mul, [])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    reduce(mul, [])
NameError: name 'mul' is not defined
>>> reduce(mul, [1])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    reduce(mul, [1])
NameError: name 'mul' is not defined
>>> values = [1, 2, 3]
>>> reduce(operator.add, values, 0)
6
>>> values = []
>>> reduce(operator.add, values, 0)
0
>>> values =[1, 2, 3]
>>> reduce(operator.add, values, 0)
6
>>> values = [1, 2, 3]
>>> reduce(operator.mul, values, 1)
6
>>> 