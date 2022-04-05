ENV=local


.PHONY: build
build: 
	sudo docker-compose -f docker-compose.$(ENV).yml build


.PHONY: run
run: 
	sudo docker-compose -f docker-compose.$(ENV).yml build
	sudo docker-compose -f docker-compose.$(ENV).yml up


.PHONY: tidy
tidy: 
	pip freeze > requirements.txt


.PHONY: count
count:
	find . -name tests -prune -o -type f -name '*.py' | xargs wc -l


.DEFAULT_GOAL := run