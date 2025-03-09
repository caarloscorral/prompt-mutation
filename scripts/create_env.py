"""
File to set environment variables.
"""

import os
import sys
import configparser

sys.path.append('.')


def run_env() -> None: 
	'''
	Upon execution set system variables. 
	'''
	#---------------------------
	# Add path variables
	#---------------------------
	sys.path.append('./problem_mutation/')
	sys.path.append('./app/')


	#---------------------------
	# Config Parser
	#---------------------------
	config = configparser.ConfigParser()
	conf = config.read('./config.ini')
	assert len(conf) != 0, 'Config file not found'

	#---------------------------
	# OpenAI config variables
	#---------------------------
	os.environ['OPENAI_API_KEY'] = config.get('OpenAI', 'OPENAI_API_KEY')
	os.environ['OPENAI_API_ENDPOINT'] = config.get('OpenAI', 'OPENAI_API_ENDPOINT')
