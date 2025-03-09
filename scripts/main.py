"""
Main entry point for processing and managing problem statements.
"""

import os
import sys
sys.path.append('.')

import random
import logging
from src.Logger import Logger
from scripts.create_env import run_env
from scripts.arg_parsing import parse_arguments
from src.AzureOpenAIClient import AzureOpenAIClient
from scripts.mutation import mutate_problem, evaluate_problem
from scripts.data_handling import load_problems, load_prompt_templates, load_evaluation_template, update_leaderboard, save_mutated_problem


def main():
	# Initialize the custom Logger
	logger = Logger(level=logging.INFO)
	logger.info("Starting the main processing loop.")

	# Setting environment variables
	run_env()

	# Parsing arguments
	logger.info("Parsing command-line arguments.")
	args = parse_arguments()
	random.seed(args.seed)

	# Creating OpenAI client for mutation
	logger.info("Initializing Azure OpenAI clients for mutation and evaluation.")
	mutation_client = AzureOpenAIClient(
		endpoint=os.getenv('OPENAI_API_ENDPOINT'),
		api_key=os.getenv('OPENAI_API_KEY'),
		model=args.agent
	)

	# Creating OpenAI client for evluation
	evaluation_client = AzureOpenAIClient(
		endpoint=os.getenv('OPENAI_API_ENDPOINT'),
		api_key=os.getenv('OPENAI_API_KEY'),
		model=args.agent
	)

	# Loading initial problem statements
	logger.info(f"Loading problems from file: {args.filepath}")
	try:
		problems = load_problems(filename=args.filepath)

	except FileNotFoundError as e:
		log_message = f"Error while loading problems: {str(e)}"
		logger.error(log_message)
		raise FileNotFoundError(log_message)

	except Exception as e:
		log_message = f"Error while loading problems: {str(e)}"
		logger.error(log_message)
		raise Exception(log_message)

	# Loading prompt templates for each strategy
	prompt_templates = load_prompt_templates()

	# Looping while num_rounds
	for n_round in range(args.num_rounds):
		logger.debug(f"Processing round {n_round + 1}/{args.num_rounds}")

		# Selecting a random subset of problems
		problems = random.sample(problems, min(args.num_problems, len(problems)))

		# Determining initial mutation based on --mutated_on_start argument
		if n_round == 0 and args.mutate_on_start.lower() == 'y':
			mutation_prob = True
		elif n_round == 0 and args.mutate_on_start.lower() == 'n':
			continue
		else:
			# 50% chance to mutate
			# mutation_prob = random.choice([True, False])
			mutation_prob = True
		
		# Applying mutations to create new variants using random strategies
		for problem in problems:
			logger.info(f"Processing problem with ID: {problem.id}")

			# If time to mutate
			if mutation_prob:
				# Selecting random strategy
				strategy = random.choice(list(prompt_templates.keys()))

				# Selecting prompt template
				prompt_template = prompt_templates[strategy]

				# Mutating problem
				mutated_description = mutate_problem(client=mutation_client, problem=problem, prompt_template=prompt_template)
				problem.description = mutated_description
	
		# Loading evaluation prompt template
		logger.info("Loading evaluation template.")
		evaluation_template = load_evaluation_template()

		# Evaluating the results
		for problem in problems:
			logger.info(f"Evaluating problem with ID: {problem.id}")
			evaluate_problem(client=evaluation_client, problem=problem, evaluation_template=evaluation_template)
		
		# Updating leaderboard
		logger.info("Updating leaderboard.")
		update_leaderboard(problems=problems)

		# Retaining the top k problems based on score
		logger.info(f"Retaining top {args.topk_problems} problems.")
		problems.sort(key=lambda x: x.score, reverse=True)
		selected_problems = problems[:args.topk_problems]
		
		# Saving mutated and evaluated problems
		for problem in selected_problems:
			logger.info(f"Saving mutated problem with ID: {problem.id}")
			save_mutated_problem(problem=problem)


if __name__ == '__main__':
	main()
