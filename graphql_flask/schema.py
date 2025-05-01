# schema.py (update this)
from queries import Query
from mutations import CreateUser

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
