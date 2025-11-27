format:
    uv run ruff format
    uv run ruff check --fix

sync-env:
    uv sync --all-packages --all-extras

test:
    uv run --all-packages pytest
