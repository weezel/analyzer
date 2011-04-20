## Obtain

	git clone git@github.com:weezel/analyzer.git

Recommended directory structure is something like this:

	.
	..
	glibc
	analyzer

Add some needed softlinks:

	cd glibc/
	ln -s ../analyzer/*.py .
	ln -s ../analyzer/*.gnu .
	ln -s ../analyzer/*.sh .

...and now we are done.

## Usage
Run `./generate_stats.sh` under the glibc directory and

the script will guide for further information.

