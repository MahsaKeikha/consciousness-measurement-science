.PHONY: test lint check

test:
	PYTHONPATH=src python -m pytest -q

lint:
	ruff check .

check: test lint
