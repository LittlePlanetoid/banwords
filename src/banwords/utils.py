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


def list_files(start_path: str = ".") -> Optional[str]:
    for root, _, files in os.walk(start_path):
        for file in files:
            print(os.path.join(root, file))