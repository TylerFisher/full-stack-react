test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd fullstack/staticapp/

database:
	dropdb fullstack --if-exists
	createdb fullstack
