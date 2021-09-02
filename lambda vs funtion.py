Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> scientists = ['Marie Curie', 'Albert Einstein', 'Rosalind Franklin', 'Niels Bohr', 'Dian Fossey', 'Isaac Newton','Grace Hopper','Charles Darwin', 'Lise Meintner']
>>> sorted(scientists, key= lambda name: name.split()[-1])
['Niels Bohr', 'Marie Curie', 'Charles Darwin', 'Albert Einstein', 'Dian Fossey', 'Rosalind Franklin', 'Grace Hopper', 'Lise Meintner', 'Isaac Newton']
>>> Last_name = lambda name: name.split()[-1]
>>> last_name
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    last_name
NameError: name 'last_name' is not defined
>>> Last_name
<function <lambda> at 0x000002317FD0B1F0>
>>> Last_name("Nikola Tesla")
'Tesla'
>>> def first_name(name):
	return name.split()[0]
