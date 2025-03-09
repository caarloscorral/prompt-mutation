"""
File to handle mutation and evaluation of problems.
"""

from scripts.data_handling import Problem
from src.AzureOpenAIClient import AzureOpenAIClient


def mutate_problem(client: AzureOpenAIClient, problem: Problem, prompt_template: str) -> str:
	'''
	Mutates a problem using the specified AI model and prompt template.

	:param client: AzureOpenAIClient object.
	:param problem: Problem object to mutate.
	:param prompt_template: str, template to format the problem statement for mutation.
	:return: str, mutated problem statement.
	'''
	# Ensuring placeholder exists in the template
	if "{statement}" not in prompt_template:
		log_message = "Error: Placeholder '{statement}' not found in the chosen template."
		problem.error_logs.append(log_message)
		raise ValueError(log_message)
	
	prompt = prompt_template.format(statement=problem.original_description)

	try:
		# Sending mutation prompt to LLM model
		response = client.generate_response(
			system_message=\
			"""
			You are a helpful assistant ready to mutate problem descriptions, providing direct responses without additional commentary.
			""",
			user_input=prompt
   		)

		problem.mutated_description = response
		problem.mutated = True
		problem.mutation_log.append(
			{
				'prompt': prompt,
				'result': response
			}
		)

	except Exception as e:
		log_message = f"Error during mutation: {str(e)}"
		problem.error_logs.append(log_message)
		raise ValueError(log_message)

	return response


def evaluate_problem(client: AzureOpenAIClient, problem: Problem, evaluation_template: str) -> float:
	'''
	Evaluates a problem using the specified AI model comparing the original and the mutated statements.

	:param client: AzureOpenAIClient object.
	:param problem: Problem object to mutate..
	:param evaluation_template: str, template to format the problem statement for evaluation.
	:return: float, evauation score.
	'''
	# Checking if problem statement is mutated
	if not problem.mutated:
		log_message = "Error: Problem statement is not mutated. Cannot evaluate."
		problem.error_logs.append(log_message)
		raise ValueError(log_message)

	# Checking if placeholders exist in the evaluation template
	if "{original_statement}" not in evaluation_template:
		log_message = f"Error: Placeholder '{{original_statement}}' not found in the chosen template for evaluation '{evaluation_template}'"
		problem.error_logs.append(log_message)
		raise ValueError(log_message)

	if "{mutated_statement}" not in evaluation_template:
		log_message = f"Error: Placeholder '{{mutated_statement}}' not found in the chosen template for evaluation '{evaluation_template}'"
		problem.error_logs.append(log_message)
		raise ValueError(log_message)
	
	# Creating evaluation prompt
	evaluation_prompt = evaluation_template.format(original_statement=problem.original_description, mutated_statement=problem.mutated_description)

	try:
		# Sending evaluation prompt to LLM model
		response = client.generate_response(
			system_message=\
			"""
			You are a helpful assistant tasked with scoring the quality of problem statement mutations.
			""",
			user_input=evaluation_prompt
		)

		problem.score = float(response)

	except Exception as e:
		log_message = f"Error during evaluation: {str(e)}"
		problem.error_logs.append(log_message)
		raise ValueError(log_message)

	return float(response)
