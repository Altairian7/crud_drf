# queries.py
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description="A simple hello world")

    def resolve_hello(self, info):
        return "Hello, GraphQL!"
