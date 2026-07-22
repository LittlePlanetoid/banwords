from banwords import logger

from dataclasses import dataclass


@dataclass
class BanwordsConf:
    def __init__(self, conf: dict):

        self.wordslist: list[str] = conf.get("wordslist", [])
        if len(self.wordslist) == 0:
            logger.error("wordslist not found into conf file")

        self.exclude: list[str] = conf.get("exclude", [])
        if len(self.exclude) == 0:
            logger.warning("no exclude found into conf file")
