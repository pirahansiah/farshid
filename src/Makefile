
.PHONY: help
.DEFAULT_GOAL := help

conda: ## Install requirement file using conda with pip fallback

	while read line; do \
      echo "$$line" ; \
	  conda install --yes "$$line" || pip install -U "$$line"; \
    done <  requirements.txt 

help: ## get a list of all the targets, and their short descriptions
	@# source for the incantation: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

environment: ## installs required environment for deployment
	pip install -q -r requirements.txt

dev_environment:  ## installs required environment for development & document corpus generation
	python.exe -m pip install --upgrade pip
	pip install -q -r requirements-dev.txt

run:
	python 0000.py







update: ## conda update ; pip update 

	conda update -y -n base -c defaults conda		
	conda config --add channels pytorch
	conda config --add channels conda-forge
	conda config --add channels anaconda

	# Install pip for fallback
	conda install --yes pip

	python -m pip install --upgrade pip
	
info: ## more
	@echo "www.Pirahansiah.com"