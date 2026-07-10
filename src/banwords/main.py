from banwords import logger
from banwords.cli import cli_args

logger.setLevel(10)

logger.info("checking CLI")
args = cli_args()
logger.debug(args._get_args())

def entry() -> None:
    ...

