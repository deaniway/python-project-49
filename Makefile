install:
	poetry install

publish:
	poetry publish --dry-run

build:
	poetry build

run:
	poetry run brain-games

package-reinstall:
	pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games
