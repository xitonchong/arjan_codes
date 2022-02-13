from data import Author, all_authors, get_author 


from data import Author, all_authors, get_author 
from graphql.type.definition import GraphQLResolveInfo 

from schema.types import query 
from typing import List 

AUTHOR_TYPEDEF = """
    type Author {
        id: ID!
        name: String!
    }
"""


@query.field("authors")
def resolve_authors(_, info: GraphQLResolveInfo) -> List[Author]:
    return all_authors()


@query.field("author")
def resolve_author(_, info: GraphQLResolveInfo, id:str) -> Author:
    return get_author[int(id)]