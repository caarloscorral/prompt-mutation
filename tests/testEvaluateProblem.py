"""
Unit test class for problems evaluation.
"""

import sys
sys.path.append('.')

import unittest
from unittest.mock import Mock
from scripts.data_handling import Problem
from scripts.mutation import evaluate_problem

class TestEvaluateProblem(unittest.TestCase):
	def test_evaluation_successful(self):
		'''
		Test that the evaluation of a mutated problem returns the correct score.
		'''
		client = Mock()
		client.generate_response.return_value = "9.5"
		problem = Problem(original_description="Original description", mutated_description="Mutated description", mutated=True)
		evaluation_template = "Evaluate: {original_statement} vs {mutated_statement}"

		score = evaluate_problem(client=client, problem=problem, evaluation_template=evaluation_template)
		self.assertEqual(score, 9.5)
		self.assertEqual(problem.score, 9.5)
	

	def test_evaluation_without_mutation(self):
		'''
		Test behavior when trying to evaluate an unmutated problem.
		'''
		client = Mock()
		problem = Problem(original_description="Original description")
		evaluation_template = "Evaluate: {original_statement} vs {mutated_statement}"

		with self.assertRaises(ValueError) as context:
			evaluate_problem(client=client, problem=problem, evaluation_template=evaluation_template)

		self.assertIn("Error: Problem statement is not mutated. Cannot evaluate.", str(context.exception))
		self.assertIn("Error", problem.error_logs[-1])


if __name__ == '__main__':
	unittest.main()
