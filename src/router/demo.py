from fastapi import APIRouter
from core import my_logger

router = APIRouter()
logger = my_logger.set_logger(__name__)


@router.get('/tet')
async def get_demo():
    logger.info('get_demo')
    return {'message': 'demo'}
