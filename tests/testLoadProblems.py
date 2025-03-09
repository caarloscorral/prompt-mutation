"""
Unit test class for problems loading.
"""

import sys
sys.path.append('.')

import unittest
from scripts.data_handling import load_problems

class TestLoadProblems(unittest.TestCase):
	def test_file_not_found(self):
		'''
		Test that loading from a non-existent file raises a FileNotFoundError.
		'''
		with self.assertRaises(FileNotFoundError):
			load_problems(filename='non_existent_file.txt')


	def test_load_problems_successfully(self):
		'''
		Test that loading from a existent file.
		'''
		# Creating a temporary file with problem descriptions and verify loading
		test_filename = 'test_problems.txt'
		with open(test_filename, 'w') as f:
			f.write("Problem 1 description\nProblem 2 description")

		problems = load_problems(filename=test_filename)
		self.assertEqual(len(problems), 2)
		self.assertEqual(problems[0].original_description, "Problem 1 description")
		self.assertEqual(problems[1].original_description, "Problem 2 description")


	# Cleaning-up method to remove temporary files
	def tearDown(self):
		import os
		try:
			os.remove('test_problems.txt')
		except Exception:
			pass


if __name__ == '__main__':
	unittest.main()
