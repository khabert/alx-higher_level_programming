#!/usr/bin/python3
"""Defines a class_checking function"""

def is_same_class(obj, a_class):
	"""check if an object is an instance of a given class"""
	
	Args:
		obj(any): The object to check
		a_class (type): a class to match the type of obj to
	Return:
		if an obj is exactly an instance of a_class-True.
		otherwise-False
	"""
	if type(obj) = a_class:
		return True
	return False