class Employee():
	"""A class to represent an employee."""
	def __init__(self, first, last, salary):
		"""Initialize the employee."""
		self.first = first.title()
		self.last = last.title()
		self.salary = salary
		
	def give_raise(self, salary_increase = 5000):
		self.salary += salary_increase 
		print("The salary of " + self.first + " " + self.last + " is $" 
		+ str(self.salary)) 

employee1 = Employee('Heurys','Grullon', 70000)
employee1.give_raise(10000)

import unittest

class TestDifferentIncrease(unittest.TestCase):
	def setUp(self):
		self.employee1 = Employee('heurys','grullon', 80000)
		
	def test_normal_amount(self):
		"""Test that 5000 works."""
		self.employee1.give_raise()
		self.assertEqual(self.employee1.salary , 85000)
		
	def test_different_amount(self):
		"""Test that any other value still works."""
		self.employee1.give_raise(15000)
		self.assertEqual(self.employee1.salary , 95000)
			
unittest.main()
			
		
		
