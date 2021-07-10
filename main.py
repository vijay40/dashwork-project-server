from typing import Optional

import http3
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from QueryController import *

client = http3.AsyncClient()

queryController = QueryController()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root(query: str = ''):
  res = queryController.getMatchingQueries(query)
  json_compatible_item_data = jsonable_encoder(res)
  return JSONResponse(json_compatible_item_data)
