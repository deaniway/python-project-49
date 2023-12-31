install:
	poetry install

publish:
	poetry publish --dry-run

build:
	poetry build

run:
	poetry run brain-games

package-reinstall:
	 python3 -m pip install  --force-reinstall dist/*.whl

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime
