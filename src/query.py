from utils import get_logger, Database
from typing import List
from models import *
import strawberry
import logging
import asyncio

# init logger
logger = get_logger(logging.INFO)

# database connection
db = Database()

@strawberry.type
class Query:
    
    @strawberry.field
    async def environment(self) -> str:
        return db.env

    @strawberry.field
    async def companies(self) -> List[Company]:

        statement = "SELECT * FROM vw_companies"
        records = db.execute(statement)
        return [
            Company(
                symbol=record[0], 
                name=record[1], 
                url=record[2], 
                category=record[3]
            ) for record in records
        ]       
        
    @strawberry.field
    async def creditCards(self) -> List[CreditCard]:
        
        statement = "SELECT * FROM vw_credit_cards"
        records = db.execute(statement)
        return [
            CreditCard(
                name=record[0], 
                issuer=record[1], 
                type=record[2], 
                network=record[3]
            ) for record in records
        ]      

    @strawberry.field
    async def pricing(self) -> List[Pricing]:

        statement = "SELECT * FROM vw_pricing"
        records = db.execute(statement)
        return [
            Pricing(
                tier=record[0],
                price_monthly=record[1],
                price_yearly=record[2],
                n_discounts=record[3],
                discount_total=record[4],
                discount_pct=record[5],
                discounted_yearly=record[6]
            ) for record in records
        ]

if __name__=="__main__":

    q = Query()