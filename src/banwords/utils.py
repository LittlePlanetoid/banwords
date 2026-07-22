from banwords import logger
from banwords.dataclasses import BanwordsConf

import tomllib
import os

from typing import Optional


def _parse_tomfile(path: str) -> dict:
    try:
        with open(path, "rb") as tfile:
            return tomllib.load(tfile)
    except FileNotFoundError:
        raise FileNotFoundError("conf file was not found")


def get_banwords_conf(path: str) -> BanwordsConf:
    conf = _parse_tomfile(path)
    try:
        return BanwordsConf(conf=conf["tool"]["banwords"])
    except KeyError:
        logger.error("no tool.banwords found")

    logger.error(f"banwords's conf not found into {path}")
    return BanwordsConf(conf={"wordslist": None, "exclude": None})


# TODO: be better for that func
def list_files(
    banwords_conf: BanwordsConf, start_path: str = "."
) -> Optional[list[str]]:
    files_list: list[str] = []
    for root, _, files in os.walk(start_path):
        for file in files:
            full_path = os.path.join(root, file)
            exclude_found = False
            for exclude in banwords_conf.exclude:
                if exclude in full_path:
                    exclude_found = True
            if not exclude_found:
                logger.debug(f"found {full_path}")
                files_list.append(full_path)

    logger.debug(f"{len(files_list)} files found")
    return files_list


def read_file(file: str) -> list[str]:
    """Reads content from a specified file path."""
    try:
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            if len(lines) == 0:
                logger.warning(f"{file} is empty")
        return lines
    except FileNotFoundError:
        print(f"Error: File not found at {file}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return []


def colorize_line(line: str, occurencies: list[str]) -> str:
    # TODO: find occurency(ies) and being/end in line
    # TODO: return formatted line

    return line
