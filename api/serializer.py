#-------used to convert data model into json

from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'                               #----Transforming all fields from User model
