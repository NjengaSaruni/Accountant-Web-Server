from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from phonenumber_field import serializerfields

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username','id','first_name', 'last_name')

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='Email already exists. '
                    'Please enter another email or sign in'
        )],
        error_messages={
            'invalid': 'Please enter a valid email address'
        }
    )
    phone_number = serializerfields.PhoneNumberField(
        required=False,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='PhoneNumber already exists. '
                    'Please enter another phonenumber or sign in'
        )],
        )
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        error_messages={
            'max_length': 'Password allows a maximum of 128 characters.',
            'min_length': 'Password allows a minimum of 8 characters.'
        })
    
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
