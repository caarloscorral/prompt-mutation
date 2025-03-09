"""
File to handle loading and saving of prompts and problems.
"""

import os
import yaml
import uuid
import datetime
from typing import List
from dataclasses import dataclass, field


@dataclass
class Problem:
	'''
	Data class for representing a problem.
	'''
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	original_description: str = ""
	mutated_description: str = ""
	mutated: bool = False
	score: float = 0.0
	mutation_log: list = field(default_factory=list)
	error_logs: list = field(default_factory=list)
	warnings_log: list = field(default_factory=list)


def load_prompt_templates(strategies_dir: str='prompts/mutations/') -> dict:
	'''
	Loads prompt templates for available mutation strategies.

	:param strategies_dir: str, directory path where strategies are saved, defaults to prompts/mutations/
	:return: dict, dictionary where keys are the mutation strategies and values are the templates.
	'''
	
	prompt_templates = {}

	# Loading prompt templates in strategies_dir
	for strategy in os.listdir(strategies_dir):
		with open(os.path.join(strategies_dir, strategy), 'r') as file:
			prompt_templates[strategy] = file.read().strip()

	return prompt_templates


def load_evaluation_template(evaluation_dir: str='prompts/evaluations/', evaluation_filepath: str='evaluate.txt') -> dict:
	'''
	Loads evaluation template.

	:param evaluation_dir: str, directory path where evaluation is saved, defaults to prompts/evaluations/
	:param evaluation_filepath: str, evaluation file name, defaults to evaluate.txt.
	:return: str, evaluation template.
	'''
	# Checking if evaluation file exists
	filepath = os.path.join(evaluation_dir, evaluation_filepath)
	if not os.path.exists(filepath):
		raise FileNotFoundError(f"Error: The file {filepath} does not exist.")
	
	# Loading evaluation template
	evaluation_template = ""
	with open(os.path.join(evaluation_dir, evaluation_filepath), 'r') as file:
		evaluation_template = file.read().strip()

	return evaluation_template


def load_problems(filename: str='problems/problems.txt') -> List[Problem]:
	'''
	Loads problem statements from a specified text file and saves them in list of Problem classes.

	:param filename: str, problems file name.
	:return: list, list whith each of the problems
	'''
	# Checking if problems file exists
	if not os.path.exists(filename):
		raise FileNotFoundError(f"Error: The file {filename} does not exist.")

	# If problems file exists parsing it saving each of the problems in a list of Problem classes
	problems = []
	with open(filename, 'r') as file:
		for line in file:
			description = line.strip()

			# Checking line is not empty
			if description:
				problems.append(Problem(original_description=description))

	return problems


def save_mutated_problem(problem: Problem, output_dir: str='output/') -> None:
	'''
	Saves mutated problem to a uniquely named file in the output directory.

	:param problem: Problem class to be saved
	:param output_dir: str, directory path where mutated problems are saved, defaults to output/
	'''
	# Creating output folder if it does not exist
	os.makedirs(output_dir, exist_ok=True)

	# Saving problem statement in a separated text file with a unique filename
	filepath = os.path.join(output_dir, f'{problem.id}.txt')

	with open(filepath, 'w') as file:
		if problem.mutated:
			file.write(problem.mutated_description)
		else:
			log_message = "Error: Cannot save problem as it is still not mutated."
			problem.error_logs.append(log_message)
			raise ValueError(log_message)


def update_leaderboard(problems: List[Problem], filepath: str='logs/leaderboard.yml') -> None:
	'''
	Update the leaderboard with current problem scores.

	:param problems: list, list of mutated Problem classes to write on leaderboard file
	:param filepath: str, leaderboard filepath, defaults to logs/leaderboard.yml
	'''
	# Creating logs folder if it does not exist
	os.makedirs(os.path.dirname(filepath), exist_ok=True)

	leaderboard_content = [{
		'ts': str(datetime.datetime.now()),
		'id': str(problem.id),
		'original_description': problem.original_description,
		'mutated_description': problem.mutated_description,
		'mutated': problem.mutated,
		'score': problem.score,
		'mutation_log': problem.mutation_log,
		'error_logs': problem.error_logs,
		'warnings_log': problem.warnings_log
	} for problem in problems]

	try:
		with open(filepath, 'w') as file:
			yaml.dump(leaderboard_content, file)

	except Exception as e:
		raise Exception(f"Error writing leaderboard: {str(e)}") from e
