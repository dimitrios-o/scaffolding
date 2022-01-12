install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest --cov=deepcrawl test_mywhatever.py 


lint:
	pylint --disable=R,C *.py

format:
	black *.py
	isort *.py

git:
	git rm -r --cached .
	git add .	
	git commit -m "$m"
	git push -u origin main

all:
	install format lint test