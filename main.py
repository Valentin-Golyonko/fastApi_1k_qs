from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from sql_app import schemas, crude_sql
from sql_app.database import get_db

fastapi_app = FastAPI()

LIMIT_100 = int(1e2)
LIMIT_1K = int(1e3)
LIMIT_10K = int(1e4)
LIMIT_100K = int(1e5)
LIMIT_1M = int(1e6)


@fastapi_app.get("/")
async def root():
    return {"message": "Hello World"}


@fastapi_app.get(
    path="/v1/",
    response_model=list[schemas.Product],
)
def api_v1(skip: int = 0,
           limit: int = LIMIT_1K,
           db_session: Session = Depends(get_db)):
    """ 43 RPS """
    return crude_sql.get_products_v1(db_session, skip=skip, limit=limit)


@fastapi_app.get(
    path="/debug_v1/",
    # response_model=list[schemas.ProductDebugV1],
)
def api_debug_v1(skip: int = 0,
                 limit: int = LIMIT_100,
                 db_session: Session = Depends(get_db)):
    """ rq: 7ms; 980 RPS """
    out_data = {
        'low_price': [],
        'high_price': [],
    }

    products = crude_sql.get_debug_v1(db_session, skip=skip, limit=limit)
    for product in products:
        out_data['low_price'].append(product[0])
        out_data['high_price'].append(product[1])

    return out_data


@fastapi_app.get(
    path="/debug_v3/",
    response_model=list[schemas.Product],
)
def api_debug_v3(skip: int = 0,
                 limit: int = LIMIT_100K,
                 db_session: Session = Depends(get_db)):
    return crude_sql.get_debug_v3(db_session, skip=skip, limit=limit)
