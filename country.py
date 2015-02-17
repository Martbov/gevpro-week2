#!usr/bin/python3.4

import sys

class Country():
	"""A class with a name attribute and prints "Hello from {country} when you print the object"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "Hello from {}".format(self.name)

print(Country("Holland"))