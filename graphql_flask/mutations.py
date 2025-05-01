# mutations.py
import graphene
from models import User, users_db
from types import UserType

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, name, email):
        new_user = User(id=len(users_db) + 1, name=name, email=email)
        users_db.append(new_user)
        return CreateUser(user=new_user)
