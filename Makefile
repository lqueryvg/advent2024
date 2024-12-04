all:
	echo "Nothing to do"

clean:
	find . \( -name coverage.lcov -o \
	  -name .coverage -o \
	  -name .pytest_cache -o \
		-name __pycache__ \
		\) -exec rm -rf {} \;