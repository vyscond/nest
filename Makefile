dist:
	python setup.py bdist
	python setup.py sdist --formats=gztar,zip
	python setup.py bdist_wheel --universal

pep8:
	flake8 nest/*

install:
	pip install .

upgrade:
	pip install . --upgrade