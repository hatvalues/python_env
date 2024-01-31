install:
	python -m pip install --upgrade pip && python -m pip install -r requirements.txt

test:
	python -m pytest --cov=python_env

lint:
	pylint --disable=R,C ./

format:
	black *.py

clean:
	rm -rf __pycache__

all: install lint clean format test