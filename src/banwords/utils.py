from banwords import logger

import tomllib
import os

from typing import Optional
from dataclasses import dataclass


@dataclass
class BanwordsConf:
    def __init__(self, conf: dict):

        self.wordslist: Optional[list[str]] = conf.get("wordslist")
        if self.wordslist is None:
            raise Exception("wordslist not found into conf file")

        self.exclude: Optional[list[str]] = conf.get("exclude")
        if self.exclude is None:
            logger.warning("no exclude found into conf file")


def _parse_tomfile(path: str) -> dict:
    try:
        with open(path, "rb") as tfile:
            return tomllib.load(tfile)
    except FileNotFoundError:
        raise FileNotFoundError("conf file was not found")


def get_banwords_conf(path: str) -> Optional[BanwordsConf]:
    conf = _parse_tomfile(path)
    try:
        return BanwordsConf(conf=conf["tool"]["banwords"])
    except KeyError:
        logger.error("no tool.banwords found")

    logger.error(f"banwords's conf not found into {path}")
    return None


# TODO: be better for that func
def list_files(banwords_conf: BanwordsConf, start_path: str = ".") -> Optional[str]:
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


def read_file(path: str) -> Optional[list[str]]:
    with open(path, "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            logger.warning(f"{path} is empty")
        return lines
