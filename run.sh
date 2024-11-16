#!/usr/bin/env bash

function clean() {
  find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*.html' -exec rm -f {} +
	find . -name '*.apk' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf reports && mkdir -p reports
}

function test_all() {
    poetry run pytest tests
}

function test_web() {
    poetry run pytest --headed tests/web
}

function setup() {
    poetry install --no-root
}

"$@"