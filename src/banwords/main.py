from banwords import logger
from banwords.cli import cli_args


args = cli_args()
logger.setLevel(args.loglevel)
logger.debug(args.__dict__)

def entry() -> None:
    ...

