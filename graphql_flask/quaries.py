# queries.py (update this)
from types import UserType
from models import users_db

class Query(graphene.ObjectType):
    hello = graphene.String()
    users = graphene.List(UserType)

    def resolve_hello(self, info):
        return "Hello, GraphQL!"

    def resolve_users(self, info):
        return users_db
