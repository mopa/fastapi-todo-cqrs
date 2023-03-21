SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.SILENT:

build: ## Build all containers
	docker build -t todocqrs:latest .

start: ## Up ALL workspace and Pycharm
	docker-compose up -d

stop: ## Stop containers
	docker-compose stop

destroy: ## Delete all this containers
	docker-compose down

logs: ## Show logs
	docker-compose logs -f

clean-cache: ## Clean cache files
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .coverage

