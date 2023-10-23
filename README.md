# Derivco Assessment

This is a Python-based automation project which uses Pytest as a test framework. There is
more to this framework.

# Pre-requisites:

➔ Python 3


➔ An IDE suitable for Python. Ideally Pycharm

# How To Run:

## Part 1 - Set Up

Install virtualenv - pip install virtualenv

Create virtual environment - python3 -m virtualenv venv

Activate virtual environment - source venv/bin/activate

Install dependencies - pip install -r requirements.txt



## Part 2 - Run

To run all tests - pytest --html=report.html

To run tests for Ingredients Scenarios - pytest -m INGREDIENTS --html=report.html

To run tests for Cocktails Scenarios - pytest -m COCKTAILS --html=report.html

To run tests for Additional Scenarios - pytest -m EXTRA --html=report.html

## Reporting:

In order to view the execution report,open a file named report.html in the
./derivco-assessment/ folder.
