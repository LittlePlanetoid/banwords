from banwords import logger

from dataclasses import dataclass
from typing import Optional


@dataclass
class BanwordsConf:
    def __init__(self, conf: dict):

        self.wordslist: Optional[list[str]] = conf.get("wordslist")
        if self.wordslist is None:
            raise Exception("wordslist not found into conf file")

        self.exclude: Optional[list[str]] = conf.get("exclude")
        if self.exclude is None:
            logger.warning("no exclude found into conf file")