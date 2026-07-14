import sys

from banwords import logger
from banwords.cli import cli_args
from banwords.utils import get_banwords_conf, list_files, read_file


args = cli_args()
logger.setLevel(args.loglevel)
logger.debug(f"CLI: {args.__dict__}")


def entry() -> None:
    toml = get_banwords_conf(args.conf)
    logger.debug(f"banwords conf: {toml.__dict__}")
    files = list_files(toml)
    found = False
    for file in files:
        for line in read_file(file):
            for word in toml.wordslist:
                if word in line:
                    found = True
                    print(f"{file} - {line}")

    if found:
        sys.exit(1)
