from starlette.applications import Starlette
from strawberry.asgi import GraphQL
from query import Query
import strawberry
import os

schema = strawberry.Schema(
    query=Query, 
    mutation=None, 
    subscription=None
)

graphql_app = GraphQL(schema)

app = Starlette()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)