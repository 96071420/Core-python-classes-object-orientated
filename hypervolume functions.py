Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hypervolume(*args):
	print(args)
	print(type(args))

	
>>> hypervolume(3,4)
(3, 4)
<class 'tuple'>
>>> def hypervolume(*lengths):
	i = iter(lengths)
	v = next(i)
	for length in i:
		v *=length
	return v

>>> hypervolume(2,4)
8
>>> hypervolume(2,4, 6)
48
>>> hypervolume(2, 4,6,8)
384
>>> hypervolume(1)
1
>>> hypervolume()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    hypervolume()
  File "<pyshell#11>", line 3, in hypervolume
    v = next(i)
StopIteration
>>> def hypervolume(length, *lengths):
	v = length
	for item in lengths:
		v *= item
	return v

>>> hypervolume(3,5,7,9)
945
>>> hypervolume(3,5,7)
105
>>> hypervolume(3,5)
15
>>> hypervolume(3)
3
>>> hypervolume()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    hypervolume()
TypeError: hypervolume() missing 1 required positional argument: 'length'
>>> 