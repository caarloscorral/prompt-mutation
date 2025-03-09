# Contributing to Prompt-Mutation

We welcome contributions from the community to help make Prompt-Mutation better. Whether it's fixing bugs, adding new features, improving documentation, or tweaking test scripts, your involvement is appreciated. Here is a step-by-step guide to help you contribute.

## Getting Started

### Fork the Repository

1. Navigate to the [Prompt-Mutation GitHub repository](https://github.com/caarloscorral/prompt-mutation).
2. Click on the 'Fork' button to create your own copy of the repository.

### Clone Your Fork

```bash
git clone https://github.com/caarloscorral/prompt-mutation.git
cd prompt-mutation
```

### Set Upstream Remote

It's useful to have the original repository configured as your `upstream` remote to keep your fork up-to-date with the latest changes from the main repository.

```bash
git remote add upstream https://github.com/caarloscorral/prompt-mutation.git
```

## Making Changes

### Create a Branch

Create a new branch for your changes. Use a descriptive name for your branch:

```bash
git checkout -b feature-name
```

### Make Your Changes

Edit the code and make improvements or fix issues.

### Test Your Changes

Before committing changes, ensure that all tests pass, and add new tests where necessary to cover your additions or modifications.

Run tests with:
```bash
python -m unittest discover -s tests/ -p "test*.py"
```

### Commit Your Changes

```bash
git add .
git commit -m "Description of changes"
```

### Push to Your Fork

```bash
git push origin feature-name
```

## Submitting a Pull Request

1. Go to the repository on GitHub where your fork is stored.
2. Click on the 'Compare & pull request' button.
3. Provide a clear description of your changes in the pull request comment section.
4. Submit the pull request for review.

## Code Review

Your pull request will be reviewed, and you may be asked to make additional modifications. Please be responsive to feedback and make the requested changes where necessary.

## Contributor Code of Conduct

Please adhere to the project's code of conduct in all interactions to ensure a welcoming and supportive environment for all contributors.

## Thank You!

Thank you for considering contributing to Prompt-Mutation! Your efforts help make this project successful and beneficial to the community.