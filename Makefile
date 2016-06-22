PEP8=$(shell flake8 nest/*.py)

dist:
ifeq($(PEP8),'')
	python setup.py bdist
	python setup.py sdist --formats=gztar,zip
	python setup.py bdist_wheel --universal
else
	@echo 'you have pep issue!'
	@echo "$pep8"
endif

pep8:
	flake8 nest/*.py

install:
	pip install .

upgrade:
	pip install . --upgrade
