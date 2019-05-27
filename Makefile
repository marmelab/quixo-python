DOCKER := docker run -it --rm quixo-python

help: ## Print all commands (default)
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Build the docker container
	docker build -t quixo-python .

run: ## Run the game.
	$(DOCKER) python3 ./main.py

test: ## Run the tests
	$(DOCKER) python3 -m unittest discover -v -s . -p "*_test.py"

lint: ## Run the linter
	$(DOCKER) pycodestyle .
