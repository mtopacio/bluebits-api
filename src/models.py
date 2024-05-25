import strawberry

@strawberry.type
class Company:
    symbol:str
    name:str
    url:str
    category:str

@strawberry.type
class CreditCard:
    name:str
    issuer:str
    type:str
    network:str

@strawberry.type
class Pricing:
    tier:str
    price_monthly: float
    price_yearly: float
    n_discounts: int
    discount_total: float
    discount_pct: str
    discounted_yearly: float