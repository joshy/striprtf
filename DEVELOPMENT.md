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

## Releasing a new version

1. Prepare the release commit on top of master. The working copy must contain only the release changes,
   everything else would end up in the built package without being committed.
```sh
jj new master
# edit striprtf/_version.py  -> __version__ = "0.0.X"
# edit CHANGELOG.md          -> add "## v0.0.X - DD.MM.YY" entry
uv run pytest
jj commit -m "new version v0.0.X"
jj bookmark set master -r @-
jj git push --bookmark master
```

2. Build from the committed state and check the metadata:
```sh
rm -rf dist
uv build
unzip -p dist/*.whl '*/METADATA' | grep -E '^(Version|Requires-Dist)'
```
   `Version` must be `0.0.X` and every `Requires-Dist` line must end with `extra == "dev"`.

3. Publish with twine, tokens come from `~/.pypirc`. Twine is part of the `dev` extras, never run
   `uv add twine`, that makes twine a runtime dependency:
```sh
uv run twine upload -r testpypi dist/*   # optional
uv run twine upload -r pypi dist/*
```

4. Tag the release commit (a tag, not a bookmark) and push it:
```sh
jj tag set v0.0.X -r master
git push origin refs/tags/v0.0.X
```

Dependabot alerts for dev or transitive packages are fixed with `uv lock --upgrade-package <name>`,
never by adding the package to `[project] dependencies`.
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
