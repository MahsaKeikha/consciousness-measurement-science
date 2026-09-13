# Reproducibility

Create an environment and run:

```bash
python -m pip install -e ".[dev]"
pytest -q
ruff check .
```

The initial code is intentionally small and auditable. It demonstrates structural alignment and assumption-explicit evidence fusion.

Future empirical analyses should record:

- dataset version/hash;
- preprocessing pipeline;
- exclusion criteria;
- random seeds;
- preregistration link;
- software environment;
- held-out split definition;
- all analysis variants attempted.
