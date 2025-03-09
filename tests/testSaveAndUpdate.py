"""
Unit test class for problems saving and leaderboard updating.
"""

import sys
sys.path.append('.')

import unittest
from unittest.mock import patch, mock_open
from scripts.data_handling import Problem, save_mutated_problem, update_leaderboard

class TestSaveAndUpdate(unittest.TestCase):
	@patch('builtins.open', new_callable=mock_open)
	def test_save_mutated_problem(self, mock_file):
		# Testing saving a mutated problem to a file
		problem = Problem(id="123", mutated=True, mutated_description="Mutated description")
		save_mutated_problem(problem, output_dir='outputs/')

		mock_file.assert_called_once_with('outputs/123.txt', 'w')
		mock_file().write.assert_called_once_with("Mutated description")

	@patch('yaml.dump')
	@patch('builtins.open', new_callable=mock_open)
	def test_update_leaderboard(self, mock_file, mock_yaml_dump):
		# Testing updating the leaderboard file with new data
		problems = [Problem(id="123", score=10.0)]
		update_leaderboard(problems, filepath='logs/leaderboard.yml')

		mock_file.assert_called_once_with('logs/leaderboard.yml', 'w')
		mock_yaml_dump.assert_called_once()


if __name__ == '__main__':
	unittest.main()
