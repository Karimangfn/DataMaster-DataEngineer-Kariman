precommit:
	pre-commit run --all-files

test:
	pytest --cov=src/ --cov-report=term-missing tests/

mypy:
	mypy src/

docker-build:
	@service_path=$$(git ls-tree -r HEAD --name-only | grep 'VERSION' | head -n 1 | xargs dirname); \
	image_name=$$(basename $$service_path); \
	docker build -t $$image_name:test -f $$service_path/Dockerfile $$service_path

check: precommit test mypy docker-build
