from argparse import Namespace, ArgumentParser
from logging import _nameToLevel, INFO, _levelToName


def cli_args() -> Namespace:

    parser = ArgumentParser(prog="banwords CLI")

    parser.add_argument("-c", "--conf", default="pyproject.toml")
    parser.add_argument("-l", "--loglevel", choices=_nameToLevel.keys(), default=_levelToName[INFO])
    return parser.parse_args()
