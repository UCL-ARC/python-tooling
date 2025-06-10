SHELL := /bin/bash

help: ## Show this help
	@echo
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%s\033[0m|%s\n", $$1, $$2}' \
        | column -t -s '|'
	@echo

serve: install ## Start a local server and serve the site
	bundle exec jekyll serve

build: install ## Build the site
	bundle exec jekyll build

install: check ## Pull all jekyll dependencies
	bundle install

clean: ## Remove build files
	rm -rf _site

check: ## Check ruby (bundle) is installed
	@command -v bundle &> /dev/null || { echo >&2 "Please install ruby >= 2.7 to use Jekyll"; exit 1; }
