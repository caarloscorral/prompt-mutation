"""
File to parse command-line arguments.
"""

import argparse

def positive_int(value):
	'''
	Custom argparse type for checking positive integers.
	'''
	ivalue = int(value)
	if ivalue < 0:
		raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value.")

	return ivalue


def non_empty_string(value):
	'''
	Custom argparse type for checking non-empty strings.
	'''
	if not value.strip():
		raise argparse.ArgumentTypeError("String value cannot be empty.")

	return value


def parse_arguments():
	'''
	Parses command-line arguments for the problem processing application.
	'''
	parser = argparse.ArgumentParser(description="Process and mutate problem statements.")
	parser.add_argument('--filepath', type=non_empty_string, default='problems/problems.txt', help="File path to the problems.txt file.")
	parser.add_argument('--seed', type=positive_int, default=42, help="Integer seed for random operations.")
	parser.add_argument('--agent', type=non_empty_string, default='gpt-4o', help="Specifies AI agent (e.g., gpt-4o).")
	parser.add_argument('--num-rounds', type=positive_int, default=5, help="Number of processing rounds.")
	parser.add_argument('--num-problems', type=positive_int, default=2, help="Number of problems to process each round.")
	parser.add_argument('--topk-problems', type=positive_int, default=2, help="Number of top problems retained per round.")
	parser.add_argument('--mutate-on-start', type=non_empty_string, default='Y', choices=['Y', 'N'], help="Whether to mutate at the beginning of execution. Select from 'Y' or 'N'.")	

	return parser.parse_args()
