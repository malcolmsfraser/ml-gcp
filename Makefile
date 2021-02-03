setup:
	gcloud app create
	
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
lint:
	pylint --disable=R,C main.py
	pylint --disable=R,C main3.py
deploy:
	gcloud app deploy
all: install lint deploy
