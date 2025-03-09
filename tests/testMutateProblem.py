"""
Unit test class for problems mutation.
"""

import sys
sys.path.append('.')

import unittest
from unittest.mock import Mock
from scripts.data_handling import Problem
from scripts.mutation import mutate_problem

class TestMutateProblem(unittest.TestCase):
	def test_mutation_with_valid_template(self):
		'''
		Test mutation functionality using a valid prompt template.
		'''
		client = Mock()
		client.generate_response.return_value = "Mutated description"
		problem = Problem(original_description="Original description")
		prompt_template = "Rephrase this problem statement: {statement}"
		
		result = mutate_problem(client=client, problem=problem, prompt_template=prompt_template)

		self.assertEqual(result, "Mutated description")
		self.assertTrue(problem.mutated)
		self.assertEqual(problem.mutated_description, "Mutated description")


	def test_mutation_with_invalid_template(self):
		'''
		Test handling of an invalid template without placeholders.
		'''
		client = Mock()
		client.generate_response.return_value = "Mutated description"
		problem = Problem(original_description="Original description")
		prompt_template = "Incorrect Template"

		with self.assertRaises(ValueError) as context:
			mutate_problem(client=client, problem=problem, prompt_template=prompt_template)
		
		self.assertIn("Error: Placeholder '{statement}' not found in the chosen template.", str(context.exception))
		self.assertIn("Error: Placeholder '{statement}' not found in the chosen template.", problem.error_logs[-1])


if __name__ == '__main__':
	unittest.main()
