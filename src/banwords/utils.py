from banwords import logger

import tomllib

from typing import Optional
from dataclasses import dataclass


@dataclass
class BanwordsConf:
    def __init__(self, conf: dict):
        self.raw_conf = conf
        self.ban_list = conf.get("ban_list")


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
