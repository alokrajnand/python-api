from rest_framework import serializers
from .models import User


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_name', 'phone_number', 'name', 'email_address',
                  'date_of_birth', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# we must have to update the sceanirio for the updating the password also