.PHONY: help run isort black flake pylint test


help:
	@echo "run: run the project locally\n"
	@echo "isort: adjust imports\n"
	@echo "black: format code\n"
	@echo "flake: lint the code\n"
	@echo "pylint: lint the code\n"
	@echo "test: run the tests\n"


run:
	uvicorn src.main.app:app --reload

isort:
	isort src

black:
	black src

flake:
	flake8 src

pylint:
	pylint src

test:
	pytest --cov --cov-config=.coveragerc
