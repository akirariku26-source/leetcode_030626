default:
  just --list

# Lint the source and tests
lint:
  uv run ruff check src test

# Auto-fix lint issues and format the codebase
format:
  uv run ruff check --fix src test
  uv run ruff format src test

# Run tests for a specific file or all tests
test test_name='':
  #!/usr/bin/env bash
  if [ -z "{{test_name}}" ]; then
    uv run pytest test/ -v
  else
    uv run pytest test/test_{{test_name}}.py -v
  fi
