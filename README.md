# gatorquery

![Pensive Spiderman](https://i.imgur.com/Cb3vQSR.png)

[![Build Status](https://travis-ci.com/GatorEducator/gatorquery.svg?branch=master)](https://travis-ci.com/GatorEducator/gatorquery)
[![codecov.io](http://codecov.io/github/GatorEducator/gatorquery/coverage.svg?branch=master)](http://codecov.io/github/GatorEducator/gatorquery?branch=master)
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat)](#contributors)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)

## A Survey Hosting Tool for Professors

As an alternative to Google Forms or other survey creation sites, this program allows professors to create survey, send it to students to answer, and then dynamically collect the responses. By allowing for the dynamic collection and storing of the responses, professors do not have to repeatedly download the output to run analysis.

In the future, this program will look into supporting uploading surveys as a CSV, as well as providing integration for basic analysis tools.

This [Flask](http://flask.pocoo.org/) based web application allows course instructors to upload a course survey, distribute that survey to their students, and collect their data through a dynamically updated endpoint.

## Pipenv

GatorQuery uses a [Pipenv](https://project/pipenv/)-built virtual environment
to standardize the execution of the project. If you don't have pipenv we highly
recommend installing it using `pip`:

```
pip install pipenv
```

If for some reason this doesn't work for you, you can check out the [pipenv
github](https://github.com/pypa/pipenv).

## Commands

After cloning the repo for the first time, run

```
pipenv install --dev
```

to install the developer and default packages. To get a list of scripts for the
project, inspect the `[scripts]` tag in `Pipfile`:

```
cat Pipfile
```

Finally, to run the project locally:

```
pipenv run server
```

Or use the following to see all the options:

```
pipenv run python GatorQuery.py --help
```
