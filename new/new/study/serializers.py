from .models import NewUser

from rest_framework import serializers


class NewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}
        fields = ("id", "first_name", "last_name", "email", "phone_number", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields.pop("password")

    def create(self, validated_data):
        user = NewUser.objects.create_user(**validated_data)
        return user


