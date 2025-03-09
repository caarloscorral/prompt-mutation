# Prompt-Mutation

## Overview

Prompt-Mutation is a Python application designed to process, mutate, and evaluate problem statements. Utilizing AI technologies, particularly Azure's OpenAI services, the application reads problem descriptions, applies various mutative strategies, and evaluates the results to generate innovative solutions in a structured and repeatable manner.


## Directory Structure

- **logs/**: Stores logs and the leaderboard in YAML format.

- **outputs/**: Directory for storing processed and mutated problems.

- **problems/**: Contains the list of problem statements.
  - `problems.txt`: The initial set of problems to be processed.

- **prompts/**: Holds templates that guide mutation and evaluation.
  - `mutations/`: Contains templates for mutation strategies.
      - `add_constraints.txt`, `rephrase.txt`, `simplify.txt`, etc.
  - `evaluations/`: Contains templates for evaluating mutated problems.
      - `evaluate.txt`

- **scripts/**: Contains the script files with core functionality.
  - `arg_parsing.py`: Handles command-line argument parsing using argparse. Defines flags necessary for running the application (e.g., file paths, AI agent type, processing rounds)..
  - `create_env.py`: Configures environment variables for accessing Azure's OpenAI API, critical for authentication and access control.
  - `data_handling.py`: Functions for loading problem statements from files, saving processed results, and updating leaderboards. Facilitates input/output operations.
  - `main.py`: Entry point for running the application. It orchestrates the overall workflow from environment setup, problem loading, iteration over rounds, applying mutations, evaluating results, to updating the leaderboard.
  - `mutation.py`: Implements the core logic for mutating and evaluating problem statements using AI models. Connects with Azure OpenAI via AzureOpenAIClient.

- **src/**: Supporting source files.
  - `AzureOpenAIClient.py`: Manages API calls to Azure's OpenAI service. Provides methods to generate model responses from problem templates.
  - `Logger.py`: Implements logging functionality to track application status, errors, and outputs. Enhances debugging and monitoring.

- **tests/**: Holds the unit tests for modules.
  - `testArgumentParsing.py`: Tests for argument parsing.
  - `testEvaluateProblem.py`: Tests for problem evaluation.
  - `testMutateProblem.py`: Tests for problem mutation.
  - `testSaveAndUpdate.py`: Tests for saving and updating leaderboard.

- **config.ini**: Stores crucial Azure OpenAI API credentials.

- **docker-compose.yml**: Configuration for Docker if integration is necessary.

- **Dockerfile**: Specifications for the Docker image creation.

- **requirements.txt**: Lists Python dependencies required for the project.


## Prerequisites

- Docker installed on your machine.
- Azure OpenAI API credentials.


## Setup and Installation

### Configuration File

- A `config.ini` file is used for storing Azure OpenAI API credentials.
- Example `config.ini`:
  ```ini
  [OpenAI]
  OPENAI_API_KEY = your_openai_api_key
  OPENAI_API_ENDPOINT = your_openai_api_endpoint
  ```
  Replace `your_openai_api_key` and `your_openai_api_endpoint` with your actual OpenAI credentials. This configuration is necessary for authenticating your requests to the Azure OpenAI API.

### Using Docker

1. **Build the Docker Image and run the container**
   Navigate to the root of your project where the `docker-compose.yml` file is located and run:
   ```bash
   docker-compose up --build
   ```

   This will build and run your application in a container, mapping port 5678 from the container to your local machine.

### Modify Command-Line Arguments

The default arguments for the application are specified in the `Dockerfile` under the `CMD` section:
```Dockerfile
CMD ["python", "scripts/main.py", "--filepath", "problems/problems.txt", "--seed", "42", "--agent", "gpt-4o", "--num-rounds", "5", "--num-problems", "2", "--topk-problems", "2", "--mutate-on-start", "Y"]
```
To modify these arguments, you can either:

- **Edit the Dockerfile**: Directly change the command and arguments in the `CMD` statement.

- **Override the Command at Runtime**: Use Docker run commands or Docker Compose overrides to specify changes:
  ```bash
  docker-compose run prompt-mutation python scripts/main.py --filepath "yourfilepath.txt" --seed "123"
  ```
  This allows you to specify different arguments directly when using the CLI.


## Usage

When the container is up and running, it will execute the main script with the specified arguments, processing the problems defined in your `problems.txt` file.


## Testing

To ensure functionality, run the unit tests:
```bash
python -m unittest discover -s tests/ -p "test*.py"
```


## Documentation

- **Code**: Ensure inline comments and function docstrings for clarity.
- **Read Me**: Maintain the README for setup and usage instructions.
- **Additional Documentation**: Any additional documents should be added in a `docs/` folder if required.


## Contributing

We welcome contributions! Please read [CONTRIBUTING](https://github.com/caarloscorral/prompt-mutation/blob/main/CONTRIBUTING.md) for guidelines on contributing to this project.


## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/caarloscorral/prompt-mutation/blob/main/LICENSE) file for details.