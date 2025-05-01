# queries.py (update this)
# from types import UserType
from graphql_types import UserType
from models import users_db

class Query(graphene.ObjectType):
    hello = graphene.String()
    users = graphene.List(UserType)

    def resolve_hello(self, info):
        return "Hello, GraphQL!"

    def resolve_users(self, info):
        return users_db


# queries.py (add to Query class)
user_by_id = graphene.Field(UserType, id=graphene.Int())

def resolve_user_by_id(self, info, id):
    return next((user for user in users_db if user.id == id), None)
