from rest_framework import serializers
from .models import Account
from rest_framework.validators import UniqueValidator


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username", "password", "email", "is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="user with this email already exists.",
                    )
                ]
            },
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
        }

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)
