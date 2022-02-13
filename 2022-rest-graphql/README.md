
graph
python app.py # to start 

http:localhost:5000/graphql
- specify data format in the query interface, e.g.:
query {
    blogs{
        id
        name 
        author {
            name
            id
        }
    }
}


## GraphQL
exclamation mark "!" means it is a required field 


## Python 
how to use TypedDict 

TypedDict allows us to declare a structure for dict s, 
mapping their keys (strings) to the types of their values.

`
from typing import TypedDict


class SalesSummary(TypedDict):
    sales: int
    country: str
    product_codes: list[str]


def get_sales_summary() -> SalesSummary:
    """Return summary for yesterday’s sales."""
    return {
        "sales": 1_000,
        "country": "UK",
        "product_codes": ["SUYDT"],
    }

`

