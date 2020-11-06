# makefile to manage repetitive commands


all: format lint test

format:
	@echo "Formatting files..."
	@black . --target-version py38
	@isort .

lint:
	@echo "Type checking files..."
	@mypy .
	@echo "Linting files..."
	@flake8 --docstring-convention google

test:
	@echo "Testing..."
	@pytest --color=yes

test-cov:
	@echo "Testing with Coverage..."
	@pytest --cov

run:
	@poetry run streamlit run gfdx/app.py

