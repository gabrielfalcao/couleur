.PHONY: tests all clean dependencies tdd docs html purge dist

GIT_ROOT		:= $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
DOCS_ROOT		:= $(GIT_ROOT)/docs
HTML_ROOT		:= $(DOCS_ROOT)/build/html
VENV_ROOT		:= $(GIT_ROOT)/.venv
VENV			?= $(VENV_ROOT)
BENTO_BIN		:= $(shell which bento)
DOCS_INDEX		:= $(HTML_ROOT)/index.html
BENTO_EMAIL		:= gabriel@nacaolivre.org
export FORCE_COULEUR	:= true

export VENV


all: dependencies tests

$(VENV):  # creates $(VENV) folder if does not exist
	python3 -mvenv $(VENV)
	$(VENV)/bin/pip install -U pip setuptools

$(VENV)/bin/sphinx-build $(VENV)/bin/twine $(VENV)/bin/sure $(VENV)/bin/python $(VENV)/bin/pip: # installs latest pip
	test -e $(VENV)/bin/pip || make $(VENV)
	$(VENV)/bin/pip install -r development.txt
	$(VENV)/bin/pip install -e .

# Runs all tests
tests: $(VENV)/bin/sure  # runs all tests
	$(VENV)/bin/sure tests

tdd: $(VENV)/bin/sure  # runs all tests
	$(VENV)/bin/sure tests

# Install dependencies
dependencies: | $(VENV)/bin/sure
	$(VENV)/bin/pip install -r development.txt


$(DOCS_INDEX): | $(VENV)/bin/sphinx-build
	cd docs && make html

html: $(DOCS_INDEX)

docs: $(DOCS_INDEX)
	open $(DOCS_INDEX)

release: | clean bento tests html
	@rm -rf dist/*
	@./.release
	@make pypi

bento: | $(BENTO_BIN)
	$(BENTO_BIN) --agree --email=$(BENTO_EMAIL) check --all

dist: | clean
	$(VENV)/bin/python setup.py build sdist

pypi: dist | $(VENV)/bin/twine
	$(VENV)/bin/twine upload dist/*.tar.gz

# cleanup temp files
clean:
	rm -rf $(HTML_ROOT) build dist


# purge all virtualenv and temp files, causes everything to be rebuilt
# from scratch by other tasks
purge: clean
	rm -rf $(VENV)
