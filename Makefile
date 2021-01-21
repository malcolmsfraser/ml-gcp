install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
lint:
	pylint --disable=R,C main.py
	pylint --disable=R,C main2.py
all: install lint
