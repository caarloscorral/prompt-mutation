import logging

class Logger:
	def __init__(self, log_file='logs/app.log', level=logging.DEBUG):
		'''
		Initializes the Logger class.

		:param log_file: str, file path for logging output, defaults to logs/app.log
		:param level: Logging level (default is DEBUG)
		'''
		# Creating a custom logger
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(level)

		# Creating handlers
		file_handler = logging.FileHandler(log_file)
		stream_handler = logging.StreamHandler()

		# Setting level for handlers
		file_handler.setLevel(level)
		stream_handler.setLevel(level)

		# Creating formatters and adding them to handlers
		file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		stream_format = logging.Formatter('%(levelname)s - %(message)s')
		file_handler.setFormatter(file_format)
		stream_handler.setFormatter(stream_format)

		# Adding handlers to the logger
		self.logger.addHandler(file_handler)
		self.logger.addHandler(stream_handler)


	def debug(self, message) -> None:
		'''
		Logs a message with level DEBUG.

		:param message: str, message to log.
		'''
		self.logger.debug(message)


	def info(self, message) -> None:
		'''
		Logs a message with level INFO.

		:param message: str, message to log.
		'''
		self.logger.info(message)


	def warning(self, message) -> None:
		'''
		Logs a message with level WARNING.

		:param message: str, message to log.
		'''
		self.logger.warning(message)


	def error(self, message) -> None:
		'''
		Logs a message with level ERROR.

		:param message: str, message to log.
		'''
		self.logger.error(message)


	def critical(self, message) -> None:
		'''
		Logs a message with level CRITICAL.

		:param message: str, message to log.
		'''
		self.logger.critical(message)
