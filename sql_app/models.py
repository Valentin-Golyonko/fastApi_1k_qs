from sqlalchemy import (
    Column, Integer, Numeric, DateTime, DECIMAL
)

from sql_app.database import Base


class Product(Base):
    __tablename__ = "some_app_product"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    low_price = Column(
        Numeric(
            precision=7,
            scale=2,
            asdecimal=True,
        ),
        default=0.0,
    )
    high_price = Column(
        Numeric(
            precision=7,
            scale=2,
            asdecimal=True,
        ),
        default=0.0,
    )

    demand_qty = Column(
        Integer,
        default=0,
    )
    offers_qty = Column(
        Integer,
        default=0,
    )

    bought_qty = Column(
        Integer,
        default=0,
    )
    sold_qty = Column(
        Integer,
        default=0,
    )

    time_created = Column(
        DateTime,
    )
