# bookish
Very broken repository, only meant to prove a point.

## Requirements
Only a working version of Python 3 and virtualenv is required.

## Setup
Wherever this repository is cloned, run:
```shell
$ python -m venv ve
$ . ve/bin/activate
(ve) $ pip install -e .[dev]
```

## Running
To run the application in development mode:
```shell
(ve) $ pserve dev.ini --reload
```
It should be accessible on http://localhost:6543.

## Testing
To run the test suite:
```shell
(ve) $ pytest
```
