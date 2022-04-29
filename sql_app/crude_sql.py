import logging
from typing import Optional, List

from sqlalchemy.orm import Session

from sql_app import models

logger = logging.getLogger(__name__)


def get_products_v1(db_session: Session,
                    skip: int,
                    limit: int,
                    ) -> List[Optional[models.Product]]:
    try:
        return db_session.query(models.Product).offset(skip).limit(limit).all()
    except Exception as ex:
        logger.exception(f"get_products_v1(): query Ex;"
                         f" {ex = }")
        return []


def get_debug_v1(db_session: Session,
                 skip: int,
                 limit: int,
                 ) -> List[Optional[models.Product]]:
    try:
        return db_session.query(
            models.Product
        ).offset(skip).limit(limit).with_entities(
            models.Product.low_price,
            models.Product.high_price,
        ).all()
    except Exception as ex:
        logger.exception(f"get_debug_v1(): query Ex;"
                         f" {ex = }")
        return []


def get_debug_v3(db_session: Session,
                 skip: int,
                 limit: int,
                 ) -> List[Optional[models.Product]]:
    try:
        data = db_session.query(models.Product).offset(skip).limit(limit)  # .all()
        # for i in data:
        #     i.low_price
        return []
    except Exception as ex:
        logger.exception(f"get_debug_v3(): query Ex;"
                         f" {ex = }")
        return []
