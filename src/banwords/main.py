import sys

from banwords import logger
from banwords.cli import cli_args
from banwords.utils import get_banwords_conf, list_files, read_file, colorize_line


args = cli_args()
logger.setLevel(args.loglevel)
logger.debug(f"CLI: {args.__dict__}")


def entry() -> None:
    toml = get_banwords_conf(args.conf)
    logger.debug(f"banwords conf: {toml.__dict__}")
    files = list_files(toml)

    if not files:
        logger.warning("no file was found")
        return

    # TODO: do better
    found = False
    for file in files:
        lines = read_file(file)
        if lines:
            for num_line, line in enumerate(lines):
                for word in toml.wordslist:
                    if word in line:
                        found = True
                        print(
                            colorize_line(
                                f"{file} - l.{num_line} - {line}", toml.wordslist
                            ),
                            end="",
                        )

    if found:
        sys.exit(1)
