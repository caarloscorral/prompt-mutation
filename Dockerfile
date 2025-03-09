# Using official Python 3.9 image as base
FROM python:3.9-slim

# Setting working directory inside the container
WORKDIR /app

# Copying project files into the container
COPY . .

# Updating and installing system dependencies
RUN apt-get update && apt-get install -y \
	python3-venv \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# Creating virtual environment
RUN python3 -m venv venv

# Using virtual environment by default
ENV PATH="/app/venv/bin:$PATH"

# Activating virtual environment
RUN ./venv/bin/activate

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Running Python script specifying command line arguments
CMD ["python", "scripts/main.py", "--filepath", "problems/problems.txt", "--seed", "42", "--agent", "gpt-4o", "--num-rounds", "5", "--num-problems", "2", "--topk-problems", "2", "--mutate-on-start", "Y"]