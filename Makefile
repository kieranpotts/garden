.DEFAULT_GOAL := help

cultivate: ## Run the cultivate skill on every page individually, one PR per page fixed
	./run/cultivate

entwine: ## Run the entwine skill as a single whole-garden pass, one PR for all links added
	./run/entwine

fertilize: ## Run the fertilize skill on every page individually, one PR per page expanded
	./run/fertilize

forage: ## Regenerate TODO.md with topics mentioned but not yet sown, one PR
	./run/forage

graft: ## Run the graft skill as a single whole-garden pass, one PR for all merges
	./run/graft

harvest: ## Append a digest of recent garden activity to docs/digests.md, one PR
	./run/harvest

prune: ## Run the prune skill as a single whole-garden pass, one PR for all merges
	./run/prune

sow: ## Plant a brand-new entry for the topic given on the command line
	./run/sow

split: ## Run the split skill on every page individually, one PR per page split
	./run/split

tend: ## Run the tend skill on every page individually, one PR per page fixed
	./run/tend

tidy: ## Run the tidy skill on every page individually, one PR per page improved
	./run/tidy

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: cultivate entwine fertilize forage graft harvest prune sow split tend tidy help
