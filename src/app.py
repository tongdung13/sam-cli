from fastapi import FastAPI
from mangum import Mangum
from core import crontab
from router import demo

import uvicorn
app = FastAPI()

app.include_router(demo.router, prefix='/demo', tags=['demo'])


lambda_handler = Mangum(app)