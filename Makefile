.DEFAULT_GOAL := help

divide: ## Run the divide skill on every page individually, one PR per page split
	./run/divide

entwine: ## Run the entwine skill as a single whole-garden pass, one PR for all links added
	./run/entwine

fertilize: ## Run the fertilize skill on every page individually, one PR per page expanded
	./run/fertilize

forage: ## Regenerate TODO.md with topics mentioned but not yet sown, one PR
	./run/forage

graft: ## Run the graft skill as a single whole-garden pass, one PR for all merges
	./run/graft

prune: ## Run the prune skill on every page individually, one PR per page trimmed
	./run/prune

sow: ## Plant a brand-new entry for the topic given on the command line
	./run/sow

tend: ## Run the tend skill on every page individually, one PR per page fixed
	./run/tend

tidy: ## Run the tidy skill on every page individually, one PR per page fixed
	./run/tidy

uproot: ## Run the uproot skill on every page individually, one PR per page dropped
	./run/uproot

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: divide entwine fertilize forage graft prune sow tend tidy uproot help