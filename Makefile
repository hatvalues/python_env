install:
	python -m pip install --upgrade pip && python -m pip install -r requirements.txt

test:
	python -m pytest

lint:
	/home/codespace/.venv/bin/pylint --disable=R,C ./

format:
	black *.py

clean:
	rm -rf __pycache__

all: install lint clean format test