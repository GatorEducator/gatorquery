#!/bin/bash

pipenv run pytest -s --cov-config=.coveragerc --cov-report=term-missing --cov-branch --cov
