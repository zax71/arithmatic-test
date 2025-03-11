unit_test:
	python3 -m unittest

run: unit_test 
	PYTHONPATH=. python3 __init__.py

