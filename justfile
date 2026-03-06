default:
  just --list

# Run tests for a specific file or all tests
test test_name='':
  #!/usr/bin/env bash
  if [ -z "{{test_name}}" ]; then
    uv run pytest test/ -v
  else
    uv run pytest test/test_{{test_name}}.py -v
  fi
