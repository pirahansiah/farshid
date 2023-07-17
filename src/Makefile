.PHONY: help
.DEFAULT_GOAL := help

help: ## get a list of all the targets, and their short descriptions
	@# source for the incantation: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

create: ## create requirements.txt
	pip freeze > requirements.txt

environment: ## installs required environment for deployment
	pip install -r requirements.txt

dev_environment:  ## installs required environment for development & document corpus generation
	pip install -qqq -r requirements-dev.txt

conda: ##conda
	conda install -y -c conda-forge --file requirements_conda.txt
	pip install -r requirements.txt

