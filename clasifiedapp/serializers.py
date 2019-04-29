from .models import Users
from rest_framework import serializers


class Userserializer(serializers.ModelSerializer):

    photo = serializers.ImageField(max_length=None,use_url=True)


    class Meta:
        model = Users
        fields = ('id','fistname','lastname','email','password','photo')
