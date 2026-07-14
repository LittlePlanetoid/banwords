from argparse import Namespace, ArgumentParser, ArgumentDefaultsHelpFormatter
from logging import INFO, DEBUG, _levelToName


log_levels: list[str] = [_levelToName[INFO], _levelToName[DEBUG]]


def cli_args() -> Namespace:

    parser = ArgumentParser(
        prog="banwords CLI", formatter_class=ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("-c", "--conf", default="pyproject.toml", help="tool's conf")
    parser.add_argument(
        "-l",
        "--loglevel",
        choices=log_levels,
        default=_levelToName[INFO],
        help="lvl your logs",
    )
    return parser.parse_args()
