Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def print_args(arg1, arg2, *args):
	print(arg1)
	print(arg2)
	print(args)

	
>>> t = (11, 12,13, 14)
>>> print_args(*t)
11
12
(13, 14)
>>> def color(red, green, blue, **kwargs):
	print ("r =", red)
	print("g =", green)
	print("b =", blue)
	print(kwargs)

	
>>> k = {'red':21, 'green' :68, 'blue':120, 'alpha' :52
     color(**k)
     
SyntaxError: invalid syntax
>>> k = {'red':21, 'green' :68, 'blue':120, 'alpha' :52
     color(**k)
     
SyntaxError: invalid syntax
>>> 
>>> k = {'red':21, 'green' :68, 'blue':120, 'alpha' :52}
>>> color(**k)
r = 21
g = 68
b = 120
{'alpha': 52}
>>> k = dict(red=21, green=68, blue=120, alpha=52)
>>> 