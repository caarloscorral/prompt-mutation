"""
Unit test class for argument parsing.
"""

import sys
sys.path.append('.')

import unittest
import argparse
from unittest.mock import patch
from scripts.arg_parsing import parse_arguments

class TestArgumentParsing(unittest.TestCase):
	@patch('scripts.arg_parsing.argparse.ArgumentParser.parse_args')
	def test_default_values(self, mock_args):
		'''
		Test that default argument values are correctly parsed
		'''
		# Mocking default arguments as if they are parsed
		mock_args.return_value = argparse.Namespace(
			filepath='problems/problems.txt',
			seed=42,
			agent='gpt-4o',
			num_rounds=5,
			num_problems=2,
			topk_problems=2,
			mutate_on_start='Y'
		)
		
		# Simulating command line argument parsing and check default values
		args = parse_arguments()
		self.assertEqual(args.filepath, 'problems/problems.txt')
		self.assertEqual(args.seed, 42)
		self.assertEqual(args.agent, 'gpt-4o')
		self.assertEqual(args.num_rounds, 5)
		self.assertEqual(args.num_problems, 2)
		self.assertEqual(args.topk_problems, 2)
		self.assertEqual(args.mutate_on_start, 'Y')


	@patch('scripts.arg_parsing.argparse.ArgumentParser.parse_args')
	def test_with_custom_values(self, mock_args):
		'''
		Test that custom argument values are correctly parsed.
		'''
		# Mocking provided command line arguments for custom values
		mock_args.return_value = argparse.Namespace(
			filepath='test_path.txt',
			seed=123,
			agent='test_agent',
			num_rounds=10,
			num_problems=5,
			topk_problems=3,
			mutate_on_start='N'
		)

		args = parse_arguments()
		self.assertEqual(args.filepath, 'test_path.txt')
		self.assertEqual(args.seed, 123)
		self.assertEqual(args.agent, 'test_agent')
		self.assertEqual(args.num_rounds, 10)
		self.assertEqual(args.num_problems, 5)
		self.assertEqual(args.topk_problems, 3)
		self.assertEqual(args.mutate_on_start, 'N')


	def test_invalid_file_path(self):
		'''
		Test handling of an invalid file path.
		'''
		with self.assertRaises(SystemExit):
			with patch('sys.argv', ['prog', '--filepath', '']):
				parse_arguments()


	def test_invalid_seed(self):
		'''
		Test handling invalid seed value (e.g., non-integer).
		'''
		with self.assertRaises(SystemExit):
			with patch('sys.argv', ['prog', '--seed', 'not_an_integer']):
				parse_arguments()


	def test_invalid_number_of_rounds(self):
		'''
		Test handling invalid number of rounds (e.g., negative number).
		'''
		with self.assertRaises(SystemExit):
			with patch('sys.argv', ['prog', '--num-rounds', '-5']):
				parse_arguments()

		
	def test_invalid_number_of_problems(self):
		'''
		Test handling invalid number of problems (e.g., negative number).
		'''
		with self.assertRaises(SystemExit):
			with patch('sys.argv', ['prog', '--num-problems', '-3']):
				parse_arguments()


	def test_invalid_topk_problems(self):
		'''
		Test handling invalid topk problems value (e.g., negative number).
		'''
		with self.assertRaises(SystemExit):
			with patch('sys.argv', ['prog', '--topk-problems', '-1']):
				parse_arguments()


	def test_invalid_agent_value(self):
		'''
		Test handling invalid agent value (empty).
		'''
		with self.assertRaises(SystemExit):
			with patch('sys.argv', ['prog', '--agent', '']):
				parse_arguments()


	def test_invalid_mutation_start(self):
		'''
		Test handling invalid mutation start value (should be 'Y' or 'N').
		'''
		with self.assertRaises(SystemExit):
			with patch('sys.argv', ['prog', '--mutate-on-start', 'Invalid']):
				parse_arguments()


if __name__ == '__main__':
	unittest.main()
