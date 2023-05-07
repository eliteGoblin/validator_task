# Validator Task

This Python project implements a validator to check certain rules for input objects. It uses the SimpleFactory and Strategy design patterns to create a flexible and extensible validation system.

# Design Patterns

## Simple Factory Pattern

The Factory pattern is used to create validator instances based on the input topic. The ValidatorFactory class is responsible for creating the appropriate validator for a given topic. This pattern allows for easy addition of new topic validators without modifying the existing code.

## Strategy Pattern

The Strategy pattern is used to define different validation strategies for each topic. Each validator class implements a specific validation strategy by extending the Validator base class and providing its own validate method. 

# Continuous Integration (CI)

The project uses GitHub Actions for Continuous Integration. The CI pipeline consists of multiple checks, including code formatting, linting, type checking, and testing.

*  We use isort and black for code formatting. The reformat function in the scripts/reformat.sh script runs these tools on the project files.
*  We use pycodestyle and pylint for linting. The scripts/lint.sh script runs these tools on the project files.
*  We use mypy for type checking. The scripts/type_check.sh script runs mypy with the specified configuration file.
*  We use pytest for testing, and coverage for test coverage analysis

```sh
# test result
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
validator_task/__init__.py        2      0   100%
validator_task/validator.py      36      1    97%   23
-----------------------------------------------------------
TOTAL                            38      1    97%
```

# Usage

To use the validator, create an instance of the InputData class with the required properties and pass it to the appropriate validator obtained from the ValidatorFactory. If the validation fails, a ValidationError will be raised.

```python
validator = ValidatorFactory.get_validator("A")
validator.validate(data)
```