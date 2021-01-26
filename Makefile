setup:
	source venv/bin/activate
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
lint:
	pylint --disable=R,C main.py
	pylint --disable=R,C main3.py
all: install lint
