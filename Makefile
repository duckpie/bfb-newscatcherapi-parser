ENV=local

.PHONY: run
run: 
	python3 main.py --env $(ENV)


.PHONY: tidy
tidy: 
	pip freeze > requirements.txt


.PHONY: count
count:
	find . -name tests -prune -o -type f -name '*.py' | xargs wc -l


.DEFAULT_GOAL := run