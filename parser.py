"""This module contains cmd arguments parser and args"""

from argparse import ArgumentParser

parser = ArgumentParser(
    prog = "BitrixNodes - Servers",
    description = "Servers manager for BitrixNodes staff.",
    usage = "%(prog)s [options]",
)

parser.add_argument(
    "--token",
    type = str,
    help = "Token of pterodactyl API.",
)

parser.add_argument(
    "--verbose",
    action = "store_true",
    default = False,
    help = "Make log level lower (more output)"
)

args = parser.parse_args()