#----------handling logic for API's endpoints

from rest_framework.decorators import api_view
from rest_framework.response import api_view
from rest_framework import status
from .models import User
from .serializer import Userserializers

@api_view(['GET'])
def get_user(request):
    return Response(Userserializers({'name': "Sean", 'age': 21}))