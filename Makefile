all: install_deps test

filename=couleur-`python -c 'import couleur;print couleur.version'`.tar.gz

export PYTHONPATH:=  ${PWD}
export FORCE_COULEUR:=  true

install_deps:
	@pip install -r requirements.pip

test:
	@nosetests --verbosity=2
	@steadymark README.md

clean:
	@printf "Cleaning up files that are already in .gitignore... "
	@for pattern in `cat .gitignore`; do rm -rf $$pattern; find . -name "$$pattern" -exec rm -rf {} \;; done
	@echo "OK!"

release: clean test publish
	@printf "Exporting to $(filename)... "
	@tar czf $(filename) couleur setup.py README.md
	@echo "DONE!"

publish:
	@python setup.py sdist register upload
