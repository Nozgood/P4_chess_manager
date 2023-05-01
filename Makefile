run:
	python3 main.py

flake8:
	flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport ./
