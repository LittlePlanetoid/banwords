from argparse import Namespace, ArgumentParser


def cli_args() -> Namespace:

    parser = ArgumentParser(prog="banwords CLI")

    return parser.parse_args()
