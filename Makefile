.PHONY: lint

lint:
	isort .
	black .
	flake8 . --exclude .venv

