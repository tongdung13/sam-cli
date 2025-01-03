from aiocron import crontab
from core import my_logger

logger = my_logger.set_logger(__name__)

@crontab("*/1 * * * *")
async def job():
    logger.info("job -----1-----")
    print("job ------2------")


