import sys
if sys.version_info <= (3, 6):
    sys.stdout.write("Sorry, WhoAlias requires Python 3.6+\n")
    sys.exit(1)


from whoalias.whoalias import WhoAlias, run

__version__ = "0.1.0"
__author__  = "github.com/griimnak"

__all__ = ["WhoAlias", "run"]
