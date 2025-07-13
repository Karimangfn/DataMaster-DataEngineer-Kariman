precommit:
	pre-commit run --all-files

test:
	pytest --cov=src/ --cov-report=term-missing tests/

mypy:
	mypy src/

check: precommit test mypy
