install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest

lint:
	pylint ./

clean:
	rm -rf __pycache__

all: setup lint test clean
