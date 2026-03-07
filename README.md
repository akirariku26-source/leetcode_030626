# LeetCode Training 2026

Personal LeetCode practice repository for 2026. Solutions, notes, and problem-solving approaches for algorithm and data structure challenges.

## Structure

```
├── src/          # Solution code (e.g., lc_146_lru.py)
├── test/         # Tests (e.g., test_lc_146_lru.py)
└── README.md
```

## Running tests

Uses [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/):

```bash
# Show available recipes
just

# Run all tests
just test

# Run tests for a specific problem (e.g., lc_146_lru -> test/test_lc_146_lru.py)
just test lc_146_lru

# Lint the repo
just lint

# Auto-fix and format the repo
just format
```

First-time setup: `uv sync` (installs pytest and ruff as dev dependencies).
