Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def tag(name, **kwargs):
	print(name)
	print(kwargs)
	print(type(kwargs))

	
>>> tag('img', src="Monet.jpg", alt="Sunrise by Claude Monet", border=1)
img
{'src': 'Monet.jpg', 'alt': 'Sunrise by Claude Monet', 'border': 1}
<class 'dict'>
>>> def tag(name, **attributes):
	results = '<' + name
	for key, value in attributes.items():
		results += ' {k}= "{v}"'.format(k=key, v=str(value))
	results += 'v'
	return results

>>> tag('img',src="Monet.jpg", alt="Sunrise by Claude Monet", border=1)
'<img src= "Monet.jpg" alt= "Sunrise by Claude Monet" border= "1"v'
>>> def print_args(arg1, arg2, *args):
	print(arg1)
	print(arg2)
	print(args)

	
>>> print_args(1,2,3,4,5)
1
2
(3, 4, 5)
>>> def name_tag(first_name,*,tittle='')
SyntaxError: invalid syntax
>>> def name_tag(first_name,*,tittle=''):
	print(title, first_name, last_name)

	
>>> name_tag('Judy','Spudmeyer', title='Galactic commander')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name_tag('Judy','Spudmeyer', title='Galactic commander')
TypeError: name_tag() got an unexpected keyword argument 'title'
>>> def print_args(arg1,arg2,*args, kwarg1,kwarg2, **kwargs):
	print(arg1)
	print(arg2)
	print(args)
	print(kwarg1)
	print(kwarg2)
	print(kwargs)

	
>>> print_args(1,2,3, 4,5, kwarg1=6, kwarg2=7, kwarg3=8, kwarg4=9)
1
2
(3, 4, 5)
6
7
{'kwarg3': 8, 'kwarg4': 9}
>>> def print_args(arg1, arg2,  *args, kwarg1,kwarg2, **kwargs, kwargs99):
	
SyntaxError: invalid syntax
>>> 