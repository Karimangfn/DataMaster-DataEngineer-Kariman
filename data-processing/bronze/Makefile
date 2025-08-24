precommit:
	pre-commit run --all-files

test:
	pytest --cov=src/ --cov-report=term-missing tests/

mypy:
	PYTHONPATH=src mypy --ignore-missing-imports src/

check: precommit test mypy
