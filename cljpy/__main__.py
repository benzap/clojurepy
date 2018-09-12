""" Main entry point to 'cljpy' commandline tool
"""

import sys


def main(args=None):
    if args is None:
        args = sys.argv

    print("There be args " + str(args))
