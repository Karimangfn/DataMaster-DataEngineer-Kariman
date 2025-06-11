precommit:
	pre-commit run --all-files

test:
	pytest --cov=src/ --cov-report=term-missing tests/

mypy:
	mypy src/

docker-build:
	@image_name=$$(basename $$PWD); \
	echo "Building image $$image_name:test"; \
	docker build -t $$image_name:test .

check: precommit test mypy docker-build
