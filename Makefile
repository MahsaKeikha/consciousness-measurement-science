.PHONY: test policy lint check

test:
	PYTHONPATH=src python -m pytest -q

policy:
	python scripts/verify_repository_policy.py

lint:
	ruff check .

check: test policy lint
