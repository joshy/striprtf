# Development Guide

This guide covers development setup, debugging, and release procedures for striprtf.

## Development Setup

1. Install `uv` (recommended for faster dependency management):
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create and activate a virtual environment:
```sh
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install development dependencies:
```sh
uv pip install -e ".[dev]"
```

4. Set up PyPI credentials:
   - Create a `.env` file in the project root (this file is gitignored)
   - Add your PyPI token:
   ```sh
   UV_PUBLISH_TOKEN=your-pypi-token-here
   ```
   - Or set it as an environment variable:
   ```sh
   export UV_PUBLISH_TOKEN=your-pypi-token-here
   ```

## Running Tests

Run the test suite:
```sh
pytest
```

For verbose output:
```sh
pytest -v
```

## Debugging

For debugging with `debugpy`, install it first:
```sh
uv pip install debugpy
```

Then run the following command:
```sh
python -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m pytest -v tests/test_issue_55.py
```

For debugging a single method:
```sh
python -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m pytest -v tests/test_issue_55.py::Fonttbl::test_fonttbl_file1
```

Use this `launch.json` configuration for VS Code:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Remote Attach",
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 5678
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "."
                }
            ]
        }
    ]
}
```

## Building and Publishing

1. Build the package:
```sh
uv build
```

2. Upload to TestPyPI (recommended for testing):
```sh
uv publish --index testpypi
```

3. Upload to PyPI:
```sh
uv publish --index pypi
```

Note: Make sure you have set up your PyPI credentials in the `.env` file or as environment variables before publishing.

The PyPI and TestPyPI configurations are already set up in your `pyproject.toml`:
```toml
[[tool.uv.index]]
name = "pypi"
url = "https://pypi.org/simple/"
publish-url = "https://upload.pypi.org/legacy/"
explicit = true

[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```

## Project Structure

- `striprtf/` - Main package directory
- `tests/` - Test suite
- `pyproject.toml` - Project configuration and dependencies
- `.env` - PyPI credentials (not committed to git)

## Development Tools

- `pytest` - Testing framework
- `build` - Package building
- `ruff` - Code linting (configured in pyproject.toml)
- `uv` - Fast Python package installer and resolver
