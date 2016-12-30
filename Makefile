
test:
	@coverage run $(shell which py.test) tests
	@coverage report -m
	@flake8 distelli
