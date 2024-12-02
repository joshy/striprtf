# Release and development 

Some notes for development and pushing new releases to pypi.

## Debugging
For now the best options seems to install `debugpy` and run the following command:
```sh
python -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m pytest -v tests/test_issue_55.py
```

For debugging single method the following syntax can be used:
```sh
python -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m pytest -v tests/test_issue_55.py::Fonttbl::test_fonttbl_file1
```

And the following `launch.json`
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
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
        },
    ]
}
```

## Pushing to PyPi
 * pip install twine

Run commands
```
python setup.py sdist bdist_wheel
twine upload -r testpypi dist/*
twine upload -r pypi dist/*
```
