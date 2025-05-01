# types.py
import graphene
from models import User

class UserType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
