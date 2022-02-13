from schema.types import query, mutation 

from ariadne import ObjectType 
from graphql import GraphQLResolveInfo
from typing import List, Any, Dict
from data import Blog, BlogPayload, all_blogs, get_blog, get_author, update_blog

BLOG_TYPEDEF = """
    type Blog {
        id: ID!
        title: String!
        content: String!
        author: Author!
    }

    input BlogPayload {
        title: String
        content: String
    }

    type Mutation {
        update_blog(id: ID!, payload: BlogPayload!): Blog!
    }
"""

blog_query = ObjectType("Blog")


@query.field("blogs")
def resolve_blogs(_, info: GraphQLResolveInfo) -> List[Blog]:
    return all_blogs()


@query.field("blog")
def resolve_blog(_, info: GraphQLResolveInfo) -> Blog:
    return get_blog()

@mutation.field("update_blog")
def resolve_update_blog(
    _, info: GraphQLResolveInfo, id: str, payload: BlogPayload
) -> Blog:
    return update_blog(int(id), payload)

@blog_query.field("author")
def resolve_blog_author(blog: Dict[str, Any], info: GraphQLResolveInfo):
    #print(blog)
    return get_author(blog["author_id"])