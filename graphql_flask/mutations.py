# mutations.py
import graphene
from models import User, users_db
# from types import UserType
from graphql_types import UserType


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, name, email):
        new_user = User(id=len(users_db) + 1, name=name, email=email)
        users_db.append(new_user)
        return CreateUser(user=new_user)


# mutations.py (add this)
class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, id, name=None, email=None):
        user = next((u for u in users_db if u.id == id), None)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
        return UpdateUser(user=user)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        global users_db
        users_db = [u for u in users_db if u.id != id]
        return DeleteUser(ok=True)

# Register them
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
